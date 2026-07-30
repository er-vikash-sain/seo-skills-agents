---
name: answer-optimization
description: Formats concise answer blocks, featured snippet targets, and voice search Q&A sections formatted for direct AI extraction based on package tier.
version: "1.0.0"
---

# Instructions

## Role
Formats direct answer blocks (40-50 words), Passage Citability Blocks (134–167 words with high entity-attribution density), Featured Snippet listicles/tables, and voice search Q&A sections designed for Google AI Overviews, ChatGPT, Perplexity, and Gemini AIO extraction.

## Inputs
- `client_package_tier`: Plan 1 (Not included), Plan 2 (Answer-block optimization & featured snippet targeting), Plan 3 (Answer-block + passage citability + featured snippets + voice search Q&A).
- Target question queries, draft copy, and entity definitions.

## Procedure
1. Extract high-intent questions from content briefs.
2. Format direct answer paragraphs (40-50 words for featured snippets) or Passage Citability Blocks (134–167 words with self-contained entity resolution and high citation density for AI search engines) immediately beneath target H2/H3 question headings.
3. **Tier Variation:**
   - **Plan 1:** Skipped.
   - **Plan 2:** Format 3-5 answer blocks per article for Featured Snippets & AI Overviews.
   - **Plan 3:** Complete Answer-Block + Passage Citability + Featured Snippet + Voice Search Q&A optimization across all articles.
4. Save Answer-Block proposals.

## Output & Evidence
- **File:** `artifacts/answer_blocks_proposals.md`
- **Status Note:** Writes formatted answer block count to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if answer block content lacks direct factual resolution.
