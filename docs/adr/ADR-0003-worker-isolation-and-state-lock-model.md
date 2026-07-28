# ADR-0003: Worker Isolation and State Lock Model

- **Status:** Accepted
- **Date:** 2026-07-28
- **Context:** Concurrent multi-agent execution risks corrupting shared state tracking files (`tracking_index.json`).
- **Decision:** Worker subagents write output strictly to isolated task result files (`task_artifacts/`). ONLY the Lead Orchestrator agent is authorized to merge state into central tracking indexes.
- **Consequences:** Eliminates race conditions and file lock collisions across multi-agent executions.
