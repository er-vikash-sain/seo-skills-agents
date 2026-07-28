#!/usr/bin/env python3
"""
Auto-Generates docs/CAPABILITY_REGISTRY.md directly from .agents/skills/*/SKILL.md frontmatter metadata.
Enforces 100% automated Single Source of Truth for Enterprise Capability Architecture.
"""

import os
import sys
import glob

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKILLS_DIR = os.path.join(WORKSPACE_ROOT, ".agents", "skills")
OUTPUT_REGISTRY_PATH = os.path.join(WORKSPACE_ROOT, "docs", "CAPABILITY_REGISTRY.md")

def parse_skill_metadata(skill_md_path):
    name = ""
    description = ""
    version = "1.0.0"
    with open(skill_md_path, "r") as f:
        lines = f.readlines()
        in_header = False
        for line in lines:
            if line.strip() == "---":
                if not in_header:
                    in_header = True
                else:
                    break
                continue
            if in_header:
                if line.startswith("name:"):
                    name = line.split(":", 1)[1].strip()
                elif line.startswith("description:"):
                    description = line.split(":", 1)[1].strip()
                elif line.startswith("version:"):
                    version = line.split(":", 1)[1].strip().strip('"').strip("'")
    return name, description, version

def generate_registry():
    skill_files = glob.glob(os.path.join(SKILLS_DIR, "*", "SKILL.md"))
    skill_files.sort()

    content = []
    content.append("# ENTERPRISE BUSINESS CAPABILITY REGISTRY & TRACEABILITY MATRIX")
    content.append("\n**Status:** Auto-Generated Single Source of Truth (SSOT)")
    content.append("**Generator:** `evals/checkers/generate_capability_registry.py`\n")
    content.append("---")
    content.append("\n## 🏛️ AUTOMATED CAPABILITY REGISTRY TABLE\n")
    content.append("| Skill Slug | Version | Description | Assigned Agent | Primary Acceptance Gate |")
    content.append("|---|---|---|---|---|")

    for sf in skill_files:
        name, desc, ver = parse_skill_metadata(sf)
        if not name:
            name = os.path.basename(os.path.dirname(sf))
        
        assigned_agent = "orchestrator"
        if name in ["keyword-research", "ai-prompt-research"]:
            assigned_agent = "keyword-strategist"
        elif name in ["content-optimization"]:
            assigned_agent = "english-writer"
        elif name in ["answer-optimization", "entity-markup", "ai-visibility-audit"]:
            assigned_agent = "entity-geo"

        gate = "Deterministic Gate / Scorecard"
        if "schema" in name:
            gate = "check_schema.py"
        elif "title" in name or "meta" in name or "onpage" in name:
            gate = "check_title_meta.py"
        elif "link" in name:
            gate = "check_internal_links.py"
        elif "provenance" in name or "report" in name:
            gate = "check_provenance.py"
        elif "crawler" in name:
            gate = "check_ai_crawler_control.py"
        elif "onboarding" in name:
            gate = "client_data_house.json SSOT"

        content.append(f"| `{name}` | `v{ver}` | {desc} | `{assigned_agent}` | `{gate}` |")

    content.append("\n---\n")
    content.append("## 🔒 ARCHITECTURE GOVERNANCE LAW")
    content.append("This registry is automatically generated and verified by `evals/run_scorecard.py`.")
    content.append("Every skill MUST have a valid `SKILL.md` file with name, version, and description metadata.")

    with open(OUTPUT_REGISTRY_PATH, "w") as f:
        f.write("\n".join(content) + "\n")
    
    print(f"✓ Successfully auto-generated docs/CAPABILITY_REGISTRY.md ({len(skill_files)} skills registered)")
    return True

if __name__ == "__main__":
    generate_registry()
