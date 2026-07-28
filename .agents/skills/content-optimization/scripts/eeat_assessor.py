#!/usr/bin/env python3
"""
E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) Signal Assessor.
Audits web pages for author bylines, expert credentials, external citations, and trust signals.
"""

import sys
import json
from html.parser import HTMLParser

class EEATParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_blocks = []
        self.external_links = []
        self.has_author_byline = False
        self.has_citations = False

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if tag == "a" and "href" in attr_dict:
            href = attr_dict["href"]
            if href.startswith("http://") or href.startswith("https://"):
                self.external_links.append(href)
        elif tag == "meta":
            if attr_dict.get("name", "").lower() == "author":
                self.has_author_byline = True

    def handle_data(self, data):
        cleaned = data.strip().lower()
        if "author" in cleaned or "written by" in cleaned or "edited by" in cleaned or "reviewed by" in cleaned:
            self.has_author_byline = True
        if "references" in cleaned or "sources" in cleaned or "citations" in cleaned:
            self.has_citations = True

def assess_eeat_signals(url_or_html):
    parser = EEATParser()
    if url_or_html.startswith("http://") or url_or_html.startswith("https://"):
        import urllib.request
        try:
            req = urllib.request.Request(url_or_html, headers={"User-Agent": "EEAT-Assessor/1.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                content = resp.read().decode("utf-8", errors="ignore")
        except Exception as e:
            return {"error": str(e), "status": "Failed"}
    else:
        content = url_or_html

    parser.feed(content)

    external_link_count = len(parser.external_links)
    has_author = parser.has_author_byline
    has_sources = parser.has_citations or external_link_count >= 2

    score = 40
    if has_author:
        score += 30
    if has_sources:
        score += 30

    rating = "Strong E-E-A-T" if score >= 80 else ("Moderate E-E-A-T" if score >= 60 else "Weak E-E-A-T (Needs Author & Citations)")

    return {
        "eeat_score": score,
        "rating": rating,
        "signals": {
            "author_byline_detected": has_author,
            "citations_or_references_detected": has_sources,
            "external_reference_links": external_link_count
        },
        "recommendations": [
            "Add explicit author bio box with credentials",
            "Include 2+ external citations to authoritative sources"
        ] if score < 80 else []
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "URL or HTML file path required"}))
        sys.exit(1)

    target = sys.argv[1]
    result = assess_eeat_signals(target)
    print(json.dumps(result, indent=2))
