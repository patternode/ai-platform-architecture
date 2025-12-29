#!/usr/bin/env python3
"""
Script to create a consolidated spreadsheet of all architecture patterns.
"""

import csv
import re
from pathlib import Path

PATTERNS_ROOT = Path(r"D:\Work\BNZ\ai-platform-architecture\03-building-blocks\patterns")
OUTPUT_CSV = PATTERNS_ROOT / "patterns-consolidated.csv"

def extract_pattern_info(content):
    """Extract pattern information from markdown content."""
    info = {}

    # Extract pattern ID
    id_match = re.search(r'\*\*Pattern ID\*\*\s*\|\s*`?(PT-\d+)`?', content)
    info['ID'] = id_match.group(1) if id_match else ''

    # Extract pattern name
    name_match = re.search(r'\*\*Pattern Name\*\*\s*\|\s*([^|]+)', content)
    info['Pattern_Name'] = name_match.group(1).strip() if name_match else ''

    # Extract short name
    short_match = re.search(r'\*\*Short Name\*\*:\s*(.+)', content)
    info['Short_Name'] = short_match.group(1).strip() if short_match else ''

    # Extract category
    cat_match = re.search(r'\*\*Pattern Category\*\*\s*\|\s*`?([^`|\n]+)`?', content)
    info['Category'] = cat_match.group(1).strip() if cat_match else ''

    # Extract pattern type
    type_match = re.search(r'\*\*Pattern Type\*\*:\s*(.+)', content)
    info['Pattern_Type'] = type_match.group(1).strip() if type_match else ''

    # Extract maturity level
    maturity_match = re.search(r'\*\*Maturity Level\*\*\s*\|\s*`?([^`|\n]+)`?', content)
    info['Maturity_Level'] = maturity_match.group(1).strip() if maturity_match else ''

    # Extract status
    status_match = re.search(r'\*\*Status\*\*\s*\|\s*`?([^`|\n]+)`?', content)
    info['Status'] = status_match.group(1).strip() if status_match else ''

    # Extract intent statement
    intent_match = re.search(r'\*\*Intent Statement\*\*:\s*\n(.+?)(?:\n\n|\*\*Problem)', content, re.DOTALL)
    intent = intent_match.group(1).strip().replace('\n', ' ') if intent_match else ''
    if len(intent) > 300:
        intent = intent[:297] + '...'
    info['Description'] = intent

    return info

def main():
    patterns = []

    # Find all pattern markdown files
    pattern_files = sorted(PATTERNS_ROOT.glob("PT-*/PT-*.md"))

    for pattern_file in pattern_files:
        with open(pattern_file, 'r', encoding='utf-8') as f:
            content = f.read()

        info = extract_pattern_info(content)
        patterns.append(info)
        print(f"Processed: {info['ID']} - {info['Pattern_Name']}")

    # Write CSV
    fieldnames = ['ID', 'Pattern_Name', 'Short_Name', 'Category', 'Pattern_Type', 'Status', 'Maturity_Level', 'Description']

    with open(OUTPUT_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(patterns)

    print(f"\nCreated: {OUTPUT_CSV}")
    print(f"Total patterns: {len(patterns)}")

if __name__ == "__main__":
    main()
