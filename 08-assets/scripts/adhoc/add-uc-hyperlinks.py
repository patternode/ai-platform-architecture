#!/usr/bin/env python3
"""
Script to convert Use Case ID mentions to relative hyperlinks.
Converts plain text like 'UC-001' to '[UC-001](relative/path/to/UC-001/UC-001-Name-v1.0.0.md)'
"""

import os
import re
from pathlib import Path

# Paths
REPO_ROOT = Path(r"D:\Work\BNZ\ai-platform-architecture")
UC_ROOT = REPO_ROOT / "01-motivation" / "03-use-cases" / "use-cases"

def build_uc_lookup():
    """Build a lookup of UC ID to file info."""
    lookup = {}

    for uc_folder in UC_ROOT.iterdir():
        if not uc_folder.is_dir() or not uc_folder.name.startswith('UC-'):
            continue

        uc_id = uc_folder.name
        # Find the main UC markdown file (not README.md)
        md_files = [f for f in uc_folder.glob('UC-*.md') if f.name != 'README.md']

        if md_files:
            md_file = md_files[0]
            # Extract name from filename: UC-NNN-Name-vX.X.X.md
            match = re.match(r'UC-\d+-(.+)-v\d+\.\d+\.\d+\.md', md_file.name)
            name = match.group(1).replace('-', ' ') if match else uc_id

            lookup[uc_id] = {
                'folder': uc_folder.name,
                'filename': md_file.name,
                'name': name,
                'full_path': md_file
            }

    return lookup

def get_relative_path(from_file, to_uc_id, uc_lookup):
    """Calculate the relative path from a file to a UC document."""
    if to_uc_id not in uc_lookup:
        return None

    uc_info = uc_lookup[to_uc_id]
    to_path = uc_info['full_path']

    try:
        # Get the relative path from the source file's directory to the UC file
        from_dir = from_file.parent
        rel_path = os.path.relpath(to_path, from_dir)
        # Convert Windows backslashes to forward slashes for markdown
        rel_path = rel_path.replace('\\', '/')
        return rel_path
    except ValueError:
        # Different drives on Windows
        return None

def process_file(file_path, uc_lookup, dry_run=False):
    """Process a single file to add UC hyperlinks."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return False, 0, "Unicode decode error"

    original_content = content
    replacements = 0

    # Extract UC ID from filename if this is a UC file (to avoid self-references)
    self_uc_id = None
    if file_path.name.startswith('UC-'):
        match = re.match(r'(UC-\d{3})', file_path.name)
        if match:
            self_uc_id = match.group(1)

    # Pattern to match UC IDs that are NOT already in a markdown link
    # Pattern: UC-NNN where NNN is 3 digits
    # Avoid matching if preceded by [ or followed by ]( or if inside a link
    pattern = r'(?<!\[)(?<!/)(UC-\d{3})(?!\]\()(?!\d)'

    def replace_with_link(match):
        nonlocal replacements
        uc_id = match.group(1)

        # Skip self-references
        if uc_id == self_uc_id:
            return match.group(0)

        if uc_id not in uc_lookup:
            return match.group(0)  # Keep original if UC not found

        rel_path = get_relative_path(file_path, uc_id, uc_lookup)
        if rel_path is None:
            return match.group(0)

        replacements += 1
        return f'[{uc_id}]({rel_path})'

    # Don't replace inside code blocks
    # Split content by code blocks and only process non-code parts
    code_block_pattern = r'(```[\s\S]*?```)'
    parts = re.split(code_block_pattern, content)

    processed_parts = []
    for i, part in enumerate(parts):
        if part.startswith('```'):
            # This is a code block, don't process
            processed_parts.append(part)
        else:
            # Process this part
            processed_parts.append(re.sub(pattern, replace_with_link, part))

    content = ''.join(processed_parts)

    if content != original_content and not dry_run:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, replacements, None

    return content != original_content, replacements, None

def process_all_files(uc_lookup, dry_run=False):
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

            updated, count, error = process_file(file_path, uc_lookup, dry_run)

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
    parser = argparse.ArgumentParser(description='Add hyperlinks to UC ID references')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be changed without making changes')
    args = parser.parse_args()

    print("=" * 60)
    print("Use Case Hyperlink Addition Script")
    print("=" * 60)

    if args.dry_run:
        print("\n*** DRY RUN MODE - No changes will be made ***\n")

    # Build UC lookup
    print("\n1. Building Use Case lookup...")
    uc_lookup = build_uc_lookup()
    print(f"   Found {len(uc_lookup)} Use Cases")

    # Show sample
    print("\n   Sample entries:")
    for i, (uc_id, info) in enumerate(list(uc_lookup.items())[:5]):
        print(f"     {uc_id}: {info['name']}")
    print("     ...")

    # Process files
    print("\n2. Processing files...")
    results = process_all_files(uc_lookup, args.dry_run)

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
