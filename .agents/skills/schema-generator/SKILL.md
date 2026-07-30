---
name: schema-generator
description: Generates and validates strongly-typed Schema.org JSON-LD markup supporting Organization, Product, FAQ, HowTo, and Article schemas across package tiers.
version: "1.0.0"
---

# Instructions

## Role
Generates syntactically valid JSON-LD structured data for modern Schema.org types (`Organization`, `Article`, `Product`, `LocalBusiness`, `Service`, `SoftwareApplication`, `BreadcrumbList`). Reflects 2026 Google Search standards prioritizing structured entity graphs (note: Google retired FAQPage and HowTo rich result displays; retain schema for non-Google/internal semantic graphs only).

## Inputs
- `client_package_tier`: Plan 1 (Organization & basic Product), Plan 2 (Organization, Product, LocalBusiness, Service), Plan 3 (Full multi-schema graph + custom SameAs Wikidata nodes).
- `schema_mode`: `organization`, `product`, `service`, `article`, `local_business`.
- Entity attributes, product details, service specs, or business info.

## Procedure
1. Extract target entity parameters from input payload.
2. Select schema template according to `schema_mode`.
3. **Tier Variation:**
   - **Plan 1:** Generate `Organization` schema and basic `Product` schema.
   - **Plan 2:** Generate `Organization`, `Product` (4 products), `LocalBusiness`, and `Service` schemas.
   - **Plan 3:** Complete multi-schema graph linking `Organization`, `Product`, `Article`, `Service`, and `sameAs` Wikidata entity nodes.
4. Validate generated JSON-LD syntax against Schema.org standards.
5. Save JSON-LD snippets for human approval.

## Output & Evidence
- **File:** `artifacts/schema_markup_proposals.json`
- **Status Note:** Logs generated schema types and validation status to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if JSON-LD validation fails or required entity properties are missing.
