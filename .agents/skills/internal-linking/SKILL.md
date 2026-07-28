---
name: internal-linking
description: Audits internal linking structures, builds contextual anchor text placement maps, and optimizes PageRank distribution across site pages based on package tier.
---

# Instructions

## Role
Performs mechanical internal link audits, maps contextual anchor text opportunities between related articles/pages, and eliminates internal orphan pages.

## Inputs
- `client_package_tier`: Plan 1 (Not included), Plan 2 (Core page internal linking), Plan 3 (Site-wide PageRank sculpting & cluster interlinking).
- Site page URL index and target keyword mapping.

## Procedure
1. Scan page index for internal link counts, anchor text diversity, and orphan pages.
2. Match target pages with contextually relevant supporting blog posts/pages.
3. **Tier Variation:**
   - **Plan 1:** Skipped (or basic top-level navigation check).
   - **Plan 2:** Build internal link placement map for core landing pages and blog posts.
   - **Plan 3:** Complete PageRank sculpting map interlinking content clusters, category pages, and product pages.
4. Output internal link insertion table.

## Output & Evidence
- **File:** `artifacts/internal_linking_map.md`
- **Status Note:** Writes total internal link recommendations to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if target pages lack relevant context for natural anchor text insertion.
