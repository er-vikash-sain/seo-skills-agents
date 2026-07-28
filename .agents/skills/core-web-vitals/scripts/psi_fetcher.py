#!/usr/bin/env python3
"""
Google PageSpeed Insights Telemetry Fetcher.
Calls official free PSI API to retrieve Core Web Vitals (LCP, CLS, INP).
Supports --dry-run / offline mode. Strict URL scheme validation.
"""

import sys
import json
import argparse
import urllib.request
import urllib.parse

PSI_ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

def fetch_cwv_metrics(url, strategy="mobile", dry_run=False):
    if dry_run:
        return {
            "url": url,
            "strategy": strategy,
            "mode": "dry-run",
            "performance_score": 92.0,
            "core_web_vitals": {
                "largest_contentful_paint": "1.8 s",
                "cumulative_layout_shift": "0.02",
                "interaction_to_next_paint": "120 ms",
                "first_contentful_paint": "0.9 s"
            },
            "status": "Success"
        }

    # Strict URL Scheme Validation
    if not (url.startswith("http://") or url.startswith("https://")):
        return {
            "url": url,
            "strategy": strategy,
            "error": "Invalid URL scheme: Must start with http:// or https:// (e.g., https://acmecyber.com)",
            "status": "Failed"
        }

    try:
        params = urllib.parse.urlencode({"url": url, "strategy": strategy})
        req_url = f"{PSI_ENDPOINT}?{params}"
        req = urllib.request.Request(req_url, headers={"User-Agent": "SEO-Agentic-PSI/1.0"})

        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))

        audits = data.get("lighthouseResult", {}).get("audits", {})
        lcp = audits.get("largest-contentful-paint", {}).get("displayValue", "N/A")
        cls = audits.get("cumulative-layout-shift", {}).get("displayValue", "N/A")
        inp = audits.get("interaction-to-next-paint", {}).get("displayValue", "N/A")
        fcp = audits.get("first-contentful-paint", {}).get("displayValue", "N/A")
        performance_score = data.get("lighthouseResult", {}).get("categories", {}).get("performance", {}).get("score", 0) * 100

        return {
            "url": url,
            "strategy": strategy,
            "performance_score": round(performance_score, 1),
            "core_web_vitals": {
                "largest_contentful_paint": lcp,
                "cumulative_layout_shift": cls,
                "interaction_to_next_paint": inp,
                "first_contentful_paint": fcp
            },
            "status": "Success"
        }
    except Exception as e:
        return {
            "url": url,
            "strategy": strategy,
            "error": str(e),
            "status": "Failed"
        }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch Core Web Vitals telemetry via Google PageSpeed Insights.")
    parser.add_argument("url", help="Target URL (must start with http:// or https://)")
    parser.add_argument("--strategy", choices=["mobile", "desktop"], default="mobile", help="Audit strategy")
    parser.add_argument("--dry-run", action="store_true", help="Run offline without network API calls")
    args = parser.parse_args()

    result = fetch_cwv_metrics(args.url, strategy=args.strategy, dry_run=args.dry_run)
    print(json.dumps(result, indent=2))
    if result.get("status") == "Failed":
        sys.exit(1)
    sys.exit(0)
