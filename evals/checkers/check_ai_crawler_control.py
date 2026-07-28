#!/usr/bin/env python3
"""
Deterministic AI Crawler Control Syntax Checker.
Validates User-agent and Disallow/Allow directives in robots.txt / llms.txt.
"""

import sys

def check_ai_crawler_control(file_path):
    print(f"[*] Checking AI Crawler directives in: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    has_user_agent = False
    has_directive = False

    for line in lines:
        line_str = line.strip()
        if line_str.startswith("User-agent:"):
            has_user_agent = True
        if line_str.startswith("Disallow:") or line_str.startswith("Allow:"):
            has_directive = True

    if has_user_agent and has_directive:
        print("[+] PASS: Valid robots.txt / llms.txt crawler directive formatting.")
        return 0
    else:
        print("[!] FAIL: Missing User-agent or Disallow/Allow directives.")
        return 1

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 check_ai_crawler_control.py <path_to_file>")
        sys.exit(1)
    sys.exit(check_ai_crawler_control(sys.argv[1]))
