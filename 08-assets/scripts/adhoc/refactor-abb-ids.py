#!/usr/bin/env python3
"""
Script to refactor ABB IDs from ABB-XXX-NNN format to AB-NNN format.
This includes:
1. Creating a mapping from old to new IDs
2. Renaming folders and files
3. Updating all references across the repository
"""

import os
import re
import csv
import shutil
from pathlib import Path
from collections import OrderedDict

# Paths
REPO_ROOT = Path(r"D:\Work\BNZ\ai-platform-architecture")
ABB_ROOT = REPO_ROOT / "03-building-blocks" / "architecture-building-blocks" / "abbs"
CAPS_CSV_PATH = REPO_ROOT / "02-capabilities" / "capabilities-consolidated.csv"
PATTERNS_CSV_PATH = REPO_ROOT / "03-building-blocks" / "patterns" / "patterns-consolidated.csv"
USE_CASES_ROOT = REPO_ROOT / "01-motivation" / "03-use-cases" / "use-cases"
SCRIPTS_ROOT = REPO_ROOT / "08-assets" / "scripts" / "adhoc"

# Generate mapping
def generate_id_mapping():
    """Generate mapping from old ABB-XXX-NNN IDs to new AB-NNN IDs."""
    mapping = OrderedDict()

    # Find all existing ABB folders
    abb_folders = sorted([d for d in ABB_ROOT.iterdir() if d.is_dir() and d.name.startswith('ABB-')])

    # Assign sequential numbers
    for idx, folder in enumerate(abb_folders, start=1):
        old_id = folder.name  # e.g., AB-001
        new_id = f"AB-{idx:03d}"  # e.g., AB-001
        mapping[old_id] = new_id

    return mapping

def save_mapping_csv(mapping, output_path):
    """Save the ID mapping to a CSV file for reference."""
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Old_ID', 'New_ID', 'Category', 'Name'])
        for old_id, new_id in mapping.items():
            # Extract category and name from old ID
            parts = old_id.split('-')
            category = parts[1] if len(parts) > 1 else ''

            # Try to get the name from the folder contents
            folder_path = ABB_ROOT / old_id
            name = ''
            if folder_path.exists():
                md_files = list(folder_path.glob('*.md'))
                if md_files:
                    # Extract name from filename: ABB-XXX-NNN-Name-vX.X.X.md
                    filename = md_files[0].stem  # Remove .md
                    match = re.match(r'ABB-[A-Z]+-\d+-(.+)-v\d+\.\d+\.\d+', filename)
                    if match:
                        name = match.group(1).replace('-', ' ')

            writer.writerow([old_id, new_id, category, name])

def rename_folders_and_files(mapping):
    """Rename ABB folders and their contained markdown files."""
    renamed = []
    errors = []

    for old_id, new_id in mapping.items():
        old_folder = ABB_ROOT / old_id
        new_folder = ABB_ROOT / new_id

        if not old_folder.exists():
            errors.append(f"Folder not found: {old_folder}")
            continue

        # Find the markdown file
        md_files = list(old_folder.glob('ABB-*.md'))
        if not md_files:
            errors.append(f"No markdown file found in: {old_folder}")
            continue

        old_md = md_files[0]
        # Generate new filename: AB-NNN-Name-vX.X.X.md
        old_filename = old_md.name
        # Extract name and version from old filename
        match = re.match(r'ABB-[A-Z]+-\d+-(.+)-(v\d+\.\d+\.\d+\.md)', old_filename)
        if match:
            name_part = match.group(1)
            version_part = match.group(2)
            new_filename = f"{new_id}-{name_part}-{version_part}"
        else:
            errors.append(f"Could not parse filename: {old_filename}")
            continue

        try:
            # Rename the markdown file first
            new_md = old_folder / new_filename
            old_md.rename(new_md)

            # Rename the folder
            old_folder.rename(new_folder)

            renamed.append((old_id, new_id, old_filename, new_filename))
        except Exception as e:
            errors.append(f"Error renaming {old_id}: {e}")

    return renamed, errors

def update_file_content(file_path, mapping):
    """Update all ABB ID references in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return False, "Unicode decode error"

    original_content = content

    # Replace all old IDs with new IDs
    # Sort by length (longest first) to avoid partial replacements
    for old_id, new_id in sorted(mapping.items(), key=lambda x: len(x[0]), reverse=True):
        # Replace the full ID pattern (ABB-XXX-NNN)
        content = content.replace(old_id, new_id)

    # Also update patterns like "ABB ID" -> keep as "ABB ID" but value should be new format
    # And update any "Short Name" references

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, None

    return False, None

def update_all_references(mapping):
    """Update all references across the repository."""
    updated_files = []
    errors = []

    # Patterns to search for files that might contain ABB references
    file_patterns = [
        ('03-building-blocks/**/*.md', 'Building blocks'),
        ('01-motivation/**/*.md', 'Use cases'),
        ('02-capabilities/**/*.csv', 'Capabilities CSV'),
        ('03-building-blocks/**/*.csv', 'Patterns CSV'),
        ('08-assets/scripts/**/*.py', 'Python scripts'),
        ('05-governance/**/*.md', 'Governance docs'),
    ]

    for pattern, description in file_patterns:
        print(f"\nProcessing {description}...")
        for file_path in REPO_ROOT.glob(pattern):
            if file_path.is_file():
                updated, error = update_file_content(file_path, mapping)
                if updated:
                    updated_files.append((str(file_path.relative_to(REPO_ROOT)), description))
                    print(f"  Updated: {file_path.name}")
                if error:
                    errors.append((str(file_path), error))

    return updated_files, errors

def update_abb_file_headers(mapping):
    """Update the ABB ID in the document control section of each ABB file."""
    updated = []

    for old_id, new_id in mapping.items():
        new_folder = ABB_ROOT / new_id
        if not new_folder.exists():
            continue

        md_files = list(new_folder.glob('AB-*.md'))
        if not md_files:
            continue

        md_file = md_files[0]

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Update the ABB ID in document control table
            # Pattern: | **ABB ID** | `ABB-XXX-NNN` |
            content = re.sub(
                r'\| \*\*ABB ID\*\* \| `' + re.escape(old_id) + r'` \|',
                f'| **ABB ID** | `{new_id}` |',
                content
            )

            # Also update any remaining references to the old ID format
            content = content.replace(old_id, new_id)

            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)

            updated.append(new_id)
        except Exception as e:
            print(f"Error updating {md_file}: {e}")

    return updated

def main():
    print("=" * 60)
    print("ABB ID Refactoring Script")
    print("=" * 60)

    # Step 1: Generate mapping
    print("\n1. Generating ID mapping...")
    mapping = generate_id_mapping()
    print(f"   Generated mapping for {len(mapping)} ABBs")

    # Save mapping for reference
    mapping_path = REPO_ROOT / "03-building-blocks" / "architecture-building-blocks" / "abb-id-mapping.csv"
    save_mapping_csv(mapping, mapping_path)
    print(f"   Saved mapping to: {mapping_path}")

    # Print sample of mapping
    print("\n   Sample mapping:")
    for i, (old_id, new_id) in enumerate(list(mapping.items())[:10]):
        print(f"     {old_id} -> {new_id}")
    print("     ...")

    # Step 2: Rename folders and files
    print("\n2. Renaming folders and files...")
    renamed, rename_errors = rename_folders_and_files(mapping)
    print(f"   Renamed {len(renamed)} ABB folders/files")
    if rename_errors:
        print(f"   Errors: {len(rename_errors)}")
        for err in rename_errors[:5]:
            print(f"     - {err}")

    # Step 3: Update all references
    print("\n3. Updating all references in repository...")
    updated_files, update_errors = update_all_references(mapping)
    print(f"   Updated {len(updated_files)} files")
    if update_errors:
        print(f"   Errors: {len(update_errors)}")
        for path, err in update_errors[:5]:
            print(f"     - {path}: {err}")

    # Step 4: Update ABB file headers
    print("\n4. Updating ABB file headers...")
    updated_headers = update_abb_file_headers(mapping)
    print(f"   Updated headers in {len(updated_headers)} ABB files")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total ABBs processed: {len(mapping)}")
    print(f"Folders/files renamed: {len(renamed)}")
    print(f"Files updated with new references: {len(updated_files)}")
    print(f"ABB headers updated: {len(updated_headers)}")

    if rename_errors or update_errors:
        print(f"\nTotal errors: {len(rename_errors) + len(update_errors)}")

    print(f"\nMapping saved to: {mapping_path}")
    print("\nDone!")

if __name__ == "__main__":
    main()
