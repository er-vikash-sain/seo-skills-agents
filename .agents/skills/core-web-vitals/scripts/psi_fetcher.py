#!/usr/bin/env python3
"""
Google PageSpeed Insights Telemetry Fetcher.
Calls the official free PSI API to retrieve Core Web Vitals metrics (LCP, CLS, INP, FCP, TTFB).
"""

import sys
import json
import urllib.request
import urllib.parse

PSI_ENDPOINT = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"

def fetch_cwv_metrics(url, strategy="mobile"):
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
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Target URL required"}))
        sys.exit(1)
    
    target_url = sys.argv[1]
    strategy = sys.argv[2] if len(sys.argv) > 2 else "mobile"
    result = fetch_cwv_metrics(target_url, strategy)
    print(json.dumps(result, indent=2))
