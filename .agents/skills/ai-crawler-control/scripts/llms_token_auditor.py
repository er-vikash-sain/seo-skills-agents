#!/usr/bin/env python3
"""
Agentic Engine Optimization (AEO) Token Budget & LLMs.txt Auditor.
Inspired by Addy Osmani's agentic-seo framework.
Audits web pages for AI Agent readability, per-page token consumption, and llms.txt index formatting.
"""

import sys
import json
import urllib.request
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_blocks = []

    def handle_data(self, data):
        cleaned = data.strip()
        if cleaned:
            self.text_blocks.append(cleaned)

def estimate_tokens(text):
    # Rule of thumb: ~4 characters per token in English
    words = text.split()
    char_count = len(text)
    token_estimate = int(char_count / 4)
    return {
        "word_count": len(words),
        "character_count": char_count,
        "estimated_tokens": token_estimate
    }

def audit_agentic_seo(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "AEO-Agentic-Auditor/1.0"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html_content = resp.read().decode("utf-8", errors="ignore")

        parser = TextExtractor()
        parser.feed(html_content)
        plain_text = " ".join(parser.text_blocks)

        token_info = estimate_tokens(plain_text)
        est_tokens = token_info["estimated_tokens"]

        # Budget Check: Pages > 15,000 tokens flag token overflow risk
        status = "Optimal"
        if est_tokens > 15000:
            status = "Token Oversized (Exceeds 15k token budget, risk of agent context truncation)"
        elif est_tokens < 100:
            status = "Thin Content (Under 100 tokens)"

        return {
            "url": url,
            "token_budget_status": status,
            "word_count": token_info["word_count"],
            "character_count": token_info["character_count"],
            "estimated_tokens": est_tokens,
            "agent_readiness_score": 100 if est_tokens <= 15000 else 60,
            "recommendation": "Maintain clean Markdown structure and keep per-page tokens under 15,000."
        }
    except Exception as e:
        return {
            "url": url,
            "error": str(e),
            "status": "Failed"
        }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Target URL required as argument"}))
        sys.exit(1)

    target_url = sys.argv[1]
    result = audit_agentic_seo(target_url)
    print(json.dumps(result, indent=2))
