#!/usr/bin/env python3
"""
Script to update section 7.3 (Use Case Support) in all ABB files
by parsing use case files for ABB references and pattern usage.
"""

import csv
import re
from pathlib import Path
from collections import defaultdict

# Paths
REPO_ROOT = Path(r"D:\Work\BNZ\ai-platform-architecture")
USE_CASES_ROOT = REPO_ROOT / "01-motivation" / "03-use-cases" / "use-cases"
ABB_ROOT = REPO_ROOT / "03-building-blocks" / "architecture-building-blocks" / "abbs"
CAPS_CSV_PATH = REPO_ROOT / "02-capabilities" / "capabilities-consolidated.csv"

def load_pattern_to_abb_mapping():
    """Load mapping from patterns to ABBs from capabilities CSV."""
    pattern_to_abbs = defaultdict(set)

    with open(CAPS_CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key_components = row.get('Key_Components', '')
            technologies = row.get('Technologies', '')

            # Extract pattern references
            pattern_matches = re.findall(r'PT-\d+', key_components)
            # Extract ABB references
            abb_matches = re.findall(r'ABB-[A-Z]+-\d+', technologies)

            # Map patterns to ABBs
            for pattern_id in pattern_matches:
                for abb_id in abb_matches:
                    pattern_to_abbs[pattern_id].add(abb_id)

    return pattern_to_abbs

def parse_use_cases():
    """Parse all use case files and extract ABB references."""
    abb_to_usecases = defaultdict(list)
    all_usecases = {}

    # Load pattern to ABB mapping
    pattern_to_abbs = load_pattern_to_abb_mapping()
    print(f"Loaded {len(pattern_to_abbs)} patterns with ABB mappings")

    # Find all use case markdown files
    for uc_dir in sorted(USE_CASES_ROOT.glob("UC-*")):
        uc_files = list(uc_dir.glob("UC-*-v*.md"))
        if not uc_files:
            continue

        uc_file = uc_files[0]
        with open(uc_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract use case ID
        id_match = re.search(r'\*\*Use Case ID\*\*\s*\|\s*`?(UC-\d+)`?', content)
        uc_id = id_match.group(1) if id_match else uc_dir.name

        # Extract use case name
        name_match = re.search(r'\*\*Use Case Name\*\*\s*\|\s*([^|\n]+)', content)
        uc_name = name_match.group(1).strip() if name_match else ''

        # Extract one-line summary
        summary_match = re.search(r'\*\*One-Line Summary\*\*:\s*\n(.+?)(?:\n\n|\*\*Business)', content, re.DOTALL)
        summary = summary_match.group(1).strip().replace('\n', ' ') if summary_match else ''
        if len(summary) > 150:
            summary = summary[:147] + "..."

        # Extract status
        status_match = re.search(r'\*\*Status\*\*\s*\|\s*`?([^`|\n]+)`?', content)
        status = status_match.group(1).strip() if status_match else 'Draft'

        # Store use case info
        uc_info = {
            'id': uc_id,
            'name': uc_name,
            'summary': summary,
            'status': status
        }
        all_usecases[uc_id] = uc_info

        # Extract direct ABB references from the content
        abb_matches = re.findall(r'ABB-[A-Z]+-\d+', content)
        unique_abbs = set(abb_matches)

        # Extract pattern references and infer ABBs
        pattern_matches = re.findall(r'PT-\d+', content)
        unique_patterns = set(pattern_matches)

        # Add ABBs from patterns
        for pattern_id in unique_patterns:
            if pattern_id in pattern_to_abbs:
                unique_abbs.update(pattern_to_abbs[pattern_id])

        for abb_id in unique_abbs:
            # Check if already added to avoid duplicates
            existing = [u for u in abb_to_usecases[abb_id] if u['id'] == uc_id]
            if not existing:
                abb_to_usecases[abb_id].append(uc_info.copy())

        print(f"Processed {uc_id}: {uc_name} - {len(unique_abbs)} ABBs (direct + via {len(unique_patterns)} patterns)")

    return abb_to_usecases, all_usecases

def get_abb_info(abb_file):
    """Extract ABB ID and name from file."""
    filename = abb_file.name
    match = re.match(r'(ABB-[A-Z]+-\d+)-(.+)-v\d+\.\d+\.\d+\.md', filename)
    if match:
        abb_id = match.group(1)
        abb_name = match.group(2).replace('-', ' ')
        return abb_id, abb_name
    return None, None

def generate_support_description(abb_name, uc_name):
    """Generate a description of how the ABB supports the use case."""
    abb_name_lower = abb_name.lower()

    if 'orchestrat' in abb_name_lower:
        return f"Coordinates AI workflows for {uc_name}"
    elif 'registry' in abb_name_lower:
        return f"Provides model/tool registration for {uc_name}"
    elif 'monitor' in abb_name_lower:
        return f"Monitors performance and drift for {uc_name}"
    elif 'engine' in abb_name_lower:
        return f"Core processing engine for {uc_name}"
    elif 'gateway' in abb_name_lower:
        return f"API gateway for {uc_name} services"
    elif 'service' in abb_name_lower:
        return f"Provides managed services for {uc_name}"
    elif 'store' in abb_name_lower or 'storage' in abb_name_lower:
        return f"Data storage and retrieval for {uc_name}"
    elif 'pipeline' in abb_name_lower:
        return f"Automates workflows for {uc_name}"
    elif 'framework' in abb_name_lower:
        return f"Framework implementation for {uc_name}"
    elif 'platform' in abb_name_lower:
        return f"Platform infrastructure for {uc_name}"
    elif 'detector' in abb_name_lower:
        return f"Detection capabilities for {uc_name}"
    elif 'router' in abb_name_lower:
        return f"Intelligent routing for {uc_name}"
    elif 'database' in abb_name_lower:
        return f"Data management for {uc_name}"
    elif 'search' in abb_name_lower:
        return f"Search capabilities for {uc_name}"
    else:
        return f"Enables {uc_name} functionality"

def generate_usecase_table(abb_id, abb_name, usecases):
    """Generate the use case support table for an ABB."""
    lines = []
    lines.append("| Use Case ID | Use Case Name | Description | How This ABB Supports |")
    lines.append("|-------------|---------------|-------------|----------------------|")

    if usecases:
        for uc in sorted(usecases, key=lambda x: x['id']):
            # Truncate summary if too long
            summary = uc['summary']
            if len(summary) > 80:
                summary = summary[:77] + "..."

            support_desc = generate_support_description(abb_name, uc['name'])

            lines.append(f"| {uc['id']} | {uc['name']} | {summary} | {support_desc} |")
    else:
        lines.append("| *No use case mappings* | - | - | *Platform/cross-cutting component* |")

    return "\n".join(lines)

def update_abb_file(abb_file, abb_id, abb_name, usecases):
    """Update the use case support section in an ABB file."""
    with open(abb_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find and replace section 7.3
    # Pattern: ### 7.3 Use Case Support ... (until --- or next section)
    pattern = r'(### 7\.3 Use Case Support\s*\n)(.*?)(\n---|\n## 8\.)'

    match = re.search(pattern, content, re.DOTALL)
    if not match:
        print(f"  WARNING: Could not find section 7.3 in {abb_file.name}")
        return False

    # Generate new table
    new_table = generate_usecase_table(abb_id, abb_name, usecases)

    # Replace the section
    new_content = content[:match.start(2)] + "\n" + new_table + "\n" + content[match.end(2):]

    with open(abb_file, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True

def main():
    print("Parsing use cases for ABB references...")
    abb_to_usecases, all_usecases = parse_use_cases()
    print(f"\nFound {len(all_usecases)} use cases")
    print(f"Found {len(abb_to_usecases)} ABBs referenced in use cases")

    # Find all ABB files
    abb_files = list(ABB_ROOT.glob("**/ABB-*.md"))
    print(f"Found {len(abb_files)} ABB files\n")

    updated = 0
    skipped = 0
    errors = 0

    for abb_file in sorted(abb_files):
        abb_id, abb_name = get_abb_info(abb_file)
        if not abb_id:
            print(f"  SKIP: Could not parse ABB ID from {abb_file.name}")
            skipped += 1
            continue

        usecases = abb_to_usecases.get(abb_id, [])
        print(f"Processing {abb_id}: {len(usecases)} use cases")

        try:
            if update_abb_file(abb_file, abb_id, abb_name, usecases):
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

    # Print statistics
    print("\nABBs by use case coverage:")
    coverage_counts = defaultdict(int)
    for abb_id in abb_to_usecases:
        count = len(abb_to_usecases[abb_id])
        if count >= 10:
            coverage_counts['10+'] += 1
        elif count >= 5:
            coverage_counts['5-9'] += 1
        elif count >= 1:
            coverage_counts['1-4'] += 1

    for abb_file in abb_files:
        abb_id, _ = get_abb_info(abb_file)
        if abb_id and abb_id not in abb_to_usecases:
            coverage_counts['0'] += 1

    print(f"  10+ use cases: {coverage_counts.get('10+', 0)} ABBs")
    print(f"  5-9 use cases: {coverage_counts.get('5-9', 0)} ABBs")
    print(f"  1-4 use cases: {coverage_counts.get('1-4', 0)} ABBs")
    print(f"  0 use cases: {coverage_counts.get('0', 0)} ABBs (platform/cross-cutting)")

if __name__ == "__main__":
    main()
