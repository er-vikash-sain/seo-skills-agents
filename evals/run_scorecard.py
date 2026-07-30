#!/usr/bin/env python3
"""
Framework Scorecard Runner & Regression Gate Validator.
Executes all deterministic checkers and integration tests.
Calculates Metrics:
- Schema Validity %
- Meta Limits Compliance %
- Internal Link Health %
- Provenance/Groundedness %
- Validator Flawed-Report Catch-Rate %
- Hallucination Incident Count

REGRESSION GATE RULE: All checks must achieve 100% pass rate before framework updates can be committed.
"""

import sys
import os
import subprocess

def run_checker(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0, result.stdout + result.stderr

def main():
    print("==================================================")
    print("  AI AGENCY OS — EVAL SCORECARD RUNNER")
    print("==================================================")

    total_checks = 0
    passed_checks = 0
    hallucination_incidents = 0

    # 1. Schema Checker Test
    total_checks += 1
    p1, out1 = run_checker(["python3", "evals/checkers/check_schema.py", "evals/fixtures/sample_page.html"])
    if p1:
        passed_checks += 1
        print("  [✓] Schema JSON-LD Checker: 100% PASS")
    else:
        print("  [✗] Schema JSON-LD Checker: FAIL\n", out1)

    # 2. Title & Meta Checker Test
    total_checks += 1
    p2, out2 = run_checker(["python3", "evals/checkers/check_title_meta.py", "evals/fixtures/sample_page.html"])
    if p2:
        passed_checks += 1
        print("  [✓] Title & Meta Limits Checker: 100% PASS")
    else:
        print("  [✗] Title & Meta Limits Checker: FAIL\n", out2)

    # 3. Internal Links Checker Test
    total_checks += 1
    p3, out3 = run_checker(["python3", "evals/checkers/check_internal_links.py", "evals/fixtures/sample_page.html"])
    if p3:
        passed_checks += 1
        print("  [✓] Internal Links Resolver Checker: 100% PASS")
    else:
        print("  [✗] Internal Links Resolver Checker: FAIL\n", out3)

    # 4. Provenance Anti-Hallucination Gate (Grounded Report)
    total_checks += 1
    p4, out4 = run_checker(["python3", "evals/checkers/check_provenance.py", "evals/fixtures/grounded_report.md"])
    if p4:
        passed_checks += 1
        print("  [✓] Core Provenance Gate (Grounded Report): 100% PASS")
    else:
        print("  [✗] Core Provenance Gate (Grounded Report): FAIL\n", out4)
        hallucination_incidents += 1

    # 5. Provenance Anti-Hallucination Gate (Flawed Report - Catch Test)
    total_checks += 1
    p5_pass, out5 = run_checker(["python3", "evals/checkers/check_provenance.py", "evals/fixtures/flawed_report.md"])
    # Flawed report MUST return non-zero (blocked)
    if not p5_pass and "Unsourced metric claim" in out5:
        passed_checks += 1
        print("  [✓] Provenance Validator Gate (Catch Flawed Report): 100% PASS (Successfully Blocked)")
    else:
        print("  [✗] Provenance Validator Gate (Catch Flawed Report): FAIL (Flawed report was not blocked!)\n", out5)

    # 6. Integration Test
    total_checks += 1
    p6, out6 = run_checker(["python3", "evals/integration/test_month_planning.py"])
    if p6:
        passed_checks += 1
        print("  [✓] Integration Planning & Tier-Scoping Suite: 100% PASS")
    else:
        print("  [✗] Integration Planning & Tier-Scoping Suite: FAIL\n", out6)

    # 7. Architecture Fitness Function Test
    total_checks += 1
    p7, out7 = run_checker(["python3", "evals/checkers/check_architecture_fitness.py"])
    if p7:
        passed_checks += 1
        print("  [✓] Architecture Fitness Function: 100% PASS (All Agents, Skills & Registry Indexes Verified)")
    else:
        print("  [✗] Architecture Fitness Function: FAIL\n", out7)

    # 8. State JSON Schema Conformance Test
    total_checks += 1
    p8, out8 = run_checker(["python3", "evals/checkers/check_state_schemas.py"])
    if p8:
        passed_checks += 1
        print("  [✓] State JSON Schema Conformance Gate: 100% PASS")
    else:
        print("  [✗] State JSON Schema Conformance Gate: FAIL\n", out8)

    # 9. AI Slop & Humanizer Checker Test (Clean Draft Pass)
    total_checks += 1
    p9, out9 = run_checker(["python3", "evals/checkers/check_ai_slop.py", "evals/fixtures/clean_draft.md"])
    if p9:
        passed_checks += 1
        print("  [✓] AI Humanizer Slop Checker (Clean Draft): 100% PASS")
    else:
        print("  [✗] AI Humanizer Slop Checker (Clean Draft): FAIL\n", out9)

    # 10. AI Slop & Humanizer Checker Test (Catch Slop Draft Pass)
    total_checks += 1
    p10_pass, out10 = run_checker(["python3", "evals/checkers/check_ai_slop.py", "evals/fixtures/slop_draft.md"])
    if not p10_pass and "AI SLOP AUDIT FAILED" in out10:
        passed_checks += 1
        print("  [✓] AI Humanizer Slop Validator (Catch Slop Draft): 100% PASS (Successfully Blocked)")
    else:
        print("  [✗] AI Humanizer Slop Validator (Catch Slop Draft): FAIL (Slop draft was not blocked!)\n", out10)

    # 11. CORE-EEAT Content Quality Evaluator Test
    total_checks += 1
    p11, out11 = run_checker(["python3", "evals/checkers/check_eeat_score.py", "evals/fixtures/clean_draft.md"])
    if p11:
        passed_checks += 1
        print("  [✓] CORE-EEAT Quality Gate Evaluator: 100% PASS (Verdict: SHIP)")
    else:
        print("  [✗] CORE-EEAT Quality Gate Evaluator: FAIL\n", out11)

    pass_rate = (passed_checks / total_checks) * 100.0
    print("\n--------------------------------------------------")
    print(f"  SCORECARD METRICS:")
    print(f"  - Total Evaluated Checks: {total_checks}")
    print(f"  - Passed Checks: {passed_checks}")
    print(f"  - Pass Rate: {pass_rate:.1f}%")
    print(f"  - Hallucination Incident Count: {hallucination_incidents}")
    print("--------------------------------------------------")

    if pass_rate == 100.0 and hallucination_incidents == 0:
        print("\n[***] REGRESSION GATE PASSED: All evaluators 100% clean. Framework ready for client deployment. [***]\n")
        return 0
    else:
        print("\n[!!!] REGRESSION GATE FAILED: Framework contains failures or unbacked metrics. Blocked from commit. [!!!]\n")
        return 1

if __name__ == '__main__':
    sys.exit(main())
