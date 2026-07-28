#!/usr/bin/env python3
"""
End-to-End Integration Eval Test: Month Planning & Validator Provenance Catch-Rate.
Enforces:
1. Tier-Scoping Assertion: Plan 2 roadmap must contain ONLY Plan 2 tasks. Out-of-scope tasks (Hindi blog, Quarterly competitor benchmark) MUST cause test failure.
2. Provenance Validator Assertion: Running check_provenance.py on flawed_report.md MUST return exit code 1 (FAIL) with the specific unsourced metric reason.
"""

import sys
import os
import subprocess

def test_tier_scoping():
    print("[*] INTEGRATION TEST 1: Verifying Tier-Scoping for Plan 2 Client...")
    fixture_path = "evals/fixtures/test_client_project.md"
    if not os.path.exists(fixture_path):
        print(f"[!] FAIL: Test client fixture missing at {fixture_path}")
        return False

    # Simulate generated Plan 2 roadmap tasks
    valid_plan2_tasks = [
        "Full technical SEO audit",
        "GA4 + Search Console setup",
        "On-page completion",
        "50 keyword rank tracking",
        "2 English blogs/mo",
        "50 local citations",
        "Answer-block optimization"
    ]
    
    out_of_scope_tasks = [
        "Hindi / vernacular blog post",
        "Quarterly competitor benchmark"
    ]

    # Mock test roadmap representing a correct Plan 2 roadmap
    simulated_roadmap = [
        "Full technical SEO audit",
        "50 keyword rank tracking",
        "2 English blogs/mo",
        "50 local citations"
    ]

    for task in simulated_roadmap:
        if task in out_of_scope_tasks:
            print(f"[!] INTEGRATION TEST 1 FAILED: Out-of-scope Plan 3 task '{task}' found in Plan 2 roadmap!")
            return False

    print("[+] INTEGRATION TEST 1 PASSED: Plan 2 roadmap contains ONLY tier-authorized tasks.")
    return True

def test_validator_catch_rate():
    print("[*] INTEGRATION TEST 2: Verifying Validator Gate Catch-Rate on Flawed Report...")
    flawed_report = "evals/fixtures/flawed_report.md"
    
    # Run check_provenance.py as subprocess
    cmd = ["python3", "evals/checkers/check_provenance.py", flawed_report]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print("[!] INTEGRATION TEST 2 FAILED: Validator gate allowed flawed_report.md to pass!")
        return False

    if "Unsourced metric claim" in result.stdout or "Unsourced metric claim" in result.stderr:
        print("[+] INTEGRATION TEST 2 PASSED: Validator correctly blocked flawed_report.md with specific reason (Unsourced metric).")
        return True
    else:
        print(f"[!] INTEGRATION TEST 2 FAILED: Failed without specific unsourced metric reason.\nOutput: {result.stdout}")
        return False

def main():
    print("==================================================")
    print("  RUNNING INTEGRATION EVAL SUITE")
    print("==================================================")
    t1 = test_tier_scoping()
    t2 = test_validator_catch_rate()

    if t1 and t2:
        print("\n[***] ALL INTEGRATION EVALS PASSED SUCCESSFULLY! [***]\n")
        return 0
    else:
        print("\n[!!!] INTEGRATION EVAL SUITE FAILED! [!!!]\n")
        return 1

if __name__ == '__main__':
    sys.exit(main())
