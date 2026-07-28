---
name: review-requests
description: Formats Google Business review request templates, email/SMS outreach copy, and customer feedback workflows based on package tier.
version: "1.0.0"
---

# Instructions

## Role
Formats customer review request templates (Email, SMS, WhatsApp) and direct Google review link campaigns to build GBP review velocity.

## Inputs
- `client_package_tier`: Plan 1 (Not included), Plan 2 (Standard review request workflow), Plan 3 (Automated multi-channel review request copy).
- Direct GBP review link and brand name.

## Procedure
1. Insert direct GBP review shortlink into review request copy.
2. Format review request templates tailored for customer post-purchase/service touchpoints.
3. **Tier Variation:**
   - **Plan 1:** Skipped.
   - **Plan 2:** Format 2 standard email/SMS review request templates.
   - **Plan 3:** Format 4 multi-channel review request templates + follow-up review sequence.
4. Output Review Requests Copy Template document.

## Output & Evidence
- **File:** `artifacts/review_requests_templates.md`
- **Status Note:** Writes template count to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if review shortlink is invalid or GBP listing is not verified.
