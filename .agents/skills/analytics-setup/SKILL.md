---
name: analytics-setup
description: Configures Google Analytics 4 (GA4) property tracking, Google Search Console (GSC) verification, custom event mapping, and search telemetry pipelines based on package tier.
version: "1.0.0"
---

# Instructions

## Role
Performs mechanical verification, tag integration checks, and property configuration for Google Analytics 4 (GA4) and Google Search Console (GSC).

## Inputs
- `client_package_tier`: Plan 1 (Standard GA4 + GSC setup), Plan 2 (GA4 + GSC + Custom Event tracking), Plan 3 (GA4 + GSC + Custom Events + E-commerce tracking integration).
- `ga4_measurement_id` & `gsc_property_url`.

## Procedure
1. Verify Google Search Console site ownership and sitemap submission status.
2. Inspect GA4 measurement tag installation on target pages.
3. **Tier Variation:**
   - **Plan 1:** Basic GSC site verification & GA4 pageview tag validation.
   - **Plan 2:** Add custom event tracking for form submissions, CTA clicks, and phone leads.
   - **Plan 3:** Complete GA4 setup + E-commerce funnel conversion tracking & API data pipeline authorization.
4. Output setup verification status report.

## Output & Evidence
- **File:** `artifacts/analytics_setup_status.md`
- **Status Note:** Logs GSC indexing connection state and GA4 active stream ID to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if DNS TXT/HTML tag verification fails or OAuth access to Google Console/GA4 is missing.
