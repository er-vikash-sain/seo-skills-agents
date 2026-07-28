---
name: competitor-benchmark
description: Conducts quarterly competitor benchmarking, compares domain metrics, backlink velocity, and search market share based on package tier.
version: "1.0.0"
---

# Instructions

## Role
Performs mechanical competitor data collection, benchmark comparisons, and domain metrics tracking (Domain Authority, backlink count, estimated traffic, topic share).

## Inputs
- `client_package_tier`: Plan 1 (Not included), Plan 2 (Not included / basic check), Plan 3 (Quarterly Competitor Benchmark report).
- Top 3 competitor domain URLs and client domain URL.

## Procedure
1. Harvest competitor visibility metrics, backlink totals, top ranking pages, and AI citation presence.
2. Build comparative metrics matrix comparing client performance against competitors.
3. **Tier Variation:**
   - **Plan 1 & 2:** Skipped or basic top competitor overview.
   - **Plan 3:** Complete Quarterly Competitor Benchmark report evaluating market share gaps & growth trends.
4. Output Competitor Benchmark Matrix.

## Output & Evidence
- **File:** `artifacts/competitor_benchmark_report.md`
- **Status Note:** Logs competitor gap summary to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if competitor launches a major content or backlink campaign impacting client market share.
