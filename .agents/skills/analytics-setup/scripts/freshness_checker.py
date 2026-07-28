#!/usr/bin/env python3
"""
Telemetry Freshness & Cache Expiration Checker.
Enforces 30-day and 90-day expiration windows on cached SERP, GSC, and audit telemetry files to prevent stale data.
"""

import os
import sys
import json
import time

def check_file_freshness(filepath, max_age_days=90):
    if not os.path.exists(filepath):
        return {"file": filepath, "status": "Missing", "fresh": False}

    file_mtime = os.path.getmtime(filepath)
    current_time = time.time()
    age_days = (current_time - file_mtime) / (60 * 60 * 24)

    is_fresh = age_days <= max_age_days
    return {
        "filepath": filepath,
        "age_days": round(age_days, 1),
        "max_allowed_days": max_age_days,
        "is_fresh": is_fresh,
        "status": "Fresh" if is_fresh else "Stale (Requires Re-Crawl)"
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Filepath required as argument"}))
        sys.exit(1)

    path = sys.argv[1]
    max_days = int(sys.argv[2]) if len(sys.argv) > 2 else 90
    result = check_file_freshness(path, max_days)
    print(json.dumps(result, indent=2))
