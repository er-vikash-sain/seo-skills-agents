---
name: ai-prompt-research
description: Researches conversational prompt query patterns, extracts conversational intent structures, and identifies AI answer engine query variations across package tiers.
---

# Instructions

## Role
Conducts research on conversational queries, prompt phrasing, and conversational search patterns used by users in ChatGPT, Perplexity, and Gemini.

## Inputs
- `client_package_tier`: Plan 1 (Not included), Plan 2 (Standard prompt research), Plan 3 (Deep multi-engine prompt research).
- Brand niche, target products, and service keywords.

## Procedure
1. Identify common conversational prompt templates (e.g., "What is the best X for Y?", "Compare A vs B").
2. Extract prompt intent categories (evaluation, recommendation, troubleshooting).
3. **Tier Variation:**
   - **Plan 1:** Skipped.
   - **Plan 2:** Research 25 primary conversational prompt patterns.
   - **Plan 3:** Research 75+ prompt variations across all target buyer personas.
4. Output AI Prompt Research Matrix.

## Output & Evidence
- **File:** `artifacts/ai_prompt_research_matrix.md`
- **Status Note:** Writes prompt count to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if brand niche lacks sufficient conversational search volume.
