#!/usr/bin/env python3
"""
Extract ABB descriptions from markdown files and output as CSV
"""
import os
import re
import csv

# Path to ABB files
ABB_BASE_PATH = r"D:\Work\BNZ\ai-platform-architecture\03-building-blocks\architecture-building-blocks\abbs"

# ABBs from the usage CSV (only those with use case count > 0)
abbs_with_usage = [
    "AB-050", "AB-072", "AB-094", "AB-097", "AB-051", "AB-001", "AB-037", "AB-063",
    "AB-052", "AB-095", "AB-030", "AB-040", "AB-103", "AB-127", "AB-107", "AB-031",
    "AB-047", "AB-074", "AB-108", "AB-013", "AB-029", "AB-034", "AB-036", "AB-065",
    "AB-008", "AB-041", "AB-057", "AB-070", "AB-075", "AB-096", "AB-025", "AB-032",
    "AB-064", "AB-080", "AB-087", "AB-105", "AB-002", "AB-005", "AB-033", "AB-058",
    "AB-101", "AB-104", "AB-128", "AB-007", "AB-018", "AB-035", "AB-038", "AB-042",
    "AB-054", "AB-083", "AB-106", "AB-116", "AB-129", "AB-004", "AB-019", "AB-026",
    "AB-039", "AB-043", "AB-044", "AB-045", "AB-046", "AB-048", "AB-049", "AB-053",
    "AB-059", "AB-069", "AB-076", "AB-084", "AB-086", "AB-088", "AB-093", "AB-099",
    "AB-114", "AB-115"
]

def extract_description(abb_id):
    """Extract description from ABB markdown file."""
    abb_dir = os.path.join(ABB_BASE_PATH, abb_id)

    # Find the markdown file
    if not os.path.exists(abb_dir):
        return None, None

    md_files = [f for f in os.listdir(abb_dir) if f.endswith('.md')]
    if not md_files:
        return None, None

    md_file = os.path.join(abb_dir, md_files[0])

    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract ABB Name from title or table
    name_match = re.search(r'# (.+)', content)
    name = name_match.group(1).strip() if name_match else abb_id

    # Extract Description (short description after **Description**:)
    desc_match = re.search(r'\*\*Description\*\*:\s*\n(.+?)(?:\n\n|\n###|\n\*\*)', content, re.DOTALL)
    if desc_match:
        description = desc_match.group(1).strip()
    else:
        # Try alternative pattern
        desc_match = re.search(r'\*\*Description\*\*:\s*(.+?)(?:\n\n|\n###)', content, re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else "No description available"

    return name, description

# Extract all descriptions
results = []
for abb_id in abbs_with_usage:
    name, description = extract_description(abb_id)
    if name and description:
        results.append({
            'abb_id': abb_id,
            'name': name,
            'description': description
        })
        print(f"{abb_id}: {name} - {description}")

# Write to CSV
output_path = r"D:\Work\BNZ\ai-platform-architecture\03-building-blocks\architecture-building-blocks\abb-descriptions.csv"
with open(output_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['abb_id', 'name', 'description'])
    writer.writeheader()
    writer.writerows(results)

print(f"\nWrote {len(results)} ABB descriptions to {output_path}")
