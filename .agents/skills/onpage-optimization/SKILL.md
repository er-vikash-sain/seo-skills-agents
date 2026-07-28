---
name: onpage-optimization
description: Audits and applies on-page structural optimizations, handles noindex tag removal, heading tag alignment, and page-level HTML updates adapted by package tier.
version: "1.0.0"
---

# Instructions

## Role
Performs mechanical on-page auditing, removes unwanted `noindex`/`nofollow` directives, aligns HTML heading structures (H1-H6), and optimizes text formatting.

## Inputs
- `client_package_tier`: Plan 1 (Key pages only), Plan 2 (All primary pages), Plan 3 (All pages + Product & Category pages).
- Target page URLs and target keyword specs.

## Procedure
1. Scan target page HTML for accidental `noindex` or `nofollow` meta tags and remove them.
2. Check single H1 tag presence and ensure logical H2/H3 heading hierarchy.
3. **Tier Variation:**
   - **Plan 1:** Optimize top 5 key landing pages.
   - **Plan 2:** Optimize all core site pages and service sections.
   - **Plan 3:** Full site-wide on-page optimization including e-commerce product pages.
4. Generate proposed page HTML modifications for human review.

## Output & Evidence
- **File:** `artifacts/onpage_optimization_proposals.md`
- **Status Note:** Writes list of optimized pages and removed noindex directives to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator before applying any code/HTML change to live CMS environments.
