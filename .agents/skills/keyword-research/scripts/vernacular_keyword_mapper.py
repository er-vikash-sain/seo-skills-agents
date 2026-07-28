#!/usr/bin/env python3
"""
Hindi & Vernacular Keyword Mapping Utility.
Maps technical English terms to standard Devanagari script loanwords.
Strictly returns 'unknown / needs-data' for unmapped terms to adhere to anti-hallucination policy.
"""

import sys
import json
import argparse

TECHNICAL_TERM_MAPPINGS = {
    "cloud security": "क्लाउड सिक्योरिटी",
    "cyber security": "साइबर सुरक्षा",
    "threat detection": "थ्रेट डिटेक्शन",
    "soc monitoring": "एसओसी मॉनिटरिंग",
    "search engine optimization": "सर्च इंजन ऑप्टिमाइजेशन",
    "artificial intelligence": "आर्टिफिशियल इंटेलिजेंस",
    "digital marketing": "डिजिटल मार्केटिंग"
}

def map_vernacular_keywords(english_keyword_list):
    results = []
    for kw in english_keyword_list:
        kw_clean = kw.strip().lower()
        devanagari = TECHNICAL_TERM_MAPPINGS.get(kw_clean, "unknown / needs-data")
        results.append({
            "english_keyword": kw_clean,
            "devanagari_loanword": devanagari,
            "search_intent": "Informational / Commercial" if devanagari != "unknown / needs-data" else "unknown / needs-data",
            "regional_target": "IN-HI (India Hindi Search Market)"
        })

    return {
        "mapped_count": len(results),
        "keyword_mappings": results
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Map English terms to Hindi Devanagari loanwords.")
    parser.add_argument("keywords", help="Comma-separated list of English keywords")
    args = parser.parse_args()

    raw_keywords = args.keywords.split(",")
    result = map_vernacular_keywords(raw_keywords)
    print(json.dumps(result, indent=2))
    sys.exit(0)
