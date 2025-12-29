#!/usr/bin/env python3
"""
Script: update-pattern-links.py
Purpose: Update pattern references in use case markdown files to use relative links
         to the new pattern folder structure.
Author: BNZ Enterprise Architecture
Date: 2025-12-06
"""

import os
import re
from pathlib import Path

# Configuration
USE_CASES_DIR = Path(r"D:\Work\BNZ\ai-platform-architecture\01-motivation\03-use-cases\use-cases")
PATTERNS_DIR = Path(r"D:\Work\BNZ\ai-platform-architecture\03-building-blocks\patterns")

# Pattern mapping: PT-XXX -> markdown filename
PATTERN_FILES = {
    "PT-001": "PT-001/PT-001-Enterprise-AI-Governance-v1.0.0.md",
    "PT-002": "PT-002/PT-002-MLOps-Level-2-Plus-v1.0.0.md",
    "PT-003": "PT-003/PT-003-Feature-Store-v1.0.0.md",
    "PT-004": "PT-004/PT-004-Explainability-v1.0.0.md",
    "PT-005": "PT-005/PT-005-Retrieval-Augmented-Generation-v1.0.0.md",
    "PT-006": "PT-006/PT-006-Multi-Model-Routing-v1.0.0.md",
    "PT-007": "PT-007/PT-007-Agentic-AI-v1.0.0.md",
    "PT-008": "PT-008/PT-008-Multi-Agent-Orchestration-v1.0.0.md",
    "PT-009": "PT-009/PT-009-Real-Time-Scoring-v1.0.0.md",
    "PT-010": "PT-010/PT-010-Champion-Challenger-v1.0.0.md",
    "PT-011": "PT-011/PT-011-Intelligent-Document-Processing-v1.0.0.md",
    "PT-012": "PT-012/PT-012-Data-Mesh-v1.0.0.md",
    "PT-013": "PT-013/PT-013-Conversational-AI-v1.0.0.md",
    "PT-014": "PT-014/PT-014-Batch-Prediction-v1.0.0.md",
    "PT-015": "PT-015/PT-015-Event-Driven-Architecture-v1.0.0.md",
    "PT-016": "PT-016/PT-016-Stream-Processing-v1.0.0.md",
    "PT-017": "PT-017/PT-017-Observability-Monitoring-v1.0.0.md",
    "PT-018": "PT-018/PT-018-Security-Privacy-v1.0.0.md",
}

# Relative path from use-cases/UC-XXX/ to patterns folder
RELATIVE_PATH = "../../../../03-building-blocks/patterns"

# Pattern names for display
PATTERN_NAMES = {
    "PT-001": "Enterprise AI Governance",
    "PT-002": "MLOps Level 2+",
    "PT-003": "Feature Store",
    "PT-004": "ML Explainability",
    "PT-005": "Retrieval-Augmented Generation",
    "PT-006": "Multi-Model Routing",
    "PT-007": "Agentic AI",
    "PT-008": "Multi-Agent Orchestration",
    "PT-009": "Real-Time Scoring",
    "PT-010": "Champion-Challenger",
    "PT-011": "Intelligent Document Processing",
    "PT-012": "Data Mesh",
    "PT-013": "Conversational AI",
    "PT-014": "Batch Prediction",
    "PT-015": "Event-Driven Architecture",
    "PT-016": "Stream Processing",
    "PT-017": "Observability & Monitoring",
    "PT-018": "Security & Privacy",
}

def get_pattern_link(pattern_id):
    """Generate the relative link for a pattern."""
    if pattern_id in PATTERN_FILES:
        return f"{RELATIVE_PATH}/{PATTERN_FILES[pattern_id]}"
    return None

def update_file(filepath):
    """Update pattern references in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    changes = []

    # Pattern 1: Update old-style links like [PT-005-...md](../patterns/PT-005-...md)
    # to new structure
    old_link_pattern = r'\[([^\]]+)\]\(\.\.\/patterns\/(PT-\d{3})[^\)]+\.md\)'
    def replace_old_link(match):
        link_text = match.group(1)
        pattern_id = match.group(2)
        new_link = get_pattern_link(pattern_id)
        if new_link:
            changes.append(f"  Updated old link: {pattern_id}")
            return f"[{link_text}]({new_link})"
        return match.group(0)

    content = re.sub(old_link_pattern, replace_old_link, content)

    # Pattern 2: Table rows with "See patterns/PT-XXX-*.md" format
    # e.g., | PT-008 | [Pattern Name] | See patterns/PT-008-*.md |
    see_pattern = r'\|\s*(PT-0[0-9]{2})\s*\|\s*\[Pattern Name\]\s*\|\s*See patterns\/PT-\d{3}-\*\.md\s*\|'

    def replace_see_pattern(match):
        pattern_id = match.group(1)
        new_link = get_pattern_link(pattern_id)
        if new_link and pattern_id in PATTERN_NAMES:
            pattern_name = PATTERN_NAMES[pattern_id]
            changes.append(f"  Updated See pattern: {pattern_id}")
            return f"| [{pattern_id}]({new_link}) | {pattern_name} | [View Pattern]({new_link}) |"
        return match.group(0)

    content = re.sub(see_pattern, replace_see_pattern, content)

    # Pattern 3: Plain text pattern references like "(PT-001)" not already in a link
    # Match patterns like "Platform (PT-001)" but not if already in a markdown link
    plain_ref_pattern = r'(?<!\[)(?<!\()(\b[A-Za-z][A-Za-z0-9\s&\-]+)\s*\((PT-0[0-9]{2})\)(?!\])'

    def replace_plain_ref(match):
        text_before = match.group(1).strip()
        pattern_id = match.group(2)
        new_link = get_pattern_link(pattern_id)
        if new_link:
            changes.append(f"  Linked plain ref: {pattern_id}")
            return f"[{text_before} ({pattern_id})]({new_link})"
        return match.group(0)

    content = re.sub(plain_ref_pattern, replace_plain_ref, content)

    # Pattern 4: Table entries with pattern IDs like "| PT-001 |" (not already linked)
    table_pattern = r'\|\s*(PT-0[0-9]{2})\s*\|(?!\s*\[)'

    def replace_table_pattern(match):
        pattern_id = match.group(1)
        new_link = get_pattern_link(pattern_id)
        if new_link:
            changes.append(f"  Linked table entry: {pattern_id}")
            return f"| [{pattern_id}]({new_link}) |"
        return match.group(0)

    content = re.sub(table_pattern, replace_table_pattern, content)

    # Pattern 5: References like "PT-001:" at start of text (not already linked)
    colon_pattern = r'(?<!\[)(PT-0[0-9]{2}):\s*'

    def replace_colon_ref(match):
        pattern_id = match.group(1)
        new_link = get_pattern_link(pattern_id)
        if new_link:
            changes.append(f"  Linked colon ref: {pattern_id}")
            return f"[{pattern_id}]({new_link}): "
        return match.group(0)

    content = re.sub(colon_pattern, replace_colon_ref, content)

    # Pattern 6: Standalone PT-XXX in list items like "- PT-001" or "* PT-001"
    list_pattern = r'^(\s*[-*]\s*)(PT-0[0-9]{2})(\s|$)'

    def replace_list_pattern(match):
        prefix = match.group(1)
        pattern_id = match.group(2)
        suffix = match.group(3)
        new_link = get_pattern_link(pattern_id)
        if new_link:
            changes.append(f"  Linked list item: {pattern_id}")
            return f"{prefix}[{pattern_id}]({new_link}){suffix}"
        return match.group(0)

    content = re.sub(list_pattern, replace_list_pattern, content, flags=re.MULTILINE)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    return []

def main():
    print("=" * 70)
    print("Update Pattern Links in Use Case Markdown Files")
    print("=" * 70)
    print()

    total_files = 0
    total_changes = 0

    # Process each use case folder
    for uc_folder in sorted(USE_CASES_DIR.iterdir()):
        if uc_folder.is_dir() and uc_folder.name.startswith("UC-"):
            # Find markdown files in the use case folder
            for md_file in uc_folder.glob("*.md"):
                changes = update_file(md_file)
                if changes:
                    total_files += 1
                    total_changes += len(changes)
                    print(f"{md_file.name}:")
                    for change in changes:
                        print(change)
                    print()

    # Also update README.md in use-cases folder
    readme_path = USE_CASES_DIR / "README.md"
    if readme_path.exists():
        changes = update_file(readme_path)
        if changes:
            total_files += 1
            total_changes += len(changes)
            print(f"README.md:")
            for change in changes:
                print(change)
            print()

    print("=" * 70)
    print(f"Summary: Updated {total_changes} references in {total_files} files")
    print("=" * 70)

if __name__ == "__main__":
    main()
