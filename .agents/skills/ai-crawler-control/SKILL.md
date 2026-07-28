---
name: ai-crawler-control
description: Generates and updates robots.txt rules, llms.txt files, and AI crawler access policies (GPTBot, ClaudeBot, PerplexityBot) by package tier.
version: "1.0.0"
---

# Instructions

## Role
Constructs and validates `robots.txt` AI crawler directive blocks and `llms.txt` markdown manifests for AI search bots (GPTBot, ClaudeBot, PerplexityBot, Bytespider, CCBot).

## Inputs
- `client_package_tier`: Plan 1 (Not included), Plan 2 (Basic AI bot directives), Plan 3 (Full AI crawler control + custom `llms.txt` manifest).
- Client access policy choices (Allow/Block per AI bot).

## Procedure
1. Inspect current `robots.txt` configuration for AI user-agent directives.
2. Format allow/deny rules for `GPTBot`, `ClaudeBot`, `PerplexityBot`, and `Google-Extended`.
3. **Tier Variation:**
   - **Plan 1:** Skipped.
   - **Plan 2:** Configure standard AI bot access directives in `robots.txt`.
   - **Plan 3:** Complete AI Crawler Control (`robots.txt` directives + structured `llms.txt` site content manifest).
4. Output proposed `robots.txt` block and `llms.txt` file.

## Output & Evidence
- **File:** `artifacts/ai_crawler_control_proposal.md`
- **Status Note:** Logs AI bot permission status to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator before modifying live site `robots.txt` or root server files.
