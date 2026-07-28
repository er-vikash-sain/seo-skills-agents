#!/usr/bin/env python3
"""
Title Tag and Meta Description Length & Pixel Width Validator.
Checks character length boundaries (Title: 40-60 chars, Meta: 120-160 chars).
"""

import sys
import json
import argparse

def check_title_meta_limits(title, meta_desc):
    title_len = len(title)
    meta_len = len(meta_desc)

    title_status = "Optimal"
    if title_len < 40:
        title_status = "Too Short (Under 40 chars)"
    elif title_len > 60:
        title_status = "Too Long (Triggers truncation in SERP, Over 60 chars)"

    meta_status = "Optimal"
    if meta_len < 120:
        meta_status = "Too Short (Under 120 chars)"
    elif meta_len > 160:
        meta_status = "Too Long (Triggers truncation in SERP, Over 160 chars)"

    all_optimal = (40 <= title_len <= 60) and (120 <= meta_len <= 160)
    return {
        "title": {
            "text": title,
            "length": title_len,
            "status": title_status,
            "pass": 40 <= title_len <= 60
        },
        "meta_description": {
            "text": meta_desc,
            "length": meta_len,
            "status": meta_status,
            "pass": 120 <= meta_len <= 160
        },
        "all_optimal": all_optimal
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate Title tag and Meta description character boundaries.")
    parser.add_argument("title", help="Page Title tag string")
    parser.add_argument("meta", help="Meta Description string")
    args = parser.parse_args()

    result = check_title_meta_limits(args.title, args.meta)
    print(json.dumps(result, indent=2))
    if not result.get("all_optimal", False):
        sys.exit(1)
    sys.exit(0)
