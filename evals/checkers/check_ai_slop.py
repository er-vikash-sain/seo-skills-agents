#!/usr/bin/env python3
"""
Deterministic AI Slop & Cliché Checker.
Audits English and Hindi markdown drafts for blacklisted AI writing patterns.

Exit Codes:
  0: Clean content pass (0 slop phrases found)
  1: AI Slop detected (exceeds threshold)
"""

import sys
import re
import os

ENGLISH_SLOP_PATTERNS = [
    r"\bpivotal role\b",
    r"\bserves as a testament\b",
    r"\btestament to\b",
    r"\bevolving landscape\b",
    r"\bin today's (?:fast-paced |digital |modern )?world\b",
    r"\bdelve into\b",
    r"\bmultifaceted realm\b",
    r"\bnestled in the heart of\b",
    r"\bit's not just a\b",
    r"\bnot only does it\b",
    r"\bin conclusion,\b",
    r"\bultimately, only time will tell\b",
    r"\bboasts a rich\b",
]

HINDI_SLOP_PATTERNS = [
    r"आज के इस डिजिटल युग में",
    r"महत्वपूर्ण भूमिका निभाता है",
    r"मील का पत्थर साबित",
    r"जीवित प्रमाण",
    r"निष्कर्ष के रूप में, यह कहा जा सकता है कि",
    r"सॉफ़्टवेयर अभियांत्रिकी",
    r"मेघ संगणन",
    r"मशीन शिक्षण",
]

def audit_file(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    detected_slop = []

    # Check English patterns
    for pattern in ENGLISH_SLOP_PATTERNS:
        matches = re.findall(pattern, content, re.IGNORECASE)
        if matches:
            detected_slop.append((pattern, len(matches), "English"))

    # Check Hindi patterns
    for pattern in HINDI_SLOP_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            detected_slop.append((pattern, len(matches), "Hindi"))

    if detected_slop:
        print(f"AI SLOP AUDIT FAILED for '{file_path}':")
        for pat, count, lang in detected_slop:
            print(f"  - [{lang}] Pattern '{pat}' matched {count} time(s).")
        return False
    else:
        print(f"AI SLOP AUDIT PASSED for '{file_path}': 0 AI clichés detected.")
        return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check_ai_slop.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    success = audit_file(file_path)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
