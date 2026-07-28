---
description: Automated bi-weekly & monthly performance outcome report compilation workflow.
---

// Build Report Slash Workflow (/build-report)

1. Read active client details from `client_data/project_details/project.md`.
2. Gather sprint task completion artifacts from `client_data/plannings/current_month/week_*/task_*/task_artifacts/`.
3. Invoke `report-builder` skill to aggregate GSC, GA4, and ranking telemetry.
4. Format output into `client_data/reports/{year}/{month}/performance_report.md`.
5. Execute `python3 evals/checkers/check_provenance.py` on generated report to ensure 100% grounded provenance.
6. Present verified report in Human Approval Queue.
