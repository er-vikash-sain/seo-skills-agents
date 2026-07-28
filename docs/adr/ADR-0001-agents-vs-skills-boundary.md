# ADR-0001: Agents vs. Skills Boundary Specification

- **Status:** Accepted
- **Date:** 2026-07-28
- **Context:** System requires strict isolation between complex LLM strategic reasoning and formulaic, mechanical task execution.
- **Decision:** Reasoning, planning, content writing, and quality audit contexts are assigned strictly to **Subagents** (`.agents/agents/`). Formulaic, repeatable, procedural procedures are assigned strictly to **Skills** (`.agents/skills/`).
- **Consequences:** Eliminates prompt bloat, lowers token costs, enforces Single Responsibility Principle across system roles.
