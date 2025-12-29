#!/usr/bin/env python3
"""
Script to update section 7.1 (Capability Mapping) in all ABB files
using capability IDs from capabilities-consolidated.csv
"""

import csv
import os
import re
from pathlib import Path
from collections import defaultdict

# Paths
REPO_ROOT = Path(r"D:\Work\BNZ\ai-platform-architecture")
CSV_PATH = REPO_ROOT / "02-capabilities" / "capabilities-consolidated.csv"
ABB_ROOT = REPO_ROOT / "03-building-blocks" / "architecture-building-blocks" / "abbs"

def parse_capabilities_csv():
    """Parse the CSV and build ABB to capabilities mapping."""
    abb_to_caps = defaultdict(list)
    all_caps = {}

    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cap_id = row['ID']
            cap_name = row['Capability_Name']
            level = row['Level']
            definition = row['Definition']
            technologies = row.get('Technologies', '')

            # Store capability info
            all_caps[cap_id] = {
                'id': cap_id,
                'name': cap_name,
                'level': level,
                'definition': definition
            }

            # Extract ABB references from Technologies column
            if technologies and 'ABB' in technologies:
                # Pattern: ABBs: ABB-XXX-001 or just ABB-XXX-001
                abb_matches = re.findall(r'ABB-[A-Z]+-\d+', technologies)
                for abb_id in abb_matches:
                    abb_to_caps[abb_id].append({
                        'id': cap_id,
                        'name': cap_name,
                        'level': level,
                        'definition': definition
                    })

    return abb_to_caps, all_caps

def get_abb_info(abb_file):
    """Extract ABB ID and name from file."""
    # Extract from filename: ABB-XXX-001-Name-v1.0.0.md
    filename = abb_file.name
    match = re.match(r'(ABB-[A-Z]+-\d+)-(.+)-v\d+\.\d+\.\d+\.md', filename)
    if match:
        abb_id = match.group(1)
        abb_name = match.group(2).replace('-', ' ')
        return abb_id, abb_name
    return None, None

def generate_support_description(abb_name, abb_id, cap_name, cap_definition):
    """Generate a meaningful 'How This ABB Supports' description."""
    abb_name_lower = abb_name.lower()
    cap_name_lower = cap_name.lower()

    # Extract ABB category from ID (e.g., AGT, GEN, SEC, etc.)
    abb_category = abb_id.split('-')[1] if '-' in abb_id else ''

    # Map ABB categories to action verbs and descriptions
    category_actions = {
        'AGT': ('orchestrates', 'coordinates', 'manages'),
        'GEN': ('generates', 'processes', 'produces'),
        'SEC': ('secures', 'protects', 'enforces'),
        'GOV': ('governs', 'monitors', 'ensures compliance for'),
        'OBS': ('monitors', 'tracks', 'observes'),
        'MLO': ('automates', 'manages', 'orchestrates'),
        'DAT': ('stores', 'manages', 'provides'),
        'FTR': ('provides', 'serves', 'manages'),
        'INF': ('executes', 'serves', 'processes'),
        'INT': ('integrates', 'processes', 'handles'),
        'CNV': ('manages', 'processes', 'handles'),
        'DOC': ('processes', 'analyzes', 'classifies'),
        'RTE': ('routes', 'directs', 'optimizes'),
        'BAT': ('processes', 'manages', 'executes'),
        'CMP': ('compares', 'evaluates', 'tests'),
        'KNW': ('stores', 'retrieves', 'manages'),
        'VAL': ('validates', 'verifies', 'checks'),
        'VIS': ('visualizes', 'displays', 'presents'),
        'WFL': ('orchestrates', 'manages', 'coordinates'),
        'API': ('exposes', 'provides access to', 'serves'),
        'CAC': ('caches', 'stores', 'optimizes'),
        'NLP': ('extracts', 'processes', 'analyzes'),
        'NLG': ('generates', 'produces', 'creates'),
        'STR': ('streams', 'processes', 'handles'),
        'LDB': ('balances', 'distributes', 'routes'),
        'MDL': ('serves', 'manages', 'deploys'),
        'FAI': ('monitors', 'detects', 'ensures'),
        'DSH': ('catalogs', 'manages', 'governs'),
    }

    actions = category_actions.get(abb_category, ('provides', 'supports', 'enables'))
    primary_action = actions[0]

    # Generate description based on ABB function
    if 'orchestrat' in abb_name_lower:
        desc = f"Coordinates and manages {cap_name_lower} workflows and execution"
    elif 'registry' in abb_name_lower:
        desc = f"Provides centralized registration and versioning for {cap_name_lower}"
    elif 'monitor' in abb_name_lower:
        desc = f"Continuously monitors and alerts on {cap_name_lower} metrics"
    elif 'engine' in abb_name_lower:
        desc = f"Core processing engine that {primary_action} {cap_name_lower}"
    elif 'gateway' in abb_name_lower:
        desc = f"Provides unified API access for {cap_name_lower}"
    elif 'service' in abb_name_lower:
        desc = f"Delivers {cap_name_lower} as a managed service"
    elif 'store' in abb_name_lower or 'storage' in abb_name_lower:
        desc = f"Stores and serves data for {cap_name_lower}"
    elif 'pipeline' in abb_name_lower:
        desc = f"Automates end-to-end {cap_name_lower} workflows"
    elif 'framework' in abb_name_lower:
        desc = f"Provides standardized framework for {cap_name_lower}"
    elif 'platform' in abb_name_lower:
        desc = f"Provides infrastructure platform for {cap_name_lower}"
    elif 'detector' in abb_name_lower or 'detection' in abb_name_lower:
        desc = f"Detects and identifies {cap_name_lower} patterns"
    elif 'tracker' in abb_name_lower:
        desc = f"Tracks and maintains history of {cap_name_lower}"
    elif 'validator' in abb_name_lower or 'validation' in abb_name_lower:
        desc = f"Validates and ensures quality of {cap_name_lower}"
    elif 'router' in abb_name_lower:
        desc = f"Intelligently routes requests based on {cap_name_lower} criteria"
    elif 'analyzer' in abb_name_lower:
        desc = f"Analyzes and extracts insights for {cap_name_lower}"
    elif 'generator' in abb_name_lower:
        desc = f"Generates {cap_name_lower} outputs"
    elif 'manager' in abb_name_lower:
        desc = f"Manages lifecycle and configuration of {cap_name_lower}"
    elif 'dashboard' in abb_name_lower:
        desc = f"Visualizes and reports on {cap_name_lower} metrics"
    elif 'bus' in abb_name_lower:
        desc = f"Enables message-based communication for {cap_name_lower}"
    elif 'catalog' in abb_name_lower:
        desc = f"Catalogs and discovers {cap_name_lower} assets"
    elif 'layer' in abb_name_lower:
        desc = f"Provides abstraction layer for {cap_name_lower}"
    elif 'workflow' in abb_name_lower:
        desc = f"Orchestrates {cap_name_lower} workflow processes"
    elif 'controller' in abb_name_lower:
        desc = f"Controls and manages {cap_name_lower} operations"
    elif 'balancer' in abb_name_lower:
        desc = f"Distributes load for {cap_name_lower} processing"
    elif 'broker' in abb_name_lower:
        desc = f"Brokers events and messages for {cap_name_lower}"
    elif 'queue' in abb_name_lower:
        desc = f"Queues and manages {cap_name_lower} messages"
    elif 'trigger' in abb_name_lower:
        desc = f"Triggers automated actions for {cap_name_lower}"
    elif 'cache' in abb_name_lower or 'caching' in abb_name_lower:
        desc = f"Caches and optimizes {cap_name_lower} responses"
    else:
        # Default description using the capability definition if available
        if cap_definition and len(cap_definition) > 10:
            # Use first part of definition
            short_def = cap_definition.split('.')[0].split(',')[0]
            if len(short_def) > 80:
                short_def = short_def[:77] + "..."
            desc = f"Enables {short_def.lower()}"
        else:
            desc = f"Provides core implementation for {cap_name_lower}"

    return desc

def generate_capability_table(abb_id, abb_name, capabilities, all_caps):
    """Generate the capability mapping table for an ABB."""
    lines = []
    lines.append("| Capability ID | Capability Name | Description | Level | How This ABB Supports |")
    lines.append("|---------------|-----------------|-------------|-------|----------------------|")

    if capabilities:
        for cap in capabilities:
            # Get description from capability definition
            definition = cap.get('definition', '')
            # Truncate if too long for table
            if len(definition) > 100:
                definition = definition[:97] + "..."

            # Generate meaningful support description
            support_desc = generate_support_description(abb_name, abb_id, cap['name'], cap.get('definition', ''))

            lines.append(f"| {cap['id']} | {cap['name']} | {definition} | {cap['level']} | {support_desc} |")
    else:
        # No direct mapping found - add placeholder
        lines.append("| *No direct mappings* | - | - | - | *Requires manual mapping based on ABB function* |")

    return "\n".join(lines)

def update_abb_file(abb_file, abb_id, capabilities, all_caps):
    """Update the capability mapping section in an ABB file."""
    with open(abb_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and replace section 7.1
    # Pattern: ### 7.1 Capability Mapping ... (until ### 7.2 or next section)
    pattern = r'(### 7\.1 Capability Mapping\s*\n)(.*?)(\n### 7\.2|\n---)'

    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"  WARNING: Could not find section 7.1 in {abb_file.name}")
        return False

    # Get ABB name from file
    _, abb_name = get_abb_info(abb_file)

    # Generate new table
    new_table = generate_capability_table(abb_id, abb_name, capabilities, all_caps)

    # Replace the section
    new_content = content[:match.start(2)] + "\n" + new_table + "\n" + content[match.end(2):]

    with open(abb_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    print("Parsing capabilities CSV...")
    abb_to_caps, all_caps = parse_capabilities_csv()

    print(f"Found {len(abb_to_caps)} ABBs with capability mappings")
    print(f"Total capabilities: {len(all_caps)}")

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

        capabilities = abb_to_caps.get(abb_id, [])
        print(f"Processing {abb_id}: {len(capabilities)} capabilities mapped")

        try:
            if update_abb_file(abb_file, abb_id, capabilities, all_caps):
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

    # Print ABBs without mappings for manual review
    print("\nABBs without capability mappings (need manual review):")
    for abb_file in sorted(abb_files):
        abb_id, _ = get_abb_info(abb_file)
        if abb_id and abb_id not in abb_to_caps:
            print(f"  - {abb_id}")

if __name__ == "__main__":
    main()
