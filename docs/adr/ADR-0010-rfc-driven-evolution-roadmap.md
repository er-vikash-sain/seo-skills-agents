# ADR-0010: RFC-Driven Architecture Evolution Strategy

- **Status:** Accepted
- **Date:** 2026-07-28
- **Context:** Framework evolution must proceed systematically without breaking existing skill/agent contracts.
- **Decision:** Adopt an RFC-driven specification process (`docs/rfc/`) where all structural changes must be proposed via RFC documents and pass scorecard regression testing before acceptance.
- **Consequences:** Protects architectural integrity, prevents ad-hoc design creep, provides clear evolutionary milestones.
