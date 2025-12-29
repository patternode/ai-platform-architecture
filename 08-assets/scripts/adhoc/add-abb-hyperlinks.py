#!/usr/bin/env python3
"""
Script to convert ABB ID mentions to relative hyperlinks.
Converts plain text like 'AB-001' to '[AB-001](relative/path/to/AB-001/AB-001-Name-v1.0.0.md)'
"""

import os
import re
import csv
from pathlib import Path
from collections import OrderedDict

# Paths
REPO_ROOT = Path(r"D:\Work\BNZ\ai-platform-architecture")
ABB_ROOT = REPO_ROOT / "03-building-blocks" / "architecture-building-blocks" / "abbs"

def build_abb_lookup():
    """Build a lookup of ABB ID to file info."""
    lookup = {}

    for abb_folder in ABB_ROOT.iterdir():
        if not abb_folder.is_dir() or not abb_folder.name.startswith('AB-'):
            continue

        abb_id = abb_folder.name
        md_files = list(abb_folder.glob('AB-*.md'))

        if md_files:
            md_file = md_files[0]
            # Extract name from filename: AB-NNN-Name-vX.X.X.md
            match = re.match(r'AB-\d+-(.+)-v\d+\.\d+\.\d+\.md', md_file.name)
            name = match.group(1).replace('-', ' ') if match else abb_id

            lookup[abb_id] = {
                'folder': abb_folder.name,
                'filename': md_file.name,
                'name': name,
                'full_path': md_file
            }

    return lookup

def get_relative_path(from_file, to_abb_id, abb_lookup):
    """Calculate the relative path from a file to an ABB document."""
    if to_abb_id not in abb_lookup:
        return None

    abb_info = abb_lookup[to_abb_id]
    to_path = abb_info['full_path']

    try:
        # Get the relative path from the source file's directory to the ABB file
        from_dir = from_file.parent
        rel_path = os.path.relpath(to_path, from_dir)
        # Convert Windows backslashes to forward slashes for markdown
        rel_path = rel_path.replace('\\', '/')
        return rel_path
    except ValueError:
        # Different drives on Windows
        return None

def process_file(file_path, abb_lookup, dry_run=False):
    """Process a single file to add ABB hyperlinks."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return False, 0, "Unicode decode error"

    original_content = content
    replacements = 0

    # Pattern to match ABB IDs that are NOT already in a markdown link
    # We need to be careful not to match IDs that are already links
    # Pattern: AB-NNN where NNN is 3 digits
    # Avoid matching if preceded by [ or followed by ]( or if inside a link

    # First, let's find all AB-NNN patterns and their contexts
    pattern = r'(?<!\[)(?<!/)(AB-\d{3})(?!\]\()(?!\d)'

    def replace_with_link(match):
        nonlocal replacements
        abb_id = match.group(1)

        if abb_id not in abb_lookup:
            return match.group(0)  # Keep original if ABB not found

        rel_path = get_relative_path(file_path, abb_id, abb_lookup)
        if rel_path is None:
            return match.group(0)

        replacements += 1
        return f'[{abb_id}]({rel_path})'

    # Apply the replacement
    content = re.sub(pattern, replace_with_link, content)

    if content != original_content and not dry_run:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, replacements, None

    return content != original_content, replacements, None

def process_all_files(abb_lookup, dry_run=False):
    """Process all markdown files in the repository."""
    results = {
        'updated': [],
        'skipped': [],
        'errors': []
    }

    # File patterns to process
    patterns = [
        '03-building-blocks/**/*.md',
        '01-motivation/**/*.md',
        '05-governance/**/*.md',
        '02-capabilities/**/*.md',
    ]

    for pattern in patterns:
        print(f"\nProcessing: {pattern}")
        for file_path in REPO_ROOT.glob(pattern):
            if not file_path.is_file():
                continue

            # Skip the file itself if it's an ABB file (to avoid self-references becoming links)
            # Actually, we DO want to process ABB files for cross-references

            updated, count, error = process_file(file_path, abb_lookup, dry_run)

            if error:
                results['errors'].append((str(file_path.relative_to(REPO_ROOT)), error))
            elif updated:
                results['updated'].append((str(file_path.relative_to(REPO_ROOT)), count))
                print(f"  {'[DRY RUN] Would update' if dry_run else 'Updated'}: {file_path.name} ({count} links)")
            else:
                results['skipped'].append(str(file_path.relative_to(REPO_ROOT)))

    return results

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Add hyperlinks to ABB ID references')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be changed without making changes')
    args = parser.parse_args()

    print("=" * 60)
    print("ABB Hyperlink Addition Script")
    print("=" * 60)

    if args.dry_run:
        print("\n*** DRY RUN MODE - No changes will be made ***\n")

    # Build ABB lookup
    print("\n1. Building ABB lookup...")
    abb_lookup = build_abb_lookup()
    print(f"   Found {len(abb_lookup)} ABBs")

    # Show sample
    print("\n   Sample entries:")
    for i, (abb_id, info) in enumerate(list(abb_lookup.items())[:5]):
        print(f"     {abb_id}: {info['name']}")
    print("     ...")

    # Process files
    print("\n2. Processing files...")
    results = process_all_files(abb_lookup, args.dry_run)

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    total_links = sum(count for _, count in results['updated'])
    print(f"Files updated: {len(results['updated'])}")
    print(f"Total hyperlinks added: {total_links}")
    print(f"Files skipped (no changes): {len(results['skipped'])}")
    print(f"Errors: {len(results['errors'])}")

    if results['errors']:
        print("\nErrors:")
        for path, error in results['errors'][:10]:
            print(f"  - {path}: {error}")

    if args.dry_run:
        print("\n*** This was a dry run. Run without --dry-run to apply changes. ***")

    print("\nDone!")

if __name__ == "__main__":
    main()
