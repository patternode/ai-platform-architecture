#!/usr/bin/env python3
"""
Script to remove ABB hyperlinks from inside code blocks (text diagrams).
Converts [AB-NNN](path) back to AB-NNN within code blocks only.
"""

import re
from pathlib import Path

# Paths
REPO_ROOT = Path(r"D:\Work\BNZ\ai-platform-architecture")
PATTERNS_ROOT = REPO_ROOT / "03-building-blocks" / "patterns"

def fix_links_in_code_blocks(file_path):
    """Remove hyperlinks from code blocks in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return False, 0, "Unicode decode error"

    original_content = content
    fixes = 0

    # Pattern to find code blocks
    code_block_pattern = r'```[\s\S]*?```'

    def fix_code_block(match):
        nonlocal fixes
        block = match.group(0)

        # Pattern to match ABB hyperlinks: [AB-NNN](path)
        link_pattern = r'\[AB-(\d{3})\]\([^)]+\)'

        def replace_link(link_match):
            nonlocal fixes
            fixes += 1
            return f'AB-{link_match.group(1)}'

        fixed_block = re.sub(link_pattern, replace_link, block)
        return fixed_block

    content = re.sub(code_block_pattern, fix_code_block, content)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, fixes, None

    return False, 0, None

def main():
    print("=" * 60)
    print("Fix ABB Links in Code Blocks")
    print("=" * 60)

    fixed_files = []
    total_fixes = 0

    # Process all pattern files
    for pattern_folder in PATTERNS_ROOT.iterdir():
        if not pattern_folder.is_dir() or not pattern_folder.name.startswith('PT-'):
            continue

        md_files = list(pattern_folder.glob('PT-*.md'))
        if not md_files:
            continue

        for md_file in md_files:
            fixed, count, error = fix_links_in_code_blocks(md_file)

            if error:
                print(f"  Error: {md_file.name}: {error}")
            elif fixed:
                fixed_files.append((md_file.name, count))
                total_fixes += count
                print(f"  Fixed: {md_file.name} ({count} links removed from code blocks)")

    # Also check ABB files in case they have code block diagrams
    ABB_ROOT = REPO_ROOT / "03-building-blocks" / "architecture-building-blocks" / "abbs"
    for abb_folder in ABB_ROOT.iterdir():
        if not abb_folder.is_dir() or not abb_folder.name.startswith('AB-'):
            continue

        md_files = list(abb_folder.glob('AB-*.md'))
        for md_file in md_files:
            fixed, count, error = fix_links_in_code_blocks(md_file)

            if error:
                print(f"  Error: {md_file.name}: {error}")
            elif fixed:
                fixed_files.append((md_file.name, count))
                total_fixes += count
                print(f"  Fixed: {md_file.name} ({count} links removed from code blocks)")

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Files fixed: {len(fixed_files)}")
    print(f"Total links removed from code blocks: {total_fixes}")
    print("\nDone!")

if __name__ == "__main__":
    main()
