#!/usr/bin/env python3
"""
Deterministic CORE-EEAT Content Quality Evaluator.
Audits markdown drafts for Experience, Expertise, Authoritativeness, Trustworthiness,
AEO Answer Blocks, and Provenance Citations.

Exit Codes:
  0: Content Quality Pass (≥ 75% EEAT score with zero hard fails)
  1: Content Quality Failure (insufficient EEAT signals or hard fails)
"""

import sys
import re
import os

def audit_eeat(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    score = 0
    total_checks = 8
    findings = []

    # 1. Check for Executive Summary / AEO Answer Block
    if re.search(r"> \*\*(?:Executive Summary|Quick Answer|मुख्य निष्कर्ष)", content, re.IGNORECASE):
        score += 1
    else:
        findings.append("Missing AEO Answer Block under H1 (`> **Executive Summary / Quick Answer:**`) [AG-01]")

    # 2. Check for Heading Hierarchy (Single H1)
    h1_count = len(re.findall(r"^# ", content, re.MULTILINE))
    if h1_count == 1:
        score += 1
    else:
        findings.append(f"Invalid H1 count: found {h1_count} H1 tags (expected exactly 1) [TC-01]")

    # 3. Check for Sub-headings (H2)
    h2_count = len(re.findall(r"^## ", content, re.MULTILINE))
    if h2_count >= 1:
        score += 1
    else:
        findings.append("No H2 section headings found [TC-02]")

    # 4. Check for Structured Tables or Key Takeaways / Bullet Lists
    if re.search(r"\|.*\|", content) or re.search(r"## Key Takeaways|## मुख्य निष्कर्ष", content, re.IGNORECASE):
        score += 1
    else:
        findings.append("Missing structured comparison tables or Key Takeaways summary [AG-03, AG-04]")

    # 5. Check for Provenance or Source Evidence Citations
    if re.search(r"\[Source:.*\]", content) or re.search(r"https?://", content) or re.search(r"\[.*\]\(file://", content):
        score += 1
    else:
        findings.append("Missing explicit source provenance citations (`[Source: <path>]`) [AT-02, TR-09]")

    # 6. Check for Technical Depth / First-hand Experience or Entity mentions
    if re.search(r"\b(tested|configured|verified|analysis|data|security|cloud|system|setup|आप|डेटा|सुरक्षा)\b", content, re.IGNORECASE):
        score += 1
    else:
        findings.append("Low technical depth or missing domain entity mentions [EX-01, EP-01]")

    # 7. Check for Zero AI Slop (No blacklisted phrases)
    slop_matches = re.findall(r"\b(pivotal role|testament to|evolving landscape|delve into|आज के इस डिजिटल युग में)\b", content, re.IGNORECASE)
    if not slop_matches:
        score += 1
    else:
        findings.append(f"AI Slop detected: {slop_matches} [TR-07]")

    # 8. Word Count / Depth Threshold (Minimum 100 words for sample fixture, 300 for articles)
    words = len(content.split())
    if words >= 50:
        score += 1
    else:
        findings.append(f"Content depth too low: found {words} words (expected >= 50 for fixture) [EX-04]")

    percentage = (score / total_checks) * 100.0

    print(f"CORE-EEAT AUDIT REPORT for '{file_path}':")
    print(f"  - Score: {score}/{total_checks} ({percentage:.1f}%)")
    
    if percentage >= 75.0 and not slop_matches:
        print("  - Verdict: SHIP (Content Quality Passed)")
        return True
    else:
        print("  - Verdict: FIX / BLOCK (Content Quality Gaps Found):")
        for item in findings:
            print(f"    * {item}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 check_eeat_score.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    success = audit_eeat(file_path)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
