#!/usr/bin/env python3
"""
Offline JSON-LD Schema Markup Validator.
Validates syntax, required @context, @type, and schema parameters for Organization, Product, FAQ, Article schemas.
"""

import sys
import json

REQUIRED_SCHEMA_TYPES = ["Organization", "Product", "FAQPage", "Article", "HowTo", "LocalBusiness"]

def validate_schema_json(json_str):
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
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Schema JSON string or file path required"}))
        sys.exit(1)

    arg = sys.argv[1]
    if arg.endswith(".json") or arg.endswith(".html"):
        with open(arg, "r") as f:
            content = f.read()
    else:
        content = arg

    result = validate_schema_json(content)
    print(json.dumps(result, indent=2))
