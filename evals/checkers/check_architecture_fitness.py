#!/usr/bin/env python3
"""
Architecture Fitness Function Checker for Search Everywhere AI OS.
Enforces structural architecture compliance without external dependencies:
1. Every agent folder MUST contain agent.md with frontmatter.
2. Every skill folder MUST contain SKILL.md with frontmatter.
3. Every skill MUST be indexed in docs/CAPABILITY_REGISTRY.md.
"""

import os
import sys

WORKSPACE_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AGENTS_DIR = os.path.join(WORKSPACE_ROOT, ".agents", "agents")
SKILLS_DIR = os.path.join(WORKSPACE_ROOT, ".agents", "skills")
CAPABILITY_REGISTRY_PATH = os.path.join(WORKSPACE_ROOT, "docs", "CAPABILITY_REGISTRY.md")

def check_architecture_fitness():
    errors = []

    # Check 1: Agent files
    if os.path.exists(AGENTS_DIR):
        agent_folders = [f for f in os.listdir(AGENTS_DIR) if os.path.isdir(os.path.join(AGENTS_DIR, f))]
        for folder in agent_folders:
            agent_file = os.path.join(AGENTS_DIR, folder, "agent.md")
            if not os.path.exists(agent_file):
                errors.append(f"Agent folder '{folder}' missing 'agent.md'")
            else:
                with open(agent_file, "r") as f:
                    content = f.read()
                    if not content.startswith("---"):
                        errors.append(f"Agent '{folder}/agent.md' missing YAML frontmatter header")

    # Check 2: Skill files & Capability Registry Index
    registry_content = ""
    if os.path.exists(CAPABILITY_REGISTRY_PATH):
        with open(CAPABILITY_REGISTRY_PATH, "r") as f:
            registry_content = f.read()
    else:
        errors.append("docs/CAPABILITY_REGISTRY.md missing")

    if os.path.exists(SKILLS_DIR):
        skill_folders = [f for f in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, f))]
        for folder in skill_folders:
            skill_file = os.path.join(SKILLS_DIR, folder, "SKILL.md")
            if not os.path.exists(skill_file):
                errors.append(f"Skill folder '{folder}' missing 'SKILL.md'")
            else:
                with open(skill_file, "r") as f:
                    content = f.read()
                    if not content.startswith("---"):
                        errors.append(f"Skill '{folder}/SKILL.md' missing YAML frontmatter header")
            
            # Verify skill is registered in CAPABILITY_REGISTRY.md
            if folder not in registry_content:
                errors.append(f"Skill '{folder}' is missing from docs/CAPABILITY_REGISTRY.md")

    if errors:
        print(f"❌ ARCHITECTURE FITNESS CHECK FAILED ({len(errors)} errors):")
        for err in errors:
            print(f"  - {err}")
        return False
    
    print("✓ Architecture Fitness Function: 100% PASS (All Agents, Skills & Registry Indexes Verified)")
    return True

if __name__ == "__main__":
    success = check_architecture_fitness()
    sys.exit(0 if success else 1)
