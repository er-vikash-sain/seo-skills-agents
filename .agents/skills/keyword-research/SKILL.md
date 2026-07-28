---
name: keyword-research
description: Performs mechanical keyword data extraction, keyword expansion, search volume aggregation, and LSI keyword grouping to support the keyword-strategist subagent.
version: "1.0.0"
---

# Instructions

## Role
Executes mechanical keyword data harvesting, pulls search metrics, groups keywords by search intent, and aggregates keyword lists to support `keyword-strategist`.

## Inputs
- `client_package_tier`: Plan 1 (Baseline keyword research), Plan 2 (Expanded keyword research), Plan 3 (Full multi-intent keyword universe).
- Seed keywords, target domain, and geographic location.

## Procedure
1. Aggregate search metrics (search volume, keyword difficulty, CPC, intent classification).
2. Expand seed list with long-tail phrases and LSI entity terms.
3. **Tier Variation:**
   - **Plan 1 (Baseline):** Harvest top 50 primary keywords.
   - **Plan 2 (Expanded):** Harvest 200+ keywords grouped by basic intent.
   - **Plan 3 (Full):** Complete keyword universe (500+ terms) mapped across customer journey stages.
4. Output structured keyword database for `keyword-strategist` analysis.

## Output & Evidence
- **File:** `artifacts/keyword_research_data.csv`
- **Status Note:** Logs harvested keyword counts to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if API limits prevent keyword volume extraction.
