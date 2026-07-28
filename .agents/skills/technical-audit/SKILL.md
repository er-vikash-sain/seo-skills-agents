---
name: technical-audit
description: Conducts comprehensive technical SEO crawls, indexability diagnostics, JS rendering audits, redirect chain checks, and crawl budget analysis adapted by client package tier.
---

# Instructions

## Role
Executes procedural technical site audits, identifies indexability bottlenecks, detects 404/redirect errors, and inspects JavaScript rendering performance.

## Inputs
- `client_package_tier`: Plan 1 (Standard crawl), Plan 2 (Deep crawl), Plan 3 (Deep crawl + Advanced JS rendering & log analysis).
- `target_domain`: Domain URL to audit.

## Procedure
1. Inspect site crawlability, `robots.txt`, and XML sitemap health.
2. Scan for status code errors (4xx, 5xx), redirect loops, and canonical tag misconfigurations.
3. Check mobile responsiveness and DOM structure.
4. **Tier Variation:**
   - **Plan 1 (Baseline):** Audit top 100 key pages; basic crawlability & status checks.
   - **Plan 2 (Expanded):** Audit entire site architecture; crawl budget & canonical checks.
   - **Plan 3 (Full):** Complete site audit + Advanced JS rendering inspection & server log crawl behavior.
5. Generate technical audit findings document and actionable remediation checklist.

## Output & Evidence
- **File:** `artifacts/technical_audit_report.md`
- **Status Note:** Writes entry to `artifacts/task_status.json` with audit metrics and detected error counts.

## Escalation
- Escalate to human operator if server returns 503 Service Unavailable during crawl or if critical `robots.txt` disallow blocks entire site.
