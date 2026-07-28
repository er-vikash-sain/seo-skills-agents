---
name: gbp-posts
description: Generates local update posts, offer announcements, and product updates formatted for Google Business Profiles based on package tier publishing cadence.
---

# Instructions

## Role
Drafts localized Google Business Profile (GBP) posts (Updates, Offers, Events) with strategic CTA buttons and local keyword inclusions.

## Inputs
- `client_package_tier`: Plan 1 (Not included), Plan 2 (2 GBP posts/month), Plan 3 (Weekly GBP posts - 4/month).
- Local campaign offers, updates, and target keywords.

## Procedure
1. Extract promotion/update details and target local service keywords.
2. Format post draft (150-300 words) with clear CTA (e.g., "Learn More", "Call Now", "Book").
3. **Tier Variation:**
   - **Plan 1:** Skipped.
   - **Plan 2:** Draft 2 GBP posts per month.
   - **Plan 3:** Draft weekly GBP posts (4 posts per month).
4. Output GBP post proposals for human review.

## Output & Evidence
- **File:** `artifacts/gbp_posts_proposals.md`
- **Status Note:** Writes GBP post draft counts to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator before publishing posts to live GBP listing.
