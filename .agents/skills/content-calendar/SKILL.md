---
name: content-calendar
description: Builds structured publishing schedules, assigns content deliverables to target release dates, and schedules editorial workflows based on package tier.
version: "1.0.0"
---

# Instructions

## Role
Generates mechanical content calendars, formats editorial timelines, and maps publication dates for English and Hindi content deliverables.

## Inputs
- `client_package_tier`: Plan 1 (Not included / basic schedule), Plan 2 (2 English blogs/mo schedule), Plan 3 (3 English + 1 Hindi blog/mo + product updates schedule).
- Content briefs and campaign milestone dates.

## Procedure
1. Calculate target publication cadence based on package tier specifications.
2. Assign publication dates, target keywords, writer roles, and review deadlines to each calendar entry.
3. **Tier Variation:**
   - **Plan 1:** Basic monthly execution schedule.
   - **Plan 2:** Bi-weekly publishing schedule (2 English blogs/mo + GBP updates).
   - **Plan 3:** Weekly publishing schedule (3 English blogs + 1 Hindi blog/mo + weekly GBP posts + product refreshes).
4. Save content calendar specification.

## Output & Evidence
- **File:** `artifacts/content_calendar_schedule.md`
- **Status Note:** Writes scheduled item counts to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if client approval timelines conflict with scheduled publishing dates.
