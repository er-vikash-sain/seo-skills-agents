---
name: product-copy
description: Formats and structures e-commerce product descriptions into AI-extractable, structured copy blocks tailored for e-commerce catalog pages across package tiers.
---

# Instructions

## Role
Formats product descriptions, feature bullet points, and specification tables into clean, structured HTML/Markdown that AI crawlers can extract seamlessly.

## Inputs
- `client_package_tier`: Plan 1 (Not included), Plan 2 (4 products AI-extractable copy), Plan 3 (4 products AI-extractable + ongoing product copy updates).
- Raw product specs, features, and target keywords.

## Procedure
1. Extract product attributes (SKU, brand, price, features, specifications, FAQs).
2. Format copy into clean structured blocks: Product Overview, Key Features (bulleted), Tech Specs (table), and AI Summary.
3. **Tier Variation:**
   - **Plan 1:** Skipped.
   - **Plan 2:** Format AI-extractable copy for 4 core products.
   - **Plan 3:** Format AI-extractable copy for 4 core products + ongoing catalog copy updates.
4. Save product copy proposals for approval.

## Output & Evidence
- **File:** `artifacts/product_copy_proposals.md`
- **Status Note:** Logs formatted product count to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if technical product specifications are inaccurate or unverified.
