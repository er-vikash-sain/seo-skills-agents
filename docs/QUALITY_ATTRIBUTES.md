# ENTERPRISE QUALITY ATTRIBUTES & NON-FUNCTIONAL REQUIREMENTS (NFR)

**Scope:** Operational Quantitative SLA/SLO/SLI Metrics for Search Everywhere AI OS

---

## 📊 1. RELIABILITY & PROVENANCE SLA
- **Metric Citation Accuracy (SLO):** 100% of reported ranking figures, traffic numbers, and conversion data MUST cite empirical workspace files (`[Source: <path>]`). Zero hallucinated metrics permitted.
- **Evaluation Gate:** Verified by `evals/checkers/check_provenance.py`. Failures cause automatic task rejection.
- **Rework Circuit Breaker:** Tasks failing validation $\ge 3$ times auto-escalate to human operator with `STUCK_REWORK_CAP_EXCEEDED` status.

---

## ⚡ 2. PERFORMANCE & LATENCY SLO
- **Procedural Skill Execution SLA:** $< 30$ seconds per skill invocation.
- **Subagent Strategic Reasoning SLA:** $< 120$ seconds per subagent reasoning turn.
- **Full Monthly Planning Cycle SLA:** $< 300$ seconds total workflow runtime.

---

## 💰 3. COST & TOKEN EFFICIENCY SLO
- **Monthly Roadmap Token Budget:** $< 50,000$ context tokens for full monthly task planning cycle.
- **Context Read Limit:** Maximum 500 lines per file read instruction to prevent token bloating and context rot.

---

## 🛡️ 4. SECURITY & COMPLIANCE SLO
- **Secret Scanner SLA:** Zero API keys, passwords, or PII exposed in generated artifacts (Verified by `output_scanner.json`).
- **Command Denylist SLA:** 100% blocking of destructive shell commands (`rm -rf /`, `mkfs`, raw curl pipes) (Verified by `before_tool_command.json`).
- **Human Authorization SLA:** 100% of live CMS, DNS, or GBP mutations MUST receive explicit human approval before release.

---

## 🛠️ 5. MAINTAINABILITY & TESTABILITY SLO
- **Scorecard Pass Rate:** 100% PASS rate required on `evals/run_scorecard.py` before any codebase changes are committed to Git.
- **Documentation Alignment:** 100% of registered agents and skills MUST be indexed in `docs/planning-core.md` and `docs/CAPABILITY_REGISTRY.md`.
