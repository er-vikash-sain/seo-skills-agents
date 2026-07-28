---
description: Interactive client onboarding workflow to collect business details and set up client_data house architecture.
---

// 1. Prompt user for interactive onboarding details
1. Ask user for:
   - Business Name & Domain URL
   - Logo URL
   - Business Address, Phone, WhatsApp, Email
   - Social Profile Links (FB, LinkedIn, X, IG, YT)
   - Purchased Package Tier (Plan 1 / Plan 2 / Plan 3)
   - Contract Duration & Start Date
   - Initial Client Issues or Focus Points

// 2. Execute Onboarding Skill
2. Invoke `.agents/skills/client-onboarding/SKILL.md` with gathered parameters.

// 3. Initialize Client Workspace Architecture
3. Populate:
   - `client_data/project_details/project.md`
   - `client_data/project_details/client_data_house.json`
   - `client_data/client_feedback/client_issues_log.md`
   - `client_data/plannings/current_month/tracking_index.json`

4. Log onboarding completion status note.
