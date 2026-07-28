#!/usr/bin/env python3
"""
Telemetry Freshness & Cache Expiration Checker.
Enforces 30-day and 90-day expiration windows on cached SERP, GSC, and audit telemetry files.
Supports argparse, --help, and non-zero exit code on stale/missing data.
"""

import os
import sys
import json
import time
import argparse

def check_file_freshness(filepath, max_age_days=90, dry_run=False):
    if dry_run:
        return {
            "filepath": filepath,
            "mode": "dry-run",
            "age_days": 1.0,
            "max_allowed_days": max_age_days,
            "is_fresh": True,
            "status": "Fresh"
        }

    if not os.path.exists(filepath):
        return {"filepath": filepath, "status": "Missing", "is_fresh": False}

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
    parser = argparse.ArgumentParser(description="Check telemetry cache file freshness and expiration.")
    parser.add_argument("filepath", help="Path to telemetry cache file")
    parser.add_argument("--max-age-days", type=int, default=90, help="Maximum allowed age in days (default: 90)")
    parser.add_argument("--dry-run", action="store_true", help="Run offline dry-run test")
    args = parser.parse_args()

    result = check_file_freshness(args.filepath, max_age_days=args.max_age_days, dry_run=args.dry_run)
    print(json.dumps(result, indent=2))
    if not result.get("is_fresh", False):
        sys.exit(1)
    sys.exit(0)
