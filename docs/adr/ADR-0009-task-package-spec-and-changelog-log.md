# ADR-0009: Dedicated Task Package Specification and Changelog Architecture

- **Status:** Accepted
- **Date:** 2026-07-28
- **Context:** Task tracking requires granular traceability regarding inputs, execution attempts, retry counts, and outputs.
- **Decision:** Execute every task inside a dedicated folder (`client_data/plannings/current_month/week_{w}/task_{task_id}/`) containing `task_spec.json`, `task_changelog.md`, and `task_artifacts/`.
- **Consequences:** Enables complete task auditability, explicit input path scoping, and deterministic failure recovery.
