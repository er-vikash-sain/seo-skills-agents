# ENTERPRISE BUSINESS CAPABILITY REGISTRY & TRACEABILITY MATRIX

**Status:** Auto-Generated Single Source of Truth (SSOT)
**Generator:** `evals/checkers/generate_capability_registry.py`

---

## 🏛️ AUTOMATED CAPABILITY REGISTRY TABLE

| Skill Slug | Version | Description | Assigned Agent | Primary Acceptance Gate |
|---|---|---|---|---|
| `ai-citation-tracking` | `v1.0.0` | Tracks brand citation rates, recommendation frequencies, and URL sources across ChatGPT, Perplexity, Gemini, and Google AIO by package tier. | `orchestrator` | `Deterministic Gate / Scorecard` |
| `ai-crawler-control` | `v1.0.0` | Generates and updates robots.txt rules, llms.txt files, and AI crawler access policies (GPTBot, ClaudeBot, PerplexityBot) by package tier. | `orchestrator` | `check_ai_crawler_control.py` |
| `ai-prompt-research` | `v1.0.0` | Researches conversational prompt query patterns, extracts conversational intent structures, and identifies AI answer engine query variations across package tiers. | `keyword-strategist` | `Deterministic Gate / Scorecard` |
| `ai-visibility-audit` | `v1.0.0` | Audits brand visibility across AI answer engines, measures baseline citation presence in ChatGPT, Perplexity, Gemini, and Google AIO by package tier. | `entity-geo` | `Deterministic Gate / Scorecard` |
| `analytics-setup` | `v1.0.0` | Configures Google Analytics 4 (GA4) property tracking, Google Search Console (GSC) verification, custom event mapping, and search telemetry pipelines based on package tier. | `orchestrator` | `Deterministic Gate / Scorecard` |
| `answer-optimization` | `v1.0.0` | Formats concise answer blocks, featured snippet targets, and voice search Q&A sections formatted for direct AI extraction based on package tier. | `entity-geo` | `Deterministic Gate / Scorecard` |
| `client-onboarding` | `v1.0.0` | Conducts interactive client onboarding, collects business details, social links, purchased package tier, and initializes the client data house and tracking directories. | `orchestrator` | `client_data_house.json SSOT` |
| `competitor-benchmark` | `v1.0.0` | Conducts quarterly competitor benchmarking, compares domain metrics, backlink velocity, and search market share based on package tier. | `orchestrator` | `Deterministic Gate / Scorecard` |
| `content-calendar` | `v1.0.0` | Builds structured publishing schedules, assigns content deliverables to target release dates, and schedules editorial workflows based on package tier. | `orchestrator` | `Deterministic Gate / Scorecard` |
| `content-optimization` | `v1.0.0` | Performs on-page SEO optimization passes on English content drafts, verifies keyword density, heading distribution, and internal link insertions by package tier. | `english-writer` | `Deterministic Gate / Scorecard` |
| `core-web-vitals` | `v1.0.0` | Analyzes PageSpeed Insights and Lighthouse telemetry, profiles LCP, INP, and CLS performance metrics, and generates asset optimization recommendations by package tier. | `orchestrator` | `Deterministic Gate / Scorecard` |
| `entity-markup` | `v1.0.0` | Generates and emits sameAs, Wikidata, and Knowledge Graph entity markup snippets to support the entity-geo subagent based on package tier. | `entity-geo` | `Deterministic Gate / Scorecard` |
| `gbp-posts` | `v1.0.0` | Generates local update posts, offer announcements, and product updates formatted for Google Business Profiles based on package tier publishing cadence. | `orchestrator` | `Deterministic Gate / Scorecard` |
| `gbp-setup` | `v1.0.0` | Audits, structures, and optimizes Google Business Profile (GBP) listing parameters, category selection, business details, and cover settings by package tier. | `orchestrator` | `Deterministic Gate / Scorecard` |
| `internal-linking` | `v1.0.0` | Audits internal linking structures, builds contextual anchor text placement maps, and optimizes PageRank distribution across site pages based on package tier. | `orchestrator` | `check_internal_links.py` |
| `keyword-research` | `v1.0.0` | Performs mechanical keyword data extraction, keyword expansion, search volume aggregation, and LSI keyword grouping to support the keyword-strategist subagent. | `keyword-strategist` | `Deterministic Gate / Scorecard` |
| `local-citations` | `v1.0.0` | Formats, audits, and builds NAP (Name, Address, Phone) consistency matrices for local directory submissions across package tiers. | `orchestrator` | `Deterministic Gate / Scorecard` |
| `onpage-optimization` | `v1.0.0` | Audits and applies on-page structural optimizations, handles noindex tag removal, heading tag alignment, and page-level HTML updates adapted by package tier. | `orchestrator` | `check_title_meta.py` |
| `product-copy` | `v1.0.0` | Formats and structures e-commerce product descriptions into AI-extractable, structured copy blocks tailored for e-commerce catalog pages across package tiers. | `orchestrator` | `Deterministic Gate / Scorecard` |
| `rank-tracking` | `v1.0.0` | Executes keyword rank tracking data pulls, tracks SERP positions (20, 50, or unlimited terms), and measures rank volatility by package tier. | `orchestrator` | `Deterministic Gate / Scorecard` |
| `report-builder` | `v1.0.0` | Compiles monthly outcome reports (1-page, 2-page, or full+trend format), aggregates performance telemetry, and prepares evidence-backed reporting documents by package tier. | `orchestrator` | `check_provenance.py` |
| `review-requests` | `v1.0.0` | Formats Google Business review request templates, email/SMS outreach copy, and customer feedback workflows based on package tier. | `orchestrator` | `Deterministic Gate / Scorecard` |
| `schema-generator` | `v1.0.0` | Generates and validates strongly-typed Schema.org JSON-LD markup supporting Organization, Product, FAQ, HowTo, and Article schemas across package tiers. | `orchestrator` | `check_schema.py` |
| `shopping-feed` | `v1.0.0` | Configures, formats, and enriches Google Shopping XML/JSON feed attributes, handles product mapping, and verifies feed diagnostics by package tier. | `orchestrator` | `Deterministic Gate / Scorecard` |
| `technical-audit` | `v1.0.0` | Conducts comprehensive technical SEO crawls, indexability diagnostics, JS rendering audits, redirect chain checks, and crawl budget analysis adapted by client package tier. | `orchestrator` | `Deterministic Gate / Scorecard` |
| `title-meta` | `v1.0.0` | Constructs CTR-optimized page Title tags and Meta descriptions adhering to character length constraints and target keyword specs based on package tier. | `orchestrator` | `check_title_meta.py` |

---

## 🔒 ARCHITECTURE GOVERNANCE LAW
This registry is automatically generated and verified by `evals/run_scorecard.py`.
Every skill MUST have a valid `SKILL.md` file with name, version, and description metadata.
