#!/usr/bin/env python3
"""
Offline JSON-LD Schema Markup Validator.
Extracts and validates JSON-LD schemas from raw JSON strings or HTML documents.
"""

import sys
import json
import re
import argparse

REQUIRED_SCHEMA_TYPES = ["Organization", "Product", "FAQPage", "Article", "HowTo", "LocalBusiness"]

def extract_json_ld(content):
    if "<script" in content and "application/ld+json" in content:
        match = re.search(r'<script[^>]*type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1).strip()
    return content

def validate_schema_json(raw_content):
    json_str = extract_json_ld(raw_content)
    try:
        data = json.loads(json_str)
    except Exception as e:
        return {"valid": False, "error": f"Invalid JSON syntax: {str(e)}"}

    context = data.get("@context", "")
    schema_type = data.get("@type", "")

    if "schema.org" not in str(context):
        return {"valid": False, "error": "Missing or invalid @context header (expected 'https://schema.org')"}

    if not schema_type:
        return {"valid": False, "error": "Missing required '@type' property"}

    errors = []
    if schema_type == "Organization":
        if "name" not in data or "url" not in data:
            errors.append("Organization schema requires 'name' and 'url'")
    elif schema_type == "Product":
        if "name" not in data or ("offers" not in data and "offers" not in str(data)):
            errors.append("Product schema requires 'name' and 'offers'")
    elif schema_type == "FAQPage":
        if "mainEntity" not in data:
            errors.append("FAQPage schema requires 'mainEntity' question array")

    if errors:
        return {"valid": False, "schema_type": schema_type, "errors": errors}

    return {"valid": True, "schema_type": schema_type, "message": "Schema JSON-LD is valid"}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate JSON-LD Schema syntax and structure.")
    parser.add_argument("target", help="JSON string, JSON filepath, or HTML filepath")
    args = parser.parse_args()

    target = args.target
    if target.endswith(".json") or target.endswith(".html"):
        try:
            with open(target, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(json.dumps({"valid": False, "error": f"Could not read file: {str(e)}"}))
            sys.exit(1)
    else:
        content = target

    result = validate_schema_json(content)
    print(json.dumps(result, indent=2))
    if not result.get("valid", False):
        sys.exit(1)
    sys.exit(0)
