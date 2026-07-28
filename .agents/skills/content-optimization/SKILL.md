---
name: content-optimization
description: Performs on-page SEO optimization passes on English content drafts, verifies keyword density, heading distribution, and internal link insertions by package tier.
version: "1.0.0"
---

# Instructions

## Role
Executes procedural on-page SEO optimization passes over content drafts written by `english-writer`, checking keyword placements, readability scores, and semantic density.

## Inputs
- `client_package_tier`: Plan 1 (2 English blogs/mo pass), Plan 2 (2 English blogs/mo pass + advanced formatting), Plan 3 (3 English blogs/mo pass + full cluster interlinking).
- Draft text from `english-writer` and target keyword brief.

## Procedure
1. Check primary keyword inclusion in H1, first 100 words, and meta title.
2. Verify secondary LSI keyword distribution and entity density.
3. **Tier Variation:**
   - **Plan 1:** Basic on-page pass for 2 English blogs/month.
   - **Plan 2:** Advanced on-page pass for 2 English blogs/month with schema & snippet formatting.
   - **Plan 3:** Complete optimization pass for 3 English blogs/month with cluster interlinking & E-E-A-T score verification.
4. Output optimized content draft proposal.

## Output & Evidence
- **File:** `artifacts/optimized_content_draft.md`
- **Status Note:** Writes optimization score and keyword density metrics to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if draft requires major restructuring or lacks required subject expertise.
