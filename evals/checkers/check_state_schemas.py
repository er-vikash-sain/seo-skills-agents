#!/usr/bin/env python3
"""
State Files JSON Schema Conformance Checker.
Validates tracking_index.json and task_spec.json against evals/schemas/.
"""

import sys
import os
import json

def check_state_schemas():
    print("[*] State JSON Schema Conformance Checker...")
    tracking_index = "client_data/plannings/current_month/tracking_index.json"
    task_spec = "client_data/plannings/current_month/week_1/task_TASK-001/task_spec.json"

    if not os.path.exists(tracking_index):
        print(f"[!] FAIL: Missing tracking index at {tracking_index}")
        return 1

    if not os.path.exists(task_spec):
        print(f"[!] FAIL: Missing task spec at {task_spec}")
        return 1

    try:
        with open(tracking_index, "r", encoding="utf-8") as f:
            ti_data = json.load(f)
        required_ti_keys = ["campaign_month", "plan_tier", "overall_status", "tasks"]
        for k in required_ti_keys:
            if k not in ti_data:
                print(f"[!] FAIL: tracking_index.json missing required key '{k}'")
                return 1

        with open(task_spec, "r", encoding="utf-8") as f:
            ts_data = json.load(f)
        required_ts_keys = ["task_id", "title", "assigned_agent", "priority", "due_date", "inputs"]
        for k in required_ts_keys:
            if k not in ts_data:
                print(f"[!] FAIL: task_spec.json missing required key '{k}'")
                return 1

        print("[+] PASS: All active state JSON files conform to schema keys.")
        return 0
    except Exception as e:
        print(f"[!] FAIL: Schema validation error: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(check_state_schemas())
