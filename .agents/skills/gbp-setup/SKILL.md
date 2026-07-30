---
name: gbp-setup
description: Audits, structures, and optimizes Google Business Profile (GBP) listing parameters, category selection, business details, and cover settings by package tier.
version: "1.0.0"
---

# Instructions

## Role
Performs setup, auditing, Local Maps Geo-Grid rank monitoring, and optimization of Google Business Profile (GBP) listing data (Business Name, Primary Category, Secondary Categories, Business Hours, Address, NAP parameters, Cover/Photo assets, and Google Map Pack ranking strategy).

## Inputs
- `client_package_tier`: Plan 1 (Not included), Plan 2 (GBP setup & basic optimization), Plan 3 (GBP setup + full multi-category, service area, & Geo-Grid map pack optimization).
- Raw business NAP details, category inputs, geo-coordinates, and service photos.

## Procedure
1. Audit GBP profile completeness, primary/secondary category alignment, and NAP consistency.
2. Configure Local Maps Geo-Grid monitoring parameters (radius, grid density) to track Map Pack rankings.
3. **Tier Variation:**
   - **Plan 1:** Skipped.
   - **Plan 2:** Standard GBP profile audit, primary category setup, and description optimization.
   - **Plan 3:** Complete GBP optimization including secondary categories, service area mapping, Local Geo-Grid audit, and photo metadata optimization.
4. Save GBP optimization specification.

## Output & Evidence
- **File:** `artifacts/gbp_setup_spec.md`
- **Status Note:** Logs GBP setup completion score to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if GBP listing is suspended, unverified, or requires postcard verification.
