#!/usr/bin/env python3
"""
Deterministic Internal Link Resolver Checker.
Validates internal link anchors and checks for dead or malformed anchor targets.
"""

import sys
import re

def check_internal_links(file_path):
    print(f"[*] Checking internal links in: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    links = re.findall(r'<a\s+[^>]*href=["\'](.*?)["\'][^>]*>(.*?)</a>', content, re.IGNORECASE)
    if not links:
        print("[!] WARNING: No links found in file.")
        return 0

    errors = 0
    for href, anchor in links:
        if not anchor.strip():
            print(f"[!] FAIL: Empty anchor text for link '{href}'")
            errors += 1
        if href == "#" or href == "":
            print(f"[!] FAIL: Dead/empty href target: '{href}'")
            errors += 1

    if errors == 0:
        print(f"[+] PASS: Validated {len(links)} internal links with non-empty anchors.")
        return 0
    else:
        return 1

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 check_internal_links.py <path_to_file>")
        sys.exit(1)
    sys.exit(check_internal_links(sys.argv[1]))
