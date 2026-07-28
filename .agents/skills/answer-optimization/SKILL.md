---
name: answer-optimization
description: Formats concise answer blocks, featured snippet targets, and voice search Q&A sections formatted for direct AI extraction based on package tier.
---

# Instructions

## Role
Formats direct answer blocks (40-50 words), Featured Snippet listicles/tables, and voice search Q&A sections designed for Google AI Overviews and conversational AI engines.

## Inputs
- `client_package_tier`: Plan 1 (Not included), Plan 2 (Answer-block optimization & featured snippet targeting), Plan 3 (Answer-block + featured snippets + voice search Q&A).
- Target question queries, draft copy, and entity definitions.

## Procedure
1. Extract high-intent questions from content briefs.
2. Format direct, concise answer paragraph (40-50 words) immediately beneath the target H2/H3 question heading.
3. **Tier Variation:**
   - **Plan 1:** Skipped.
   - **Plan 2:** Format 3-5 answer blocks per article for Featured Snippets & AI Overviews.
   - **Plan 3:** Complete Answer-Block + Featured Snippet + Voice Search Q&A optimization across all articles.
4. Save Answer-Block proposals.

## Output & Evidence
- **File:** `artifacts/answer_blocks_proposals.md`
- **Status Note:** Writes formatted answer block count to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if answer block content lacks direct factual resolution.
