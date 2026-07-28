# ADR-0004: Empirical Provenance and Zero-Hallucination Gate

- **Status:** Accepted
- **Date:** 2026-07-28
- **Context:** LLMs suffer from hallucination risks when drafting performance telemetry and ranking reports.
- **Decision:** Mandate explicit empirical source file citations (`[Source: <path>]`) for all performance metrics. Validate provenance deterministically via `evals/checkers/check_provenance.py`.
- **Consequences:** Guarantees 100% factual accuracy and zero unbacked metric assertions in client reports.
