#!/usr/bin/env python3
"""
Script to update ABB IDs in draw.io files from old ABB-XXX-NNN format to new AB-NNN format.
"""

import re
from pathlib import Path

# Paths
REPO_ROOT = Path(r"D:\Work\BNZ\ai-platform-architecture")
PATTERNS_ROOT = REPO_ROOT / "03-building-blocks" / "patterns"

# Mapping from old ABB-XXX-NNN to new AB-NNN
# This was generated during the refactoring process
OLD_TO_NEW_MAPPING = {
    'ABB-AGT-001': 'AB-001',
    'ABB-AGT-002': 'AB-002',
    'ABB-AGT-003': 'AB-003',
    'ABB-AGT-004': 'AB-004',
    'ABB-AGT-005': 'AB-005',
    'ABB-AGT-006': 'AB-006',
    'ABB-AGT-007': 'AB-007',
    'ABB-AGT-008': 'AB-008',
    'ABB-AGT-009': 'AB-009',
    'ABB-AGT-010': 'AB-010',
    'ABB-API-001': 'AB-011',
    'ABB-API-003': 'AB-012',
    'ABB-BAT-001': 'AB-013',
    'ABB-BAT-002': 'AB-014',
    'ABB-BAT-003': 'AB-015',
    'ABB-BAT-004': 'AB-016',
    'ABB-BAT-005': 'AB-017',
    'ABB-BAT-006': 'AB-018',
    'ABB-BAT-007': 'AB-019',
    'ABB-BAT-008': 'AB-020',
    'ABB-BAT-009': 'AB-021',
    'ABB-BAT-010': 'AB-022',
    'ABB-BAT-011': 'AB-023',
    'ABB-CAC-001': 'AB-024',
    'ABB-CMP-001': 'AB-025',
    'ABB-CMP-002': 'AB-026',
    'ABB-CMP-003': 'AB-027',
    'ABB-CMP-004': 'AB-028',
    'ABB-CNV-001': 'AB-029',
    'ABB-CNV-002': 'AB-030',
    'ABB-CNV-003': 'AB-031',
    'ABB-CNV-004': 'AB-032',
    'ABB-CNV-005': 'AB-033',
    'ABB-CNV-006': 'AB-034',
    'ABB-CNV-007': 'AB-035',
    'ABB-CNV-008': 'AB-036',
    'ABB-DAT-001': 'AB-037',
    'ABB-DAT-002': 'AB-038',
    'ABB-DAT-003': 'AB-039',
    'ABB-DOC-001': 'AB-040',
    'ABB-DOC-002': 'AB-041',
    'ABB-DOC-003': 'AB-042',
    'ABB-DSH-001': 'AB-043',
    'ABB-DSH-002': 'AB-044',
    'ABB-DSH-003': 'AB-045',
    'ABB-FAI-001': 'AB-046',
    'ABB-FTR-001': 'AB-047',
    'ABB-FTR-002': 'AB-048',
    'ABB-FTR-003': 'AB-049',
    'ABB-GEN-001': 'AB-050',
    'ABB-GEN-002': 'AB-051',
    'ABB-GEN-003': 'AB-052',
    'ABB-GEN-004': 'AB-053',
    'ABB-GEN-005': 'AB-054',
    'ABB-GEN-006': 'AB-055',
    'ABB-GEN-007': 'AB-056',
    'ABB-GEN-008': 'AB-057',
    'ABB-GEN-009': 'AB-058',
    'ABB-GEN-010': 'AB-059',
    'ABB-GOV-001': 'AB-060',
    'ABB-GOV-002': 'AB-061',
    'ABB-GOV-003': 'AB-062',
    'ABB-GOV-004': 'AB-063',
    'ABB-GOV-005': 'AB-064',
    'ABB-GOV-006': 'AB-065',
    'ABB-GOV-007': 'AB-066',
    'ABB-GOV-008': 'AB-067',
    'ABB-GOV-009': 'AB-068',
    'ABB-GOV-010': 'AB-069',
    'ABB-GOV-011': 'AB-070',
    'ABB-GOV-012': 'AB-071',
    'ABB-INF-001': 'AB-072',
    'ABB-INF-002': 'AB-073',
    'ABB-INT-001': 'AB-074',
    'ABB-INT-002': 'AB-075',
    'ABB-INT-003': 'AB-076',
    'ABB-INT-004': 'AB-077',
    'ABB-INT-005': 'AB-078',
    'ABB-INT-006': 'AB-079',
    'ABB-KNW-001': 'AB-080',
    'ABB-LDB-001': 'AB-081',
    'ABB-MDL-001': 'AB-082',
    'ABB-MDL-002': 'AB-083',
    'ABB-MDL-003': 'AB-084',
    'ABB-MDL-004': 'AB-083',  # Model Fallback Logic - alternate old ID
    'ABB-MDL-005': 'AB-083',  # Model Fallback Logic - alternate old ID
    'ABB-MDL-006': 'AB-083',  # Model Fallback Logic - alternate old ID
    'ABB-MLO-001': 'AB-085',
    'ABB-MLO-002': 'AB-086',
    'ABB-MLO-003': 'AB-087',
    'ABB-MLO-004': 'AB-088',
    'ABB-MLO-005': 'AB-089',
    'ABB-MLO-006': 'AB-090',
    'ABB-MLO-007': 'AB-091',
    'ABB-MLO-008': 'AB-092',
    'ABB-MLO-009': 'AB-093',
    'ABB-NLG-001': 'AB-094',
    'ABB-NLP-001': 'AB-095',
    'ABB-OBS-001': 'AB-096',
    'ABB-OBS-002': 'AB-097',
    'ABB-OBS-003': 'AB-098',
    'ABB-OBS-004': 'AB-099',
    'ABB-OBS-005': 'AB-100',
    'ABB-OBS-006': 'AB-101',
    'ABB-OBS-007': 'AB-102',
    'ABB-OBS-008': 'AB-103',
    'ABB-OBS-009': 'AB-104',
    'ABB-OBS-010': 'AB-105',
    'ABB-OBS-011': 'AB-106',
    'ABB-OBS-012': 'AB-107',
    'ABB-RTE-001': 'AB-108',
    'ABB-RTE-002': 'AB-109',
    'ABB-RTE-003': 'AB-110',
    'ABB-RTE-004': 'AB-111',
    'ABB-SEC-001': 'AB-112',
    'ABB-SEC-002': 'AB-113',
    'ABB-SEC-003': 'AB-114',
    'ABB-SEC-004': 'AB-115',
    'ABB-SEC-005': 'AB-116',
    'ABB-SEC-006': 'AB-117',
    'ABB-SEC-007': 'AB-118',
    'ABB-SEC-008': 'AB-119',
    'ABB-SEC-009': 'AB-120',
    'ABB-SEC-010': 'AB-121',
    'ABB-SEC-011': 'AB-122',
    'ABB-SEC-012': 'AB-123',
    'ABB-SEC-013': 'AB-124',
    'ABB-SEC-014': 'AB-125',
    'ABB-STR-001': 'AB-126',
    'ABB-VAL-001': 'AB-127',
    'ABB-VIS-001': 'AB-128',
    'ABB-WFL-001': 'AB-129',
}

def update_drawio_file(file_path):
    """Update ABB IDs in a draw.io file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return False, 0, "Unicode decode error"

    original_content = content
    replacements = 0

    # Sort by length (longest first) to avoid partial replacements
    for old_id, new_id in sorted(OLD_TO_NEW_MAPPING.items(), key=lambda x: len(x[0]), reverse=True):
        if old_id in content:
            count = content.count(old_id)
            content = content.replace(old_id, new_id)
            replacements += count

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, replacements, None

    return False, 0, None

def main():
    print("=" * 60)
    print("Update ABB IDs in Draw.io Files")
    print("=" * 60)

    updated_files = []
    errors = []
    total_replacements = 0

    for pattern_folder in sorted(PATTERNS_ROOT.iterdir()):
        if not pattern_folder.is_dir() or not pattern_folder.name.startswith('PT-'):
            continue

        drawio_files = list(pattern_folder.glob('*.drawio'))

        for drawio_file in drawio_files:
            updated, count, error = update_drawio_file(drawio_file)

            if error:
                errors.append((drawio_file.name, error))
                print(f"  Error: {drawio_file.name}: {error}")
            elif updated:
                updated_files.append((drawio_file.name, count))
                total_replacements += count
                print(f"  Updated: {drawio_file.name} ({count} replacements)")
            else:
                print(f"  Skipped (no changes): {drawio_file.name}")

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Files updated: {len(updated_files)}")
    print(f"Total replacements: {total_replacements}")
    print(f"Errors: {len(errors)}")

    print("\nDone!")

if __name__ == "__main__":
    main()
