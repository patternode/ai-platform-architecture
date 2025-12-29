#!/usr/bin/env python3
"""
Script to update section 7.2 (Pattern Usage) in all ABB files
using pattern references from capabilities-consolidated.csv
"""

import csv
import re
from pathlib import Path
from collections import defaultdict

# Paths
REPO_ROOT = Path(r"D:\Work\BNZ\ai-platform-architecture")
CAPS_CSV_PATH = REPO_ROOT / "02-capabilities" / "capabilities-consolidated.csv"
PATTERNS_CSV_PATH = REPO_ROOT / "03-building-blocks" / "patterns" / "patterns-consolidated.csv"
ABB_ROOT = REPO_ROOT / "03-building-blocks" / "architecture-building-blocks" / "abbs"

def load_patterns():
    """Load pattern information from patterns CSV."""
    patterns = {}
    with open(PATTERNS_CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pattern_id = row['ID']
            patterns[pattern_id] = {
                'id': pattern_id,
                'name': row['Pattern_Name'],
                'short_name': row['Short_Name'],
                'category': row['Category'],
                'description': row['Description']
            }
    return patterns

def parse_capabilities_for_patterns():
    """Parse the capabilities CSV and build ABB to patterns mapping."""
    abb_to_patterns = defaultdict(set)

    with open(CAPS_CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key_components = row.get('Key_Components', '')
            technologies = row.get('Technologies', '')

            # Extract pattern references from Key_Components column
            pattern_matches = re.findall(r'PT-\d+', key_components)

            # Extract ABB references from Technologies column
            abb_matches = re.findall(r'ABB-[A-Z]+-\d+', technologies)

            # Map each ABB to the patterns
            for abb_id in abb_matches:
                for pattern_id in pattern_matches:
                    abb_to_patterns[abb_id].add(pattern_id)

    return abb_to_patterns

def get_abb_info(abb_file):
    """Extract ABB ID and name from file."""
    filename = abb_file.name
    match = re.match(r'(ABB-[A-Z]+-\d+)-(.+)-v\d+\.\d+\.\d+\.md', filename)
    if match:
        abb_id = match.group(1)
        abb_name = match.group(2).replace('-', ' ')
        return abb_id, abb_name
    return None, None

def determine_role(abb_name, abb_id, pattern_name, pattern_category):
    """Determine the ABB's role in the pattern."""
    abb_name_lower = abb_name.lower()
    abb_category = abb_id.split('-')[1] if '-' in abb_id else ''
    pattern_category_lower = pattern_category.lower()

    # Primary role indicators
    if 'orchestrat' in abb_name_lower:
        return 'Primary'
    if 'engine' in abb_name_lower:
        return 'Primary'
    if 'platform' in abb_name_lower:
        return 'Primary'

    # Category-based role determination
    category_primary_patterns = {
        'AGT': ['Agent', 'Agentic'],
        'GEN': ['GenAI', 'RAG'],
        'SEC': ['Security', 'Cross-Cutting'],
        'GOV': ['Governance'],
        'OBS': ['Cross-Cutting', 'Observability'],
        'MLO': ['Governance', 'ML Prediction'],
        'DAT': ['Data'],
        'FTR': ['Data', 'ML Prediction'],
        'INF': ['ML Prediction', 'Real-Time'],
        'INT': ['Real-Time', 'Integration'],
        'CNV': ['GenAI', 'Conversational'],
        'DOC': ['Document Intelligence'],
        'RTE': ['GenAI', 'Integration'],
        'BAT': ['ML Prediction'],
        'CMP': ['Governance'],
    }

    primary_patterns = category_primary_patterns.get(abb_category, [])
    for p in primary_patterns:
        if p.lower() in pattern_category_lower or p.lower() in pattern_name.lower():
            return 'Primary'

    # Supporting role for registries, stores, monitors
    if any(x in abb_name_lower for x in ['registry', 'store', 'monitor', 'tracker', 'validator']):
        return 'Supporting'

    # Cross-cutting for security, governance, observability ABBs
    if abb_category in ['SEC', 'GOV', 'OBS'] and 'Cross-Cutting' in pattern_category:
        return 'Cross-cutting'

    return 'Supporting'

def generate_pattern_table(abb_id, abb_name, pattern_ids, all_patterns):
    """Generate the pattern usage table for an ABB."""
    lines = []
    lines.append("| Pattern ID | Pattern Name | Description | Role in Pattern |")
    lines.append("|------------|--------------|-------------|-----------------|")

    if pattern_ids:
        for pattern_id in sorted(pattern_ids):
            if pattern_id in all_patterns:
                pattern = all_patterns[pattern_id]
                # Truncate description if too long
                desc = pattern['description']
                if len(desc) > 80:
                    desc = desc[:77] + "..."
                role = determine_role(abb_name, abb_id, pattern['name'], pattern['category'])
                lines.append(f"| {pattern_id} | {pattern['name']} | {desc} | {role} |")
    else:
        lines.append("| *No pattern mappings* | - | - | *Requires manual mapping* |")

    return "\n".join(lines)

def update_abb_file(abb_file, abb_id, abb_name, pattern_ids, all_patterns):
    """Update the pattern usage section in an ABB file."""
    with open(abb_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and replace section 7.2
    # Pattern: ### 7.2 Pattern Usage ... (until ### 7.3 or next section)
    pattern = r'(### 7\.2 Pattern Usage\s*\n)(.*?)(\n### 7\.3|\n---)'

    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"  WARNING: Could not find section 7.2 in {abb_file.name}")
        return False

    # Generate new table
    new_table = generate_pattern_table(abb_id, abb_name, pattern_ids, all_patterns)

    # Replace the section
    new_content = content[:match.start(2)] + "\n" + new_table + "\n" + content[match.end(2):]

    with open(abb_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    print("Loading patterns...")
    all_patterns = load_patterns()
    print(f"Loaded {len(all_patterns)} patterns")

    print("Parsing capabilities for pattern mappings...")
    abb_to_patterns = parse_capabilities_for_patterns()
    print(f"Found {len(abb_to_patterns)} ABBs with pattern mappings")

    # Find all ABB files
    abb_files = list(ABB_ROOT.glob("**/ABB-*.md"))
    print(f"Found {len(abb_files)} ABB files")

    updated = 0
    skipped = 0
    errors = 0

    for abb_file in sorted(abb_files):
        abb_id, abb_name = get_abb_info(abb_file)
        if not abb_id:
            print(f"  SKIP: Could not parse ABB ID from {abb_file.name}")
            skipped += 1
            continue

        pattern_ids = abb_to_patterns.get(abb_id, set())
        print(f"Processing {abb_id}: {len(pattern_ids)} patterns mapped")

        try:
            if update_abb_file(abb_file, abb_id, abb_name, pattern_ids, all_patterns):
                updated += 1
            else:
                errors += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            errors += 1

    print(f"\nSummary:")
    print(f"  Updated: {updated}")
    print(f"  Skipped: {skipped}")
    print(f"  Errors: {errors}")

    # Print ABBs without pattern mappings
    print("\nABBs without pattern mappings (need manual review):")
    for abb_file in sorted(abb_files):
        abb_id, _ = get_abb_info(abb_file)
        if abb_id and abb_id not in abb_to_patterns:
            print(f"  - {abb_id}")

if __name__ == "__main__":
    main()
