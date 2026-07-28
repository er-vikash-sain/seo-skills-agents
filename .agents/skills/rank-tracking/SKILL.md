---
name: rank-tracking
description: Executes keyword rank tracking data pulls, tracks SERP positions (20, 50, or unlimited terms), and measures rank volatility by package tier.
version: "1.0.0"
---

# Instructions

## Role
Performs mechanical keyword ranking data collection, calculates rank position shifts, and aggregates search position history across SERPs.

## Inputs
- `client_package_tier`: Plan 1 (20 terms), Plan 2 (50 terms), Plan 3 (Unlimited / Full keyword universe tracking).
- Target keyword list and domain URL.

## Procedure
1. Pull search engine rank position data for configured target keywords.
2. Calculate position deltas (gain/loss), top 3/10/30 visibility ratios, and SERP feature presence.
3. **Tier Variation:**
   - **Plan 1:** Track 20 primary keywords monthly.
   - **Plan 2:** Track 50 target keywords bi-weekly.
   - **Plan 3:** Track Unlimited / full keyword universe weekly with volatility alert logs.
4. Output Keyword Rank Tracking Log.

## Output & Evidence
- **File:** `artifacts/keyword_rank_tracking_log.csv`
- **Status Note:** Writes average rank position and tracked term count to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if rank tracking API returns errors or core terms drop >10 positions.
