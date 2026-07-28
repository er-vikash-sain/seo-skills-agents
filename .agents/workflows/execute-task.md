---
description: Automated task execution, validation gate, and changelog update workflow.
---

// 1. Read Task Package Spec
1. Prompt for `task_id` or select highest priority pending task from `tracking_index.json`.
2. Read `client_data/plannings/current_month/week_{w}/task_{task_id}/task_spec.json`.

// 2. Worker Execution
3. Invoke assigned subagent / skill with input parameters from `task_spec.json`.
4. Worker writes output to `task_artifacts/task_{task_id}_output.md`.

// 3. Quality & Provenance Validation Gate
5. Invoke `validator` subagent and run `python3 evals/checkers/check_provenance.py`.
6. If validation fails:
   - Update `task_changelog.md` with failure log & increment retry count.
   - Route rework to worker.
7. If validation passes:
   - Update `task_changelog.md` status to `Validated`.
   - Update `tracking_index.json` master task status.
   - Route to Human Approval Queue if client-facing.
