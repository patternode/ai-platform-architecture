#!/usr/bin/env python3
"""
Script to fix self-referential ABB hyperlinks.
Removes links where an ABB ID links to itself within its own document.
"""

import os
import re
from pathlib import Path

# Paths
REPO_ROOT = Path(r"D:\Work\BNZ\ai-platform-architecture")
ABB_ROOT = REPO_ROOT / "03-building-blocks" / "architecture-building-blocks" / "abbs"

def fix_self_links(file_path):
    """Remove self-referential links from an ABB file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return False, 0, "Unicode decode error"

    original_content = content
    fixes = 0

    # Extract ABB ID from the file path (e.g., AB-001 from AB-001/AB-001-Name-v1.0.0.md)
    folder_name = file_path.parent.name
    if not folder_name.startswith('AB-'):
        return False, 0, None

    abb_id = folder_name  # e.g., AB-001

    # Pattern to match self-referential links: [AB-001](AB-001-...) or [AB-001](./AB-001-...)
    # This includes links that reference the file itself
    pattern = rf'\[({re.escape(abb_id)})\]\([^)]*{re.escape(abb_id)}[^)]*\.md\)'

    def replace_with_plain(match):
        nonlocal fixes
        fixes += 1
        return match.group(1)  # Return just the ABB ID without the link

    content = re.sub(pattern, replace_with_plain, content)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, fixes, None

    return False, 0, None

def main():
    print("=" * 60)
    print("Fix Self-Referential ABB Links")
    print("=" * 60)

    fixed_files = []
    total_fixes = 0

    for abb_folder in ABB_ROOT.iterdir():
        if not abb_folder.is_dir() or not abb_folder.name.startswith('AB-'):
            continue

        md_files = list(abb_folder.glob('AB-*.md'))
        if not md_files:
            continue

        md_file = md_files[0]
        fixed, count, error = fix_self_links(md_file)

        if error:
            print(f"  Error: {md_file.name}: {error}")
        elif fixed:
            fixed_files.append((md_file.name, count))
            total_fixes += count
            print(f"  Fixed: {md_file.name} ({count} self-links removed)")

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Files fixed: {len(fixed_files)}")
    print(f"Total self-links removed: {total_fixes}")
    print("\nDone!")

if __name__ == "__main__":
    main()
