#!/usr/bin/env python3
"""
Script to remove "Wave Assignment: ..." text at the end of use case documents.
"""

import re
from pathlib import Path

# Paths
REPO_ROOT = Path(r"D:\Work\BNZ\ai-platform-architecture")
UC_ROOT = REPO_ROOT / "01-motivation" / "03-use-cases" / "use-cases"

def remove_wave_assignment(file_path):
    """Remove Wave Assignment line from end of file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return False, "Unicode decode error"

    original_content = content

    # Remove various patterns of Wave Assignment at end of file
    patterns = [
        r'\n+\*\*Wave Assignment\*\*:[^\n]*\n*$',
        r'\n+Wave Assignment:[^\n]*\n*$',
    ]

    for pattern in patterns:
        content = re.sub(pattern, '\n', content)

    # Clean up trailing whitespace
    content = content.rstrip() + '\n'

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, None

    return False, None

def main():
    print("=" * 60)
    print("Remove Wave Assignment from Use Cases")
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
            updated, error = remove_wave_assignment(md_file)

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
