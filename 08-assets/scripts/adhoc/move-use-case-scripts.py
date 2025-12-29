"""
Move Use Case Scripts

This script moves all script files (.py, .bat, .ps1, .sh) from
01-motivation/03-use-cases to 08-assets/scripts/use-cases,
preserving the directory structure.

Usage:
    python move-use-case-scripts.py [--dry-run]

Options:
    --dry-run   Show what would be moved without actually moving files
"""

import os
import shutil
import argparse
from pathlib import Path


def find_scripts(source_dir: Path) -> list[Path]:
    """Find all script files in the source directory."""
    script_extensions = {'.py', '.bat', '.ps1', '.sh'}
    scripts = []

    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if Path(file).suffix.lower() in script_extensions:
                scripts.append(Path(root) / file)

    return scripts


def move_scripts(source_base: Path, dest_base: Path, dry_run: bool = False) -> dict:
    """
    Move scripts from source to destination, preserving relative structure.

    Returns a dict with counts and details of operations performed.
    """
    results = {
        'moved': [],
        'skipped': [],
        'errors': [],
        'directories_created': []
    }

    scripts = find_scripts(source_base)

    if not scripts:
        print(f"No scripts found in {source_base}")
        return results

    print(f"Found {len(scripts)} script(s) to move:\n")

    for script_path in sorted(scripts):
        # Calculate relative path from source base
        relative_path = script_path.relative_to(source_base)
        dest_path = dest_base / relative_path

        print(f"  Source: {script_path}")
        print(f"  Dest:   {dest_path}")

        if dry_run:
            print("  [DRY RUN - would move]\n")
            results['moved'].append((script_path, dest_path))
            continue

        try:
            # Create destination directory if needed
            dest_dir = dest_path.parent
            if not dest_dir.exists():
                dest_dir.mkdir(parents=True, exist_ok=True)
                results['directories_created'].append(dest_dir)
                print(f"  Created directory: {dest_dir}")

            # Check if destination already exists
            if dest_path.exists():
                print(f"  [SKIPPED - destination exists]\n")
                results['skipped'].append((script_path, dest_path))
                continue

            # Move the file
            shutil.move(str(script_path), str(dest_path))
            print(f"  [MOVED]\n")
            results['moved'].append((script_path, dest_path))

        except Exception as e:
            print(f"  [ERROR: {e}]\n")
            results['errors'].append((script_path, str(e)))

    return results


def cleanup_empty_dirs(source_base: Path, dry_run: bool = False) -> list[Path]:
    """Remove empty directories after moving scripts."""
    removed = []

    # Walk bottom-up to remove empty directories
    for root, dirs, files in os.walk(source_base, topdown=False):
        root_path = Path(root)

        # Skip if it's a 'scripts' directory that might now be empty
        if root_path.name == 'scripts' or 'scripts' in str(root_path):
            # Check if directory is empty
            try:
                if not any(root_path.iterdir()):
                    if dry_run:
                        print(f"  [DRY RUN] Would remove empty directory: {root_path}")
                    else:
                        root_path.rmdir()
                        print(f"  Removed empty directory: {root_path}")
                    removed.append(root_path)
            except (OSError, PermissionError) as e:
                print(f"  Could not remove {root_path}: {e}")

    return removed


def print_summary(results: dict, dry_run: bool):
    """Print a summary of operations."""
    print("\n" + "=" * 60)
    print("SUMMARY" + (" (DRY RUN)" if dry_run else ""))
    print("=" * 60)
    print(f"  Scripts moved:     {len(results['moved'])}")
    print(f"  Scripts skipped:   {len(results['skipped'])}")
    print(f"  Errors:            {len(results['errors'])}")
    print(f"  Directories created: {len(results['directories_created'])}")

    if results['errors']:
        print("\nErrors encountered:")
        for path, error in results['errors']:
            print(f"  - {path}: {error}")


def main():
    parser = argparse.ArgumentParser(
        description='Move use case scripts to 08-assets/scripts/use-cases'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be moved without actually moving files'
    )
    args = parser.parse_args()

    # Define paths
    repo_root = Path(__file__).parent.parent.parent.parent  # Navigate up from adhoc folder
    source_base = repo_root / '01-motivation' / '03-use-cases'
    dest_base = repo_root / '08-assets' / 'scripts' / 'use-cases'

    print("=" * 60)
    print("Move Use Case Scripts")
    print("=" * 60)
    print(f"Repository root: {repo_root}")
    print(f"Source:          {source_base}")
    print(f"Destination:     {dest_base}")
    print(f"Mode:            {'DRY RUN' if args.dry_run else 'LIVE'}")
    print("=" * 60 + "\n")

    # Validate paths
    if not source_base.exists():
        print(f"ERROR: Source directory does not exist: {source_base}")
        return 1

    # Create destination if it doesn't exist
    if not args.dry_run:
        dest_base.mkdir(parents=True, exist_ok=True)

    # Move scripts
    results = move_scripts(source_base, dest_base, dry_run=args.dry_run)

    # Cleanup empty directories
    if results['moved'] and not args.dry_run:
        print("\nCleaning up empty directories...")
        cleanup_empty_dirs(source_base, dry_run=args.dry_run)

    # Print summary
    print_summary(results, args.dry_run)

    return 0 if not results['errors'] else 1


if __name__ == '__main__':
    exit(main())
