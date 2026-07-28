---
name: local-citations
description: Formats, audits, and builds NAP (Name, Address, Phone) consistency matrices for local directory submissions across package tiers.
version: "1.0.0"
---

# Instructions

## Role
Performs mechanical NAP consistency audits and formats submission payloads for high-authority local business directories.

## Inputs
- `client_package_tier`: Plan 1 (Not included), Plan 2 (50 local citations / NAP format), Plan 3 (100 local citations / NAP format).
- Canonical NAP parameters (Name, Address, Phone, Website URL, Business Category).

## Procedure
1. Verify canonical NAP details against client brand guidelines.
2. Format directory submission payloads conforming to target directory specs.
3. **Tier Variation:**
   - **Plan 1:** Skipped.
   - **Plan 2:** Audit and format submission list for 50 local citations.
   - **Plan 3:** Audit and format submission list for 100 high-authority local citations.
4. Output Local Citations Submission Matrix.

## Output & Evidence
- **File:** `artifacts/local_citations_matrix.md`
- **Status Note:** Logs formatted citation target count to `artifacts/task_status.json`.

## Escalation
- Escalate to human operator if conflicting NAP information exists across active live directories.
