# TARGET OPERATING MODEL (TOM) — SEARCH EVERYWHERE AI OS

**Scope:** Enterprise Operational Operating Model (People, Process, Technology, Governance, Support)

---

## 👥 1. PEOPLE & ROLES
- **Lead Agency Operator (Human-in-the-Loop):** Sovereign approval authority. Reviews client drafts, authorizes live updates, signs off on monthly reports.
- **Lead Orchestrator Agent (`AGENTS.md`):** System state manager, multi-agent delegator, state lock merger.
- **Reasoning Subagents (6 Roles):** Specialist strategy, validation, writing, and GEO analysis contexts.

---

## 🔄 2. PROCESS LIFECYCLE
1. **Client Onboarding:** Capture business context $\rightarrow$ Generate canonical `client_data_house.json`.
2. **Monthly Planning:** Temporal rollover check $\rightarrow$ Tier-scoped roadmap $\rightarrow$ Task execution packages (`task_spec.json`).
3. **Autonomous Execution:** Worker agent/skill executes task $\rightarrow$ Output written to `task_artifacts/`.
4. **Verification Gate:** `validator` subagent runs `run_scorecard.py` & `check_provenance.py`.
5. **Human Sign-Off:** Verified artifacts routed to Human Approval Queue for authorization.
6. **Reporting & Archival:** Monthly report compiled $\rightarrow$ State archived to `archive/{year}/{month}/`.

---

## ⚙️ 3. TECHNOLOGY STACK
- **Orchestration Layer:** Google Antigravity Agent Engine.
- **Model Layer:** Gemini 2.5 Pro (Frontier reasoning) + Multi-engine GEO testing.
- **Evaluation Layer:** Python 3 deterministic AST & string checkers (`evals/checkers/`).
- **Data Storage Layer:** Local file-system workspace (`client_data/`, `artifacts/`).

---

## 🛡️ 4. GOVERNANCE & COMPLIANCE
- **Review-Driven Autonomy:** Zero autonomous publishing.
- **State Lock Rules:** Worker isolation + Lead Orchestrator merge mutex.
- **Ground-or-Abstain:** Mandatory empirical citations (`[Source: <path>]`).
