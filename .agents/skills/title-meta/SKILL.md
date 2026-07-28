---
name: title-meta
description: Constructs CTR-optimized page Title tags and Meta descriptions adhering to character length constraints and target keyword specs based on package tier.
version: "1.0.0"
---

# Instructions

## Role
Generates and formats page Title tags (50-60 characters) and Meta Descriptions (145-155 characters) for maximum click-through rates.

## Inputs
- `client_package_tier`: Plan 1 (Key pages), Plan 2 (All core pages), Plan 3 (All site & product pages).
- Target page URLs, target keywords, and brand name constraints.

## Procedure
1. Extract existing title and meta description tags from target pages.
2. Format new title tag: `[Primary Keyword] - [Secondary Keyword / Benefit] | [Brand Name]`.
3. Format meta description with compelling call-to-action (CTA) and primary keyword inclusion.
4. **Tier Variation:**
   - **Plan 1:** Generate metadata for top 5 key pages.
   - **Plan 2:** Generate metadata for all main site pages.
   - **Plan 3:** Generate metadata for all site pages plus product catalog pages.
5. Save metadata proposal table for approval.

## Output & Evidence
- **File:** `artifacts/title_meta_proposals.md`
- **Status Note:** Logs generated title/meta counts to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if brand guidelines prohibit standard CTA phrases or keyword formats.
