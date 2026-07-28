# ADR-0006: Transition Strategy from Prose Skills to Typed Code Tools

- **Status:** Accepted
- **Date:** 2026-07-28
- **Context:** High-frequency procedural skills suffer latency and token inflation when defined purely as prose instructions.
- **Decision:** Maintain Markdown `SKILL.md` specifications for domain definition, but provide strongly-typed Python scripts in `scripts/` for deterministic execution.
- **Consequences:** Lowers token usage, speeds execution, guarantees type safety across runtime platforms.
