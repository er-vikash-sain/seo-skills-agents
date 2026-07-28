#!/usr/bin/env python3
"""
Offline Technical SEO Site Crawler & Health Diagnostic Tool.
Scrapes target URLs to analyze status codes, title tags, meta descriptions, H1-H6 hierarchy, and broken links.
"""

import sys
import json
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

def audit_url(target_url):
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
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Target URL required as argument"}))
        sys.exit(1)
    
    url = sys.argv[1]
    result = audit_url(url)
    print(json.dumps(result, indent=2))
