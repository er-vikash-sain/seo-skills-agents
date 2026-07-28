#!/usr/bin/env python3
"""
MCP (Model Context Protocol) Endpoint & OpenAPI Action Auditor.
Audits web properties for machine-executable APIs, OpenAPI schemas, and agent action capabilities.
Supports argparse, --help, --dry-run, and strict URL scheme validation.
"""

import sys
import json
import argparse
import urllib.request

def audit_mcp_endpoints(domain_url, dry_run=False):
    if dry_run:
        return {
            "domain": domain_url,
            "mode": "dry-run",
            "agentic_action_readiness_score": 100,
            "discovered_endpoints": [f"{domain_url.rstrip('/')}/.well-known/mcp.json"],
            "mcp_support_detected": True,
            "status": "Success"
        }

    # Strict URL Scheme Validation
    if not (domain_url.startswith("http://") or domain_url.startswith("https://")):
        return {
            "domain": domain_url,
            "error": "Invalid URL scheme: Must start with http:// or https:// (e.g., https://acmecyber.com)",
            "status": "Failed"
        }

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
        "status": "Success" if len(found_endpoints) > 0 else "Failed"
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audit domain for MCP and OpenAPI endpoints.")
    parser.add_argument("domain", help="Target domain URL (must start with http:// or https://)")
    parser.add_argument("--dry-run", action="store_true", help="Run offline without network HTTP calls")
    args = parser.parse_args()

    result = audit_mcp_endpoints(args.domain, dry_run=args.dry_run)
    print(json.dumps(result, indent=2))
    if result.get("status") == "Failed":
        sys.exit(1)
    sys.exit(0)
