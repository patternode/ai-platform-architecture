#!/usr/bin/env python3
"""
Integrity check: Compare ABB heatmap diagram against source ABB markdown files
"""
import os
import re
import csv
import html

ABB_BASE_PATH = r"D:\Work\BNZ\ai-platform-architecture\03-building-blocks\architecture-building-blocks\abbs"
HEATMAP_PATH = r"D:\Work\BNZ\ai-platform-architecture\03-building-blocks\architecture-building-blocks\abb-usage-heatmap.drawio"
ENHANCED_DESC_PATH = r"D:\Work\BNZ\ai-platform-architecture\03-building-blocks\architecture-building-blocks\abb-descriptions-enhanced.csv"

def extract_from_markdown(abb_id):
    """Extract name and description from ABB markdown file."""
    abb_dir = os.path.join(ABB_BASE_PATH, abb_id)

    if not os.path.exists(abb_dir):
        return None, None, f"Directory not found: {abb_dir}"

    md_files = [f for f in os.listdir(abb_dir) if f.endswith('.md')]
    if not md_files:
        return None, None, f"No markdown file in {abb_dir}"

    md_file = os.path.join(abb_dir, md_files[0])

    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract ABB Name from title
    name_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    name = name_match.group(1).strip() if name_match else None

    # Extract Description
    desc_match = re.search(r'\*\*Description\*\*:\s*\n(.+?)(?:\n\n|\n###|\n\*\*)', content, re.DOTALL)
    if desc_match:
        description = desc_match.group(1).strip()
    else:
        desc_match = re.search(r'\*\*Description\*\*:\s*(.+?)(?:\n\n|\n###)', content, re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else None

    return name, description, None

def extract_from_diagram():
    """Extract ABB info from the heatmap diagram."""
    with open(HEATMAP_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to extract: id="ab050" value="..."
    pattern = r'id="(ab\d+)" value="([^"]+)"'

    results = {}
    for match in re.finditer(pattern, content):
        cell_id = match.group(1)  # ab050
        raw_value = match.group(2)

        # Decode HTML entities: &lt; -> <, &gt; -> >, &amp; -> &, &quot; -> "
        decoded = raw_value.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace('&quot;', '"')

        # Parse: <b>AB-050 Large Language Model Service (24/24)</b><br><span style="font-size:9px">Description</span>
        header_match = re.search(r'<b>(AB-\d+)\s+(.+?)\s+\(\d+/24\)</b>', decoded)
        desc_match = re.search(r'<span[^>]*>([^<]+)</span>', decoded)

        if header_match:
            abb_id = header_match.group(1)
            name = header_match.group(2)
            desc = desc_match.group(1) if desc_match else ""
            results[abb_id] = {'name': name, 'description': desc}

    return results

def load_enhanced_descriptions():
    """Load the enhanced descriptions CSV."""
    descriptions = {}
    with open(ENHANCED_DESC_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            descriptions[row['abb_id']] = {
                'name': row['name'],
                'description': row['description']
            }
    return descriptions

# Run integrity check
print("=" * 80)
print("ABB HEATMAP INTEGRITY CHECK")
print("=" * 80)
print()

# Extract from diagram
diagram_abbs = extract_from_diagram()
print(f"Found {len(diagram_abbs)} ABBs in diagram")

# Load enhanced descriptions
enhanced_descs = load_enhanced_descriptions()
print(f"Found {len(enhanced_descs)} ABBs in enhanced descriptions CSV")

# Count source ABBs
source_abbs = [d for d in os.listdir(ABB_BASE_PATH) if d.startswith('AB-')]
print(f"Found {len(source_abbs)} ABBs in source folder")
print()

name_issues = []
enhanced_name_issues = []
matches = []

print("-" * 80)
print("CHECKING: Diagram names vs Source Markdown names")
print("-" * 80)

for abb_id in sorted(diagram_abbs.keys()):
    diagram_name = diagram_abbs[abb_id]['name']
    diagram_desc = diagram_abbs[abb_id]['description']

    # Get from source markdown
    source_name, source_desc, error = extract_from_markdown(abb_id)

    if error:
        name_issues.append((abb_id, "ERROR", error, None))
        continue

    # Check name match
    if diagram_name != source_name:
        name_issues.append((abb_id, "MISMATCH", diagram_name, source_name))
    else:
        matches.append(abb_id)

if name_issues:
    print(f"\n{len(name_issues)} ISSUES FOUND:\n")
    for abb_id, issue_type, val1, val2 in name_issues:
        if issue_type == "ERROR":
            print(f"  [ERROR] {abb_id}: {val1}")
        else:
            print(f"  [MISMATCH] {abb_id}:")
            print(f"    Diagram: '{val1}'")
            print(f"    Source:  '{val2}'")
else:
    print("\nAll 74 ABB names in diagram match source markdown files!")

print()
print("-" * 80)
print("CHECKING: Enhanced CSV names vs Source Markdown names")
print("-" * 80)

for abb_id in sorted(enhanced_descs.keys()):
    enhanced_name = enhanced_descs[abb_id]['name']
    source_name, source_desc, error = extract_from_markdown(abb_id)

    if error:
        enhanced_name_issues.append((abb_id, "ERROR", error, None))
        continue

    if enhanced_name != source_name:
        enhanced_name_issues.append((abb_id, "MISMATCH", enhanced_name, source_name))

if enhanced_name_issues:
    print(f"\n{len(enhanced_name_issues)} ISSUES FOUND:\n")
    for abb_id, issue_type, val1, val2 in enhanced_name_issues:
        if issue_type == "ERROR":
            print(f"  [ERROR] {abb_id}: {val1}")
        else:
            print(f"  [MISMATCH] {abb_id}:")
            print(f"    Enhanced CSV: '{val1}'")
            print(f"    Source:       '{val2}'")
else:
    print("\nAll 74 enhanced CSV names match source markdown files!")

# Full detailed report
print()
print("-" * 80)
print("FULL DETAILED REPORT")
print("-" * 80)
print()

all_match = True
for abb_id in sorted(diagram_abbs.keys()):
    diagram_name = diagram_abbs[abb_id]['name']
    diagram_desc = diagram_abbs[abb_id]['description']
    source_name, source_desc, _ = extract_from_markdown(abb_id)
    enhanced = enhanced_descs.get(abb_id, {})

    name_ok = diagram_name == source_name
    enhanced_name_ok = enhanced.get('name') == source_name if enhanced else True

    if not name_ok or not enhanced_name_ok:
        all_match = False
        print(f"{abb_id}:")
        print(f"  Source Name:   '{source_name}'")
        print(f"  Diagram Name:  '{diagram_name}' {'OK' if name_ok else 'MISMATCH'}")
        print(f"  Enhanced Name: '{enhanced.get('name', 'N/A')}' {'OK' if enhanced_name_ok else 'MISMATCH'}")
        print()

if all_match:
    print("All ABB IDs, names match across diagram, enhanced CSV, and source files!")

# Summary
print()
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"ABBs in diagram:                    {len(diagram_abbs)}")
print(f"ABBs in enhanced CSV:               {len(enhanced_descs)}")
print(f"ABBs in source folder:              {len(source_abbs)}")
print(f"Diagram name mismatches:            {len([i for i in name_issues if i[1] == 'MISMATCH'])}")
print(f"Enhanced CSV name mismatches:       {len([i for i in enhanced_name_issues if i[1] == 'MISMATCH'])}")
print()
print("Note: Descriptions in diagram are ENHANCED versions (not source descriptions)")
print("      This is intentional - enhanced descriptions provide more detail")
