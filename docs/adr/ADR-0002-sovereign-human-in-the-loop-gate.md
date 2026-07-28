# ADR-0002: Sovereign Human-in-the-Loop Gate for Live Mutations

- **Status:** Accepted
- **Date:** 2026-07-28
- **Context:** System operates against live client web properties, CMS platforms, and search console engines.
- **Decision:** Enforce a zero-autonomous publishing policy. All generated reports, CMS updates, DNS changes, and GBP posts MUST land in the Human Approval Queue for explicit sign-off before release.
- **Consequences:** Eliminates legal liability, prevents rogue publishing, protects client web properties.
