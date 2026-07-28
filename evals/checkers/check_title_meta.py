#!/usr/bin/env python3
"""
Deterministic Title & Meta Description Length Checker.
Validates title tag <= 65 chars and meta description <= 160 chars.
"""

import sys
import re

def check_title_meta(file_path):
    print(f"[*] Checking Title & Meta limits in: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = 0
    # Match <title>
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    if title_match:
        title = title_match.group(1).strip()
        if len(title) > 65:
            print(f"[!] FAIL: Title length ({len(title)} chars) exceeds 65 char limit: '{title}'")
            errors += 1
        else:
            print(f"[+] PASS: Title length ({len(title)} chars) is within limits.")
    else:
        print("[!] WARNING: No <title> tag found in HTML fixture.")

    # Match <meta name="description">
    meta_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', content, re.IGNORECASE)
    if meta_match:
        desc = meta_match.group(1).strip()
        if len(desc) > 160:
            print(f"[!] FAIL: Meta description length ({len(desc)} chars) exceeds 160 char limit.")
            errors += 1
        else:
            print(f"[+] PASS: Meta description length ({len(desc)} chars) is within limits.")
    else:
        print("[!] WARNING: No meta description tag found in HTML fixture.")

    return 0 if errors == 0 else 1

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 check_title_meta.py <path_to_file>")
        sys.exit(1)
    sys.exit(check_title_meta(sys.argv[1]))
