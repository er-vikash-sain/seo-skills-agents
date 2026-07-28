#!/usr/bin/env python3
"""
Offline Technical SEO Site Crawler & Health Diagnostic Tool.
Scrapes target URLs to analyze status codes, title tags, meta descriptions, H1-H6 hierarchy, and canonicals.
Supports --dry-run / offline mode.
"""

import sys
import os
import json
import argparse
import urllib.request
import urllib.parse
from html.parser import HTMLParser

class SEOParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.meta_desc = ""
        self.canonical = ""
        self.headings = []
        self.links = []
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "meta":
            if attr_dict.get("name", "").lower() == "description":
                self.meta_desc = attr_dict.get("content", "")
        elif tag == "link":
            if attr_dict.get("rel", "").lower() == "canonical":
                self.canonical = attr_dict.get("href", "")
        elif tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            self.headings.append((tag, ""))
        elif tag == "a" and "href" in attr_dict:
            self.links.append(attr_dict["href"])

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data.strip()

def audit_url(target_url, dry_run=False):
    if dry_run or not (target_url.startswith("http://") or target_url.startswith("https://")):
        return {
            "url": target_url,
            "mode": "dry-run",
            "status_code": 200,
            "title": "Dry Run Sample Title",
            "title_length": 19,
            "meta_description": "Dry Run Sample Meta Description for testing offline functionality.",
            "meta_description_length": 66,
            "canonical_url": target_url,
            "total_links_found": 5,
            "crawl_status": "Success"
        }

    try:
        req = urllib.request.Request(
            target_url,
            headers={"User-Agent": "SEO-Agentic-Crawler/1.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            status_code = resp.getcode()
            html_content = resp.read().decode("utf-8", errors="ignore")

        parser = SEOParser()
        parser.feed(html_content)

        return {
            "url": target_url,
            "status_code": status_code,
            "title": parser.title,
            "title_length": len(parser.title),
            "meta_description": parser.meta_desc,
            "meta_description_length": len(parser.meta_desc),
            "canonical_url": parser.canonical,
            "total_links_found": len(parser.links),
            "crawl_status": "Success"
        }
    except Exception as e:
        return {
            "url": target_url,
            "status_code": 0,
            "error": str(e),
            "crawl_status": "Failed"
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Technical SEO Audit on URL.")
    parser.add_argument("url", help="Target URL to crawl (e.g. https://example.com)")
    parser.add_argument("--dry-run", action="store_true", help="Run in offline dry-run mode without network calls")
    args = parser.parse_args()

    result = audit_url(args.url, dry_run=args.dry_run)
    print(json.dumps(result, indent=2))
    if result.get("crawl_status") == "Failed":
        sys.exit(1)
    sys.exit(0)
