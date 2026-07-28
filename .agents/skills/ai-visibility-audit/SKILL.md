---
name: ai-visibility-audit
description: Audits brand visibility across AI answer engines, measures baseline citation presence in ChatGPT, Perplexity, Gemini, and Google AIO by package tier.
version: "1.0.0"
---

# Instructions

## Role
Conducts baseline auditing of brand mention frequency, citation URLs, and entity presence across generative AI engines.

## Inputs
- `client_package_tier`: Plan 1 (Not included), Plan 2 (Baseline AI visibility audit), Plan 3 (Deep multi-engine AI visibility audit + sentiment check).
- Brand entity name, target queries, and key product names.

## Procedure
1. Query target brand queries across Perplexity, ChatGPT Search, Gemini, and Google AI Overviews.
2. Record citation URLs, brand sentiment, and inclusion/exclusion status.
3. **Tier Variation:**
   - **Plan 1:** Skipped.
   - **Plan 2:** Baseline audit across 15 target queries on ChatGPT & Perplexity.
   - **Plan 3:** Deep audit across 50 target queries on ChatGPT, Perplexity, Gemini, Claude, and Google AIO.
4. Generate AI Visibility Audit Report.

## Output & Evidence
- **File:** `artifacts/ai_visibility_baseline_audit.md`
- **Status Note:** Logs baseline citation percentage to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if brand entity is completely absent or flagged negatively by AI engines.
