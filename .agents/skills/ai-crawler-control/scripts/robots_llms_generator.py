#!/usr/bin/env python3
"""
Robots.txt & LLMs.txt AI Crawler Access Policy Generator & Validator.
Generates standard robots.txt directives for AI web crawlers (GPTBot, ClaudeBot, PerplexityBot, Bytespider, CCBot).
"""

import sys
import json

DEFAULT_AI_CRAWLERS = [
    "GPTBot",
    "ClaudeBot",
    "PerplexityBot",
    "Bytespider",
    "CCBot",
    "Google-Extended"
]

def generate_robots_policy(policy="allow_all", disallowed_crawlers=None):
    if disallowed_crawlers is None:
        disallowed_crawlers = []

    lines = ["# AI Crawler Access Policy - Search Everywhere OS", ""]
    
    if policy == "allow_all":
        lines.append("User-agent: *")
        lines.append("Allow: /")
        lines.append("")
        for crawler in DEFAULT_AI_CRAWLERS:
            lines.append(f"User-agent: {crawler}")
            if crawler in disallowed_crawlers:
                lines.append("Disallow: /")
            else:
                lines.append("Allow: /")
            lines.append("")
    elif policy == "block_ai_training":
        lines.append("# Blocking AI Training Bots")
        for crawler in DEFAULT_AI_CRAWLERS:
            lines.append(f"User-agent: {crawler}")
            lines.append("Disallow: /")
            lines.append("")

    return "\n".join(lines)

if __name__ == "__main__":
    policy_type = sys.argv[1] if len(sys.argv) > 1 else "allow_all"
    output_policy = generate_robots_policy(policy_type)
    print(output_policy)
