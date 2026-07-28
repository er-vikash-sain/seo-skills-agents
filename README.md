# AI-First Agency Operating System for Search Everywhere Operations

An enterprise-grade, multi-agent AI Operating System designed to govern, orchestrate, and scale end-to-end **Search Everywhere Operations** — spanning Traditional SEO, Technical SEO, On-Page SEO, Off-Page SEO, Local SEO, Entity SEO, Answer Engine Optimization (AEO), Generative Engine Optimization (GEO), Content Operations, Website Audits, Strategic Planning, Autonomous Execution, Reporting, Knowledge Management, and Human-AI Collaboration.

---

## 🏛️ Architecture Overview

The system is built on a lean, modular architecture natively integrated into Google Antigravity:

```text
/
├── AGENTS.md                                   # Lead Orchestrator Governance & Guardrails
├── docs/                                       # RFC-000 FOUNDATION.md Constitution & Planning Core
├── .agents/
│   ├── CONVENTIONS.md                          # Paved-Road Standards & Data Integrity
│   ├── hooks/                                  # Lifecycle Hooks (Denylist, Output Scanner, Validator Gate)
│   ├── agents/                                 # 6 Reasoning Subagents (Planner, Validator, Writer, etc.)
│   └── skills/                                 # 26 Package-Aware Procedural Skills
├── client_data/                                # Per-Client Single Source of Truth & Task Packages
│   ├── project_details/                        # project.md & client_data_house.json (SSOT)
│   ├── client_feedback/                        # client_issues_log.md (Mid-month & initial requests)
│   ├── plannings/
│   │   ├── current_month/                      # tracking_index.json & task_{id}/ execution folders
│   │   └── archive/                            # Historical monthly plans ({year}/{month}/)
│   └── reports/                            # Archived verified outcome reports
└── evals/                                      # Evaluation Harness & Scorecard Suite
    ├── checkers/                               # Deterministic checkers (check_provenance.py, schema, etc.)
    ├── fixtures/                               # Sample pages, test client profiles & reports
    ├── integration/                            # End-to-End Tier-Scoping & Validator catch-rate tests
    └── run_scorecard.py                        # Scorecard Runner & Regression Gate Validator
```

---

## 🤖 Reasoning Subagents (`.agents/agents/`)

- **`orchestrator`** (`AGENTS.md`): Primary Lead Agent — Context assembly, task routing, state lock merging, and workflow orchestrating.
- **`planner`** (`.agents/agents/planner/agent.md`): Converts client service packages into weekly/daily roadmaps with dependencies.
- **`validator`** (`.agents/agents/validator/agent.md`): Quality gatekeeper — verifies task artifacts against empirical data files.
- **`keyword-strategist`** (`.agents/agents/keyword-strategist/agent.md`): Keyword research, intent mapping, topical clustering, and competitor gaps.
- **`english-writer`** (`.agents/agents/english-writer/agent.md`): High E-E-A-T English article drafting and landing page copy.
- **`hindi-writer`** (`.agents/agents/hindi-writer/agent.md`): Native Hindi & vernacular content localization for the Indian market.
- **`entity-geo`** (`.agents/agents/entity-geo/agent.md`): Knowledge graph positioning, answer-block shaping, and multi-engine GEO testing (ChatGPT, Gemini, Claude, Perplexity, AIO).

---

## 🛠️ Package-Aware Procedural Skills (`.agents/skills/`)

26 procedural skills that adapt dynamically across **Plan 1 (Baseline)**, **Plan 2 (Expanded)**, and **Plan 3 (Full)** tiers:

- **Setup & Technical:** `technical-audit`, `analytics-setup`, `onpage-optimization`, `title-meta`, `core-web-vitals`, `schema-generator`, `internal-linking`.
- **Product & E-Commerce:** `product-copy`, `shopping-feed`.
- **Content Operations:** `keyword-research`, `ai-prompt-research`, `content-calendar`, `content-optimization`, `answer-optimization`.
- **AI Search & Entity:** `ai-visibility-audit`, `entity-markup`, `ai-crawler-control`.
- **Local & Reputation:** `gbp-setup`, `gbp-posts`, `local-citations`, `review-requests`.
- **Reporting & Tracking:** `rank-tracking`, `ai-citation-tracking`, `competitor-benchmark`, `report-builder`, `client-onboarding`.

---

## 🛡️ Safety, Guardrails & Evaluation Harness

- **Review-Driven Autonomy:** Human-in-the-loop is mandatory for all live site mutations, CMS pushes, and publishing actions.
- **State Lock Boundary:** Subagents write ONLY to isolated task result files (`artifacts/task_<id>_result.md`). ONLY the `orchestrator` updates central index files.
- **Core Anti-Hallucination Gate:** `evals/checkers/check_provenance.py` requires every report metric to cite an empirical source file (`[Source: <path>]`).
- **Scorecard Runner:** Run `python3 evals/run_scorecard.py` to validate system integrity before committing framework updates.

---

## 🚀 Quick Start & Commands

```bash
# Run full evaluation scorecard & regression gate check
python3 evals/run_scorecard.py

# Test deterministic provenance checker on a report
python3 evals/checkers/check_provenance.py evals/fixtures/grounded_report.md

# Run integration test suite
python3 evals/integration/test_month_planning.py
```

---

## 📄 License & Authority

- **Supreme Governing Specification:** [docs/FOUNDATION.md](file:///Users/admin/Documents/temp/seo-skills-agents/docs/FOUNDATION.md) (RFC-000)
- **Lead Governance Rules:** [AGENTS.md](file:///Users/admin/Documents/temp/seo-skills-agents/AGENTS.md)
