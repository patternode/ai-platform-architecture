#!/usr/bin/env python3
"""
Script: update-abb-titles.py
Purpose: Update all ABB markdown documents to use the ABB name as the document title
Author: BNZ Enterprise Architecture
Date: 2025-12-06
"""

import os
import re
from pathlib import Path

# Configuration
ABB_DIR = Path(r"D:\Work\BNZ\ai-platform-architecture\03-building-blocks\architecture-building-blocks")

def update_abb_title(filepath):
    """Update the title of an ABB markdown file to use the ABB name."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Extract ABB ID and Name from the Document Control table
    # Look for pattern like: | **ABB ID** | `ABB-XXX-001` |
    abb_id_match = re.search(r'\|\s*\*\*ABB ID\*\*\s*\|\s*`(ABB-[A-Z]+-\d+)`', content)
    abb_name_match = re.search(r'\|\s*\*\*ABB Name\*\*\s*\|\s*([^|]+)\s*\|', content)

    if abb_id_match and abb_name_match:
        abb_id = abb_id_match.group(1)
        abb_name = abb_name_match.group(1).strip()

        # Replace the generic template title with the ABB name
        # The template has: # Architecture Building Block (ABB) Template
        old_title = "# Architecture Building Block (ABB) Template"
        new_title = f"# {abb_name}"

        if old_title in content:
            content = content.replace(old_title, new_title)
        else:
            # Try to replace any existing H1 title
            content = re.sub(r'^# .+$', new_title, content, count=1, flags=re.MULTILINE)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("=" * 70)
    print("Update ABB Document Titles")
    print("=" * 70)
    print()

    updated = 0
    skipped = 0

    # Process each ABB folder
    for abb_folder in sorted(ABB_DIR.iterdir()):
        if abb_folder.is_dir() and abb_folder.name.startswith("ABB-"):
            # Find markdown files in the ABB folder
            for md_file in abb_folder.glob("*.md"):
                if update_abb_title(md_file):
                    updated += 1
                    print(f"  Updated: {md_file.name}")
                else:
                    skipped += 1

    print()
    print("=" * 70)
    print(f"Summary: Updated {updated} files, skipped {skipped} files")
    print("=" * 70)

if __name__ == "__main__":
    main()
