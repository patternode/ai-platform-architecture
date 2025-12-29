#!/usr/bin/env python3
"""
Script to update section 2.1 (Core Capabilities) in all ABB files
using capability IDs from capabilities-consolidated.csv
"""

import csv
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
            priority = row.get('Priority', 'Medium')

            # Store capability info
            all_caps[cap_id] = {
                'id': cap_id,
                'name': cap_name,
                'level': level,
                'definition': definition,
                'priority': priority
            }

            # Extract ABB references from Technologies column
            if technologies and 'ABB' in technologies:
                abb_matches = re.findall(r'ABB-[A-Z]+-\d+', technologies)
                for abb_id in abb_matches:
                    abb_to_caps[abb_id].append({
                        'id': cap_id,
                        'name': cap_name,
                        'level': level,
                        'definition': definition,
                        'priority': priority
                    })

    return abb_to_caps, all_caps

def get_abb_info(abb_file):
    """Extract ABB ID and name from file."""
    filename = abb_file.name
    match = re.match(r'(ABB-[A-Z]+-\d+)-(.+)-v\d+\.\d+\.\d+\.md', filename)
    if match:
        abb_id = match.group(1)
        abb_name = match.group(2).replace('-', ' ')
        return abb_id, abb_name
    return None, None

def map_priority(priority_str):
    """Map priority string to standard values."""
    if not priority_str:
        return 'Should Have'
    priority_lower = priority_str.lower()
    if 'critical' in priority_lower or 'high' in priority_lower:
        return 'Must Have'
    elif 'medium' in priority_lower:
        return 'Should Have'
    elif 'low' in priority_lower:
        return 'Could Have'
    return 'Should Have'

def generate_capabilities_table(abb_id, abb_name, capabilities):
    """Generate the core capabilities table for an ABB."""
    lines = []
    lines.append("| Capability ID | Capability Name | Description | Priority |")
    lines.append("|---------------|-----------------|-------------|----------|")

    if capabilities:
        for cap in capabilities:
            # Truncate description if too long
            definition = cap.get('definition', '')
            if len(definition) > 80:
                definition = definition[:77] + "..."

            priority = map_priority(cap.get('priority', ''))

            lines.append(f"| {cap['id']} | {cap['name']} | {definition} | {priority} |")
    else:
        lines.append("| *No capabilities mapped* | - | *Requires capability mapping* | - |")

    return "\n".join(lines)

def update_abb_file(abb_file, abb_id, capabilities):
    """Update the core capabilities section in an ABB file."""
    with open(abb_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and replace section 2.1
    # Pattern: ### 2.1 Core Capabilities ... (until ### 2.2 or next section)
    pattern = r'(### 2\.1 Core Capabilities\s*\n)(.*?)(\n### 2\.2|\n---)'

    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"  WARNING: Could not find section 2.1 in {abb_file.name}")
        return False

    # Get ABB name from file
    _, abb_name = get_abb_info(abb_file)

    # Generate new table
    new_table = generate_capabilities_table(abb_id, abb_name, capabilities)

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
        print(f"Processing {abb_id}: {len(capabilities)} capabilities")

        try:
            if update_abb_file(abb_file, abb_id, capabilities):
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

if __name__ == "__main__":
    main()
