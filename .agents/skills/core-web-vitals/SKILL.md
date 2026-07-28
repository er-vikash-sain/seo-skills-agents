---
name: core-web-vitals
description: Analyzes PageSpeed Insights and Lighthouse telemetry, profiles LCP, INP, and CLS performance metrics, and generates asset optimization recommendations by package tier.
version: "1.0.0"
---

# Instructions

## Role
Profiles Core Web Vitals (CWV) metrics, identifies slow LCP assets, high INP script latency, and CLS layout shifts.

## Inputs
- `client_package_tier`: Plan 1 (Baseline monitoring), Plan 2 (To Green - core pages), Plan 3 (To Green - site-wide & mobile optimization).
- Lighthouse telemetry and PageSpeed API scores.

## Procedure
1. Pull mobile and desktop Lighthouse performance scores for target pages.
2. Identify LCP image bottlenecks, unminified CSS/JS resources, and render-blocking scripts.
3. Measure Cumulative Layout Shift (CLS) causes (missing image dimensions, web font swaps).
4. **Tier Variation:**
   - **Plan 1 (Baseline):** Audit baseline PSI scores and report top 3 performance bottlenecks.
   - **Plan 2 (To Green - Core):** Provide code fix proposals to achieve >90 green PSI scores on core pages.
   - **Plan 3 (To Green - Full):** Provide full site-wide asset optimization, font preloading, and JS deferment specs.
5. Generate CWV remediation specification document.

## Output & Evidence
- **File:** `artifacts/core_web_vitals_report.md`
- **Status Note:** Writes LCP, INP, and CLS scores to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if performance bottlenecks require backend server hosting upgrades or CDN implementation.
