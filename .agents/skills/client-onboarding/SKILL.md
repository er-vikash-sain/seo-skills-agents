---
name: client-onboarding
description: Conducts interactive client onboarding, collects business details, social links, purchased package tier, and initializes the client data house and tracking directories.
version: "1.0.0"
---

# Instructions

## Role
Performs client onboarding data collection, structures the canonical `client_data_house.json`, initializes `project.md`, and sets up the client directory workspace.

## Inputs
- Interactive onboarding responses:
  - `website_name` & `domain_url`
  - `brand_logo_url`
  - `business_address`, `phone`, `whatsapp`, `email`
  - `social_links` (Facebook, Instagram, LinkedIn, X, YouTube)
  - `purchased_plan_tier` (Plan 1 / Plan 2 / Plan 3)
  - `contract_duration_months`
  - `existing_assets_summary` (GSC, GA4, GBP status)
  - `client_special_instructions` (Initial issues/requests)

## Procedure
1. Create client data directory structure:
   - `client_data/project_details/`
   - `client_data/client_feedback/`
   - `client_data/plannings/current_month/`
   - `client_data/plannings/archive/`
   - `client_data/reports/`
2. Populate `client_data/project_details/client_data_house.json` and `client_data/project_details/project.md`.
3. Initialize `client_data/client_feedback/client_issues_log.md` with initial client requests.
4. Initialize `client_data/plannings/current_month/tracking_index.json`.

## Output & Evidence
- **File:** `client_data/project_details/project.md` & `client_data_house.json`
- **Status Note:** Logs onboarding completion to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if target domain is unreachable or contract tier is unmapped.
