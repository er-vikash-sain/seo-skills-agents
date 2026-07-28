---
name: shopping-feed
description: Configures, formats, and enriches Google Shopping XML/JSON feed attributes, handles product mapping, and verifies feed diagnostics by package tier.
version: "1.0.0"
---

# Instructions

## Role
Generates, formats, and validates Google Shopping Data Feeds (Google Merchant Center feed format).

## Inputs
- `client_package_tier`: Plan 1 (Not included), Plan 2 (Basic Shopping feed setup), Plan 3 (95%+ enriched Shopping feed with custom attributes).
- Product catalog data (ID, Title, Description, Link, Image_Link, Price, Availability, GTIN/MPN, Brand, Google_Product_Category).

## Procedure
1. Validate required fields (`id`, `title`, `description`, `price`, `availability`, `link`, `image_link`).
2. Format XML/TSV payload conforming to Google Merchant Center specifications.
3. **Tier Variation:**
   - **Plan 1:** Skipped.
   - **Plan 2:** Basic Shopping feed configuration for product catalog.
   - **Plan 3:** 95%+ enriched Shopping feed with optimized titles, GTINs, product highlights, and custom labels.
4. Save Shopping Feed payload.

## Output & Evidence
- **File:** `artifacts/google_shopping_feed.xml`
- **Status Note:** Writes validated product feed item count to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if Merchant Center rejects feed items due to policy or price mismatch.
