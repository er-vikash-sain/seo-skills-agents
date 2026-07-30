# CORE-EEAT Content Quality Benchmark Checklist (80-Item Matrix)

Comprehensive 80-item audit framework for evaluating Experience, Expertise, Authoritativeness, Trustworthiness, GEO/AEO answer readiness, and structural content integrity.

## 1. Experience & First-Hand Proof (15 Items)
- [ ] **EX-01:** Includes first-person observational or practical insights ("In our testing...", "When we configured...").
- [ ] **EX-02:** Details real-world edge cases or troubleshooting scenarios.
- [ ] **EX-03:** Includes original visual evidence, architecture diagrams, or data tables (no generic stock descriptions).
- [ ] **EX-04:** Demonstrates actual usage timeframe (e.g., "Tested over 30 days").
- [ ] **EX-05:** Compares practical effort vs theoretical claims.
- [ ] **EX-06:** Specifies physical or environmental testing parameters.
- [ ] **EX-07:** Highlights un-documented product behaviors discovered during hands-on use.
- [ ] **EX-08:** Mentions specific setup or installation prerequisites encountered.
- [ ] **EX-09:** Documents failure points or error messages encountered during testing.
- [ ] **EX-10:** Quantifies performance under stress or peak load.
- [ ] **EX-11:** Provides step-by-step reproduction steps for key workflows.
- [ ] **EX-12:** Clarifies target user experience level (Beginner vs Senior Engineer).
- [ ] **EX-13:** Includes real-time logs or output snippets where applicable.
- [ ] **EX-14:** Contrasts current release behavior against legacy versions.
- [ ] **EX-15:** Summarizes key lessons learned from implementation.

## 2. Expertise & Subject Authority (15 Items)
- [ ] **EP-01:** Uses precise industry terminology accurately without definition fluff.
- [ ] **EP-02:** Cites primary technical documentation, RFCs, or official API specifications.
- [ ] **EP-03:** Author credentials or expert review team explicitly stated.
- [ ] **EP-04:** Explains underlying mechanics (*why* it works) rather than surface instructions (*how*).
- [ ] **EP-05:** Distinguishes between recommended best practices and antipatterns.
- [ ] **EP-06:** References relevant compliance standards (GDPR, SOC2, ISO, HIPAA).
- [ ] **EP-07:** Provides clear mathematical formulas or logic models where relevant.
- [ ] **EP-08:** Correctly differentiates adjacent technologies (e.g. REST vs gRPC vs GraphQL).
- [ ] **EP-09:** Explains architectural trade-offs (Latency vs Throughput, Consistency vs Availability).
- [ ] **EP-10:** Identifies security risks or vulnerability vectors.
- [ ] **EP-11:** Includes code or query snippets that adhere to modern syntax standards.
- [ ] **EP-12:** References official benchmarks or peer-reviewed studies.
- [ ] **EP-13:** Avoids factual oversimplifications that lead to technical errors.
- [ ] **EP-14:** Outlines scalability bounds and memory/CPU resource requirements.
- [ ] **EP-15:** Incorporates expert quotes or verified industry commentary.

## 3. Authoritativeness & Entity Linking (15 Items)
- [ ] **AT-01:** Mentions canonical Wikidata / Knowledge Graph entities.
- [ ] **AT-02:** Links outbound to high-authority primary sources `[Source: URL/Path]`.
- [ ] **AT-03:** Includes contextual internal links to related pillar and cluster URLs.
- [ ] **AT-04:** Demonstrates topical depth across the entire Hub-and-Spoke cluster.
- [ ] **AT-05:** References recognized industry leaders, standards bodies, or frameworks.
- [ ] **AT-06:** Uses consistent entity naming across all page headings and body text.
- [ ] **AT-07:** Implements Schema.org JSON-LD (Article, Organization, FAQ, HowTo).
- [ ] **AT-08:** Avoids orphan content; clearly positioned within site taxonomy.
- [ ] **AT-09:** Cites verified industry reports or statistical research datasets.
- [ ] **AT-10:** Includes exact product version numbers and release tags.
- [ ] **AT-11:** Corresponds to verified search intent (Informational, Commercial, Transactional).
- [ ] **AT-12:** Displays clear publication and last-updated timestamps.
- [ ] **AT-13:** Contains structured citation footnotes or reference sections.
- [ ] **AT-14:** Connects to author bio pages with external verification links (`sameAs`).
- [ ] **AT-15:** Maintains consistent brand voice across all cluster documents.

## 4. Trustworthiness & Transparency (15 Items)
- [ ] **TR-01:** Includes clear affiliate/commercial disclosure where applicable.
- [ ] **TR-02:** Discloses potential conflicts of interest or vendor relationships.
- [ ] **TR-03:** States honest product limitations or non-supported use cases.
- [ ] **TR-04:** Displays transparent pricing, licensing fees, or hidden costs.
- [ ] **TR-05:** Provides accessible contact information or support channels.
- [ ] **TR-06:** Privacy policy and terms of service links accessible.
- [ ] **TR-07:** Zero AI slop words ("pivotal role", "testament to", "evolving landscape").
- [ ] **TR-08:** Zero exaggerated claims ("best in the world", "unbeatable").
- [ ] **TR-09:** Factual claims backed by empirical data files or telemetry logs.
- [ ] **TR-10:** Neutral, objective tone maintained across comparison matrices.
- [ ] **TR-11:** Grammatically correct text free of mechanical translation artifacts.
- [ ] **TR-12:** Clear editorial review process documented.
- [ ] **TR-13:** Secure HTTPS links used exclusively.
- [ ] **TR-14:** Correct handling of user data privacy and consent disclaimers.
- [ ] **TR-15:** Transparent revision history or change log available.

## 5. AEO & GEO Answer Readiness (10 Items)
- [ ] **AG-01:** Executive summary answer block (40-50 words) under main H1/H2.
- [ ] **AG-02:** Direct answer block under every H2/H3 question sub-heading.
- [ ] **AG-03:** Structured Markdown comparison tables for multi-entity queries.
- [ ] **AG-04:** Bulleted Key Takeaways summary for featured snippet extraction.
- [ ] **AG-05:** Clean Devanagari loanwords used for Indian vernacular content.
- [ ] **AG-06:** Entity properties formatted as key-value pairs for LLM extraction.
- [ ] **AG-07:** Clear definition blocks for primary terms ("X is a Y that Z").
- [ ] **AG-08:** High citation-density prose suitable for ChatGPT / Perplexity quotes.
- [ ] **AG-09:** Voice Search friendly Q&A formatting.
- [ ] **AG-10:** Schema `FAQPage` or `SpeakableSpecification` integration.

## 6. Technical Content Integrity (10 Items)
- [ ] **TC-01:** Single `<h1>` tag per document.
- [ ] **TC-02:** Logical heading hierarchy (`H1 -> H2 -> H3` with no skipped levels).
- [ ] **TC-03:** Title tag within 50-60 character limits with primary keyword.
- [ ] **TC-04:** Meta description within 140-160 character limits with CTA.
- [ ] **TC-05:** All images have descriptive `alt` attributes.
- [ ] **TC-06:** Target keyword density maintained at 1-2% without stuffing.
- [ ] **TC-07:** Anchor text is descriptive and contextual (no "click here").
- [ ] **TC-08:** Fast load time optimization (LCP assets prioritized).
- [ ] **TC-09:** Mobile-responsive layout and tap targets formatted.
- [ ] **TC-10:** 0 Broken links or redirect chains.

---

## AUDIT VERDICT MATRIX

| EEAT Score | AI Slop Score | Provenance Status | Verdict | Action Required |
|---|---|---|---|---|
| ≥ 85% | 0 Matches | 100% Grounded | `SHIP` | Route to Human Approval Queue |
| 60-84% | > 0 Matches | Minor Gaps | `FIX` | Trigger Rework Loop to Writer Subagent |
| < 60% | Severe Slop | Unsourced Claims | `BLOCK` | Reject Draft & Flag Escalation |
