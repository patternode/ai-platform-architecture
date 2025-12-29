#!/usr/bin/env python3
"""
Script to fix Architecture Patterns tables in Use Case documents.
- Remove the "View Pattern" or "Reference" link column
- Ensure proper table header
- Keep Pattern ID, Pattern Name, Usage columns
"""

import re
from pathlib import Path

# Paths
REPO_ROOT = Path(r"D:\Work\BNZ\ai-platform-architecture")
UC_ROOT = REPO_ROOT / "01-motivation" / "03-use-cases" / "use-cases"

def fix_pattern_table(content):
    """Fix the Primary Patterns Used table."""

    # Pattern to find Primary Patterns Used section and its table
    # Match the section and the table rows

    # First, let's find tables that have View Pattern or Reference columns
    # and remove those columns

    # Pattern for rows with 4 columns ending in a link (View Pattern or Reference)
    # Example: | [PT-008](...) | Multi-Agent Orchestration | [View Pattern](...) |
    pattern_3col = r'\| (\[PT-\d{3}\]\([^)]+\)) \| ([^|]+) \| \[(?:View Pattern|PT-\d{3}[^\]]*)\]\([^)]+\) \|'

    def replace_3col(match):
        pattern_id = match.group(1)
        pattern_name = match.group(2).strip()
        return f'| {pattern_id} | {pattern_name} |'

    content = re.sub(pattern_3col, replace_3col, content)

    # Pattern for rows with 4 columns: Pattern ID | Pattern Name | Usage | Reference
    # Example: | [PT-005](...) | RAG | Knowledge retrieval | [PT-005-...](...) |
    pattern_4col = r'\| (\[PT-\d{3}\]\([^)]+\)) \| ([^|]+) \| ([^|]+) \| \[PT-\d{3}[^\]]*\]\([^)]+\) \|'

    def replace_4col(match):
        pattern_id = match.group(1)
        pattern_name = match.group(2).strip()
        usage = match.group(3).strip()
        return f'| {pattern_id} | {pattern_name} | {usage} |'

    content = re.sub(pattern_4col, replace_4col, content)

    # Fix header rows - remove Reference column from headers
    # | Pattern ID | Pattern Name | Usage in Use Case | Reference |
    content = re.sub(
        r'\| Pattern ID \| Pattern Name \| Usage in Use Case \| Reference \|',
        '| Pattern ID | Pattern Name | Usage in Use Case |',
        content
    )

    # Fix separator rows - remove extra column
    # |-----------|-------------|-------------------|-----------|
    content = re.sub(
        r'\|[-]+\|[-]+\|[-]+\|[-]+\|(\n\| \[PT)',
        '|------------|--------------|-------------------|\\1',
        content
    )

    # Also need to add header row if missing
    # Find tables that start with | [PT-xxx] and don't have a header
    # Look for "Primary Patterns Used" followed by empty lines and then table without header

    def add_header_if_missing(match):
        section = match.group(0)
        # Check if it already has a header row
        if '| Pattern ID |' in section:
            return section

        # Find where the table starts (first | [PT- line)
        lines = section.split('\n')
        new_lines = []
        header_added = False

        for line in lines:
            if not header_added and line.strip().startswith('| [PT-'):
                # Count columns in this row
                col_count = line.count('|') - 1
                if col_count == 2:
                    # 2 columns: Pattern ID | Pattern Name
                    new_lines.append('| Pattern ID | Pattern Name |')
                    new_lines.append('|------------|--------------|')
                elif col_count == 3:
                    # 3 columns: Pattern ID | Pattern Name | Usage
                    new_lines.append('| Pattern ID | Pattern Name | Usage in Use Case |')
                    new_lines.append('|------------|--------------|-------------------|')
                header_added = True
            new_lines.append(line)

        return '\n'.join(new_lines)

    # Apply header fix to Primary Patterns Used sections
    pattern_section = r'\*\*Primary Patterns Used\*\*:\n\n(?:\| \[PT-[^\n]+\n)+'
    content = re.sub(pattern_section, add_header_if_missing, content)

    return content

def process_use_case(file_path):
    """Process a single use case file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return False, "Unicode decode error"

    original_content = content
    content = fix_pattern_table(content)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, None

    return False, None

def main():
    print("=" * 60)
    print("Fix Architecture Patterns Tables")
    print("=" * 60)

    updated_files = []
    errors = []

    for uc_folder in sorted(UC_ROOT.iterdir()):
        if not uc_folder.is_dir() or not uc_folder.name.startswith('UC-'):
            continue

        md_files = [f for f in uc_folder.glob('UC-*.md') if f.name != 'README.md']

        if not md_files:
            continue

        for md_file in md_files:
            updated, error = process_use_case(md_file)

            if error:
                errors.append((md_file.name, error))
                print(f"  Error: {md_file.name}: {error}")
            elif updated:
                updated_files.append(md_file.name)
                print(f"  Updated: {md_file.name}")
            else:
                print(f"  Skipped (no changes): {md_file.name}")

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Files updated: {len(updated_files)}")
    print(f"Errors: {len(errors)}")

    print("\nDone!")

if __name__ == "__main__":
    main()
