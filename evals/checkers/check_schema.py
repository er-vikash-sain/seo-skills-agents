#!/usr/bin/env python3
"""
Deterministic Schema JSON-LD Checker.
Validates that emitted JSON-LD scripts are syntactically valid JSON and contain required Schema.org fields.
"""

import sys
import json
import re

def check_schema(file_path):
    print(f"[*] Checking Schema JSON-LD in: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract JSON-LD blocks from HTML or standalone JSON
    json_ld_blocks = []
    if file_path.endswith('.html'):
        matches = re.findall(r'<script\s+type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
        for m in matches:
            json_ld_blocks.append(m.strip())
    else:
        json_ld_blocks.append(content.strip())

    if not json_ld_blocks:
        print("[!] FAIL: No Schema JSON-LD block found.")
        return 1

    errors = 0
    for idx, block in enumerate(json_ld_blocks):
        try:
            data = json.loads(block)
            context = data.get('@context', '')
            schema_type = data.get('@type', '')
            
            if 'schema.org' not in context:
                print(f"[!] Block {idx+1} FAIL: Invalid @context '{context}'. Must reference schema.org.")
                errors += 1
            if not schema_type:
                print(f"[!] Block {idx+1} FAIL: Missing required @type property.")
                errors += 1
            else:
                print(f"[+] Block {idx+1} PASS: Valid Schema (@type: {schema_type})")
        except json.JSONDecodeError as e:
            print(f"[!] Block {idx+1} FAIL: JSON syntax error: {e}")
            errors += 1

    return 0 if errors == 0 else 1

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 check_schema.py <path_to_file>")
        sys.exit(1)
    sys.exit(check_schema(sys.argv[1]))
