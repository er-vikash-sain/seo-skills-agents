# ADR-0007: Decoupling Tenant Workspace Data from Core Framework Repository

- **Status:** Accepted
- **Date:** 2026-07-28
- **Context:** Storing active client instance data in the core framework repository violates multi-tenant isolation principles.
- **Decision:** Maintain `client_data/` strictly as a template hierarchy in the core repository, isolating active tenant project databases into independent workspace repositories.
- **Consequences:** Ensures clean framework reusability, eliminates Git push conflicts, enables enterprise tenant scaling.
