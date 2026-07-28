---
name: ai-citation-tracking
description: Tracks brand citation rates, recommendation frequencies, and URL sources across ChatGPT, Perplexity, Gemini, and Google AIO by package tier.
---

# Instructions

## Role
Performs mechanical tracking of brand citation rates, inclusion percentages, and URL referral sources in AI engine responses.

## Inputs
- `client_package_tier`: Plan 1 (Not included), Plan 2 (AI citation-rate tracking - 20 prompts), Plan 3 (AI citation-rate tracking - 50+ prompts & trend logging).
- Target prompt set and brand entity keywords.

## Procedure
1. Execute prompt queries across target AI search engines.
2. Measure citation-rate percentage: `(Prompts citing brand / Total prompts tested) * 100`.
3. **Tier Variation:**
   - **Plan 1:** Skipped.
   - **Plan 2:** Track citation rate across 20 core prompts bi-weekly.
   - **Plan 3:** Track citation rate across 50+ prompts weekly with engine attribution trends.
4. Output AI Citation Tracking Log.

## Output & Evidence
- **File:** `artifacts/ai_citation_tracking_log.csv`
- **Status Note:** Writes overall AI citation rate percentage to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if brand citation rate drops by >15% across major AI engines.
