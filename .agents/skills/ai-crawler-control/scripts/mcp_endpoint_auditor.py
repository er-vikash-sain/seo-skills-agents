#!/usr/bin/env python3
"""
MCP (Model Context Protocol) Endpoint & OpenAPI Action Auditor.
Audits web properties for machine-executable APIs, OpenAPI schemas, and agent action capabilities.
"""

import sys
import json
import urllib.request

def audit_mcp_endpoints(domain_url):
    domain = domain_url.rstrip("/")
    mcp_endpoints = [
        f"{domain}/.well-known/mcp.json",
        f"{domain}/openapi.json",
        f"{domain}/api-docs"
    ]

    found_endpoints = []
    for ep in mcp_endpoints:
        try:
            req = urllib.request.Request(ep, headers={"User-Agent": "MCP-Endpoint-Auditor/1.0"})
            with urllib.request.urlopen(req, timeout=5) as resp:
                if resp.getcode() == 200:
                    found_endpoints.append(ep)
        except Exception:
            pass

    score = 100 if len(found_endpoints) > 0 else 50
    return {
        "domain": domain_url,
        "agentic_action_readiness_score": score,
        "discovered_endpoints": found_endpoints,
        "mcp_support_detected": len(found_endpoints) > 0,
        "recommendation": "Expose /.well-known/mcp.json or /openapi.json to enable autonomous AI agent transactions."
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Target domain URL required"}))
        sys.exit(1)

    url = sys.argv[1]
    result = audit_mcp_endpoints(url)
    print(json.dumps(result, indent=2))
