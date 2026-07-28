---
name: entity-markup
description: Generates and emits sameAs, Wikidata, and Knowledge Graph entity markup snippets to support the entity-geo subagent based on package tier.
version: "1.0.0"
---

# Instructions

## Role
Generates procedural `sameAs` entity link arrays, Wikidata references, and Knowledge Graph schema declarations supporting `entity-geo`.

## Inputs
- `client_package_tier`: Plan 1 (Not included), Plan 2 (Basic entity foundation markup), Plan 3 (Full entity graph markup + Wikidata link map).
- Entity mappings provided by `entity-geo` subagent.

## Procedure
1. Extract authoritative social, directory, and Wikidata URLs for target entity.
2. Build JSON-LD `sameAs` array and `knowsAbout` topic strings.
3. **Tier Variation:**
   - **Plan 1:** Skipped.
   - **Plan 2:** Generate basic `sameAs` markup array for core brand profiles.
   - **Plan 3:** Generate complete Knowledge Graph entity markup linking Wikipedia/Wikidata, social nodes, and executive author entities.
4. Output Entity Markup JSON-LD snippet.

## Output & Evidence
- **File:** `artifacts/entity_markup_snippet.json`
- **Status Note:** Writes entity link count to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if brand entity lacks verified external authoritative profiles.
