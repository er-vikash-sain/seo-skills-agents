---
description: Automated monthly roadmap planning workflow with temporal rollover, tier-scoping, and task package creation.
---

// 1. Perform Automated Month Rollover
1. Check if `client_data/plannings/current_month/tracking_index.json` has an existing completed month.
2. If previous month exists:
   - Move `client_data/plannings/current_month/*` to `client_data/plannings/archive/{year}/{month}/`.
   - Move completed reports to `client_data/reports/{year}/{month}/`.

// 2. Read Context & Active Issues
3. Read `client_data/project_details/client_data_house.json` and `client_data/client_feedback/client_issues_log.md`.

// 3. Invoke Planner Subagent
4. Invoke `.agents/agents/planner/agent.md` to generate tier-scoped roadmap incorporating active client issues.

// 4. Create Task Execution Packages
5. Create weekly task package folders under `client_data/plannings/current_month/week_{1..4}/task_{task_id}/`:
   - `task_spec.json` (Target URLs, keywords, due date)
   - `task_changelog.md` (Initial status: Pending, execution count: 0)
   - `task_artifacts/` (Output directory)

6. Generate central `client_data/plannings/current_month/tracking_index.json`.
