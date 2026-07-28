---
name: schema-generator
description: Generates and validates strongly-typed Schema.org JSON-LD markup supporting Organization, Product, FAQ, HowTo, and Article schemas across package tiers.
version: "1.0.0"
---

# Instructions

## Role
Generates syntactically valid JSON-LD structured data for Schema.org types (`Organization`, `Product`, `FAQPage`, `HowTo`, `Article`, `BreadcrumbList`).

## Inputs
- `client_package_tier`: Plan 1 (Organization & basic Product), Plan 2 (Organization, Product, FAQ, HowTo), Plan 3 (Full multi-schema graph + custom SameAs).
- `schema_mode`: `organization`, `product`, `faq_howto`, `article`.
- Entity attributes, product details, FAQ items, or business info.

## Procedure
1. Extract target entity parameters from input payload.
2. Select schema template according to `schema_mode`.
3. **Tier Variation:**
   - **Plan 1:** Generate `Organization` schema and basic `Product` schema.
   - **Plan 2:** Generate `Organization`, `Product` (4 products), `FAQPage`, and `HowTo` schemas.
   - **Plan 3:** Complete multi-schema graph linking `Organization`, `Product`, `Article`, `FAQPage`, and `sameAs` entity nodes.
4. Validate generated JSON-LD syntax against Schema.org standards.
5. Save JSON-LD snippets for human approval.

## Output & Evidence
- **File:** `artifacts/schema_markup_proposals.json`
- **Status Note:** Logs generated schema types and validation status to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if JSON-LD validation fails or required entity properties are missing.
