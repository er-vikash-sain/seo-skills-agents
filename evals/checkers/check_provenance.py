#!/usr/bin/env python3
"""
CORE ANTI-HALLUCINATION GATE: Deterministic Provenance Checker.
Validates that every factual metric, ranking gain, impression number, or conversion count
in a report explicitly cites a valid source file [Source: <path>], verifies the source file exists,
AND asserts that the claimed numeric value actually exists inside the content of the source file.
"""

import sys
import os
import re

def check_provenance(report_path):
    print(f"[*] CORE PROVENANCE GATE: Verifying metric claims in {report_path}")
    if not os.path.exists(report_path):
        print(f"[!] FAIL: Report file does not exist: {report_path}")
        return 1

    with open(report_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    errors = []
    metric_pattern = re.compile(r'(\+?\d+%\b|\b\d+\s+(leads|conversions|terms|keywords|pages|impressions)\b|\b\d{2,}\b)', re.IGNORECASE)
    source_pattern = re.compile(r'\[Source:\s*([^\s\]]+)\]', re.IGNORECASE)

    for line_num, line in enumerate(lines, start=1):
        line_str = line.strip()
        # Skip headers or empty lines
        if line_str.startswith("#") or not line_str:
            continue

        # Check if line contains a metric claim
        metric_match = metric_pattern.search(line_str)
        if metric_match:
            source_match = source_pattern.search(line_str)
            if not source_match:
                errors.append(f"Line {line_num}: Unsourced metric claim -> '{line_str}'")
            else:
                source_file = source_match.group(1)
                if not os.path.exists(source_file):
                    errors.append(f"Line {line_num}: Source file referenced in '{line_str}' does not exist on disk ('{source_file}')")
                else:
                    # Deep Value Verification: Check if claimed numeric value exists in source file content
                    claimed_val = metric_match.group(1).strip()
                    # Extract raw number digits or string snippet
                    digits_match = re.search(r'\d+', claimed_val)
                    if digits_match:
                        raw_digits = digits_match.group(0)
                        with open(source_file, 'r', encoding='utf-8', errors='ignore') as sf:
                            source_content = sf.read()
                        if raw_digits not in source_content:
                            errors.append(f"Line {line_num}: Claimed metric value '{claimed_val}' (digit '{raw_digits}') not found in source file content ('{source_file}')")

    if errors:
        print(f"[!] CORE PROVENANCE GATE FAILED for {report_path}:")
        for err in errors:
            print(f"    - {err}")
        return 1
    else:
        print(f"[+] CORE PROVENANCE GATE PASSED for {report_path}: 100% metrics grounded and verified in source file content.")
        return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 check_provenance.py <path_to_report.md>")
        sys.exit(1)
    sys.exit(check_provenance(sys.argv[1]))
