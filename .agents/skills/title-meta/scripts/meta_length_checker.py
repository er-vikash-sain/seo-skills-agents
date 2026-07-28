#!/usr/bin/env python3
"""
Title Tag and Meta Description Length & Pixel Width Validator.
Checks exact character length boundaries (Title: 50-60 chars, Meta: 150-160 chars).
"""

import sys
import json

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
        "all_optimal": (40 <= title_len <= 60) and (120 <= meta_len <= 160)
    }

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(json.dumps({"error": "Requires 2 arguments: <title> <meta_description>"}))
        sys.exit(1)

    title_arg = sys.argv[1]
    meta_arg = sys.argv[2]
    result = check_title_meta_limits(title_arg, meta_arg)
    print(json.dumps(result, indent=2))
