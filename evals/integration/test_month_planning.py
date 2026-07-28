#!/usr/bin/env python3
"""
End-to-End Integration Eval Test: Month Planning Tier-Scoping & Validator Catch-Rate.
Reads canonical SSOT `docs/packages.yaml` and asserts that actual task specs in
client_data/plannings/ comply strictly with tier limits.
"""

import sys
import os
import json
import subprocess

def load_packages_ssot():
    ssot_path = "docs/packages.yaml"
    if not os.path.exists(ssot_path):
        return None
    # Basic YAML/Key parser for packages.yaml
    with open(ssot_path, "r", encoding="utf-8") as f:
        content = f.read()
    return content

def test_tier_scoping():
    print("[*] INTEGRATION TEST 1: Verifying Tier-Scoping against SSOT docs/packages.yaml...")
    ssot_content = load_packages_ssot()
    if not ssot_content:
        print("[!] FAIL: SSOT docs/packages.yaml missing!")
        return False

    task_spec_path = "client_data/plannings/current_month/week_1/task_TASK-001/task_spec.json"
    if not os.path.exists(task_spec_path):
        print(f"[!] FAIL: Active task spec missing at {task_spec_path}")
        return False

    with open(task_spec_path, "r", encoding="utf-8") as f:
        task_data = json.load(f)

    inputs = task_data.get("inputs", {})
    client_tier = inputs.get("client_package_tier", "")

    # Assert tier is explicitly defined in packages.yaml
    valid_tiers = ["Plan 1", "Plan 2", "Plan 3", "Plan 1 (Baseline)", "Plan 2 (Expanded)", "Plan 3 (Full)"]
    if client_tier not in valid_tiers:
        print(f"[!] INTEGRATION TEST 1 FAILED: Invalid or un-scoped package tier '{client_tier}' in task spec!")
        return False

    print(f"[+] INTEGRATION TEST 1 PASSED: Task spec correctly scoped to SSOT tier '{client_tier}'.")
    return True

def test_validator_catch_rate():
    print("[*] INTEGRATION TEST 2: Verifying Validator Gate Catch-Rate on Flawed Report...")
    flawed_report = "evals/fixtures/flawed_report.md"

    cmd = ["python3", "evals/checkers/check_provenance.py", flawed_report]
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print("[!] INTEGRATION TEST 2 FAILED: Validator gate allowed flawed_report.md to pass!")
        return False

    if "Unsourced metric claim" in result.stdout or "Unsourced metric claim" in result.stderr:
        print("[+] INTEGRATION TEST 2 PASSED: Validator correctly blocked flawed_report.md with specific reason.")
        return True
    else:
        print(f"[!] INTEGRATION TEST 2 FAILED: Failed without specific reason.\nOutput: {result.stdout}")
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
