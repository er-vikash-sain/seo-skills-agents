#!/usr/bin/env python3
"""
Hindi & Vernacular Keyword Mapping Utility.
Maps technical English terms to standard Devanagari script loanwords and regional search intent variations.
"""

import sys
import json

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
        devanagari = TECHNICAL_TERM_MAPPINGS.get(kw_clean, f"{kw_clean} (हिंदी रूपांतरण)")
        results.append({
            "english_keyword": kw_clean,
            "devanagari_loanword": devanagari,
            "search_intent": "Informational / Commercial",
            "regional_target": "IN-HI (India Hindi Search Market)"
        })

    return {
        "mapped_count": len(results),
        "keyword_mappings": results
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Provide comma-separated English keywords as argument"}))
        sys.exit(1)

    raw_keywords = sys.argv[1].split(",")
    result = map_vernacular_keywords(raw_keywords)
    print(json.dumps(result, indent=2))
