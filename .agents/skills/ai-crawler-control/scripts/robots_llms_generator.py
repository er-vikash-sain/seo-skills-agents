#!/usr/bin/env python3
"""
Robots.txt & LLMs.txt AI Crawler Access Policy Generator & Validator.
Generates standard robots.txt directives for AI web crawlers (GPTBot, ClaudeBot, PerplexityBot).
Validates policy input and exits non-zero on invalid policy strings.
"""

import sys
import json
import argparse

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

    if policy not in ["allow_all", "block_ai_training"]:
        return None

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
    parser = argparse.ArgumentParser(description="Generate AI Crawler robots.txt and llms.txt policies.")
    parser.add_argument("policy", choices=["allow_all", "block_ai_training"], help="Target AI crawler policy")
    args = parser.parse_args()

    output_policy = generate_robots_policy(args.policy)
    if output_policy is None:
        print(json.dumps({"error": f"Invalid policy '{args.policy}'. Must be 'allow_all' or 'block_ai_training'"}))
        sys.exit(1)

    print(output_policy)
    sys.exit(0)
