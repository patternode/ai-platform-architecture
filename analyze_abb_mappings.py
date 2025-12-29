import re
import csv
from pathlib import Path

# Read all use case files and extract ABB references
uc_abb_mapping = {}

use_case_files = [
    ('UC-001', '01-motivation/03-use-cases/use-cases/UC-001/UC-001-FrontLine-Partnership-Banking-v1.0.0.md'),
    ('UC-002', '01-motivation/03-use-cases/use-cases/UC-002/UC-002-Finance-v1.0.0.md'),
    ('UC-003', '01-motivation/03-use-cases/use-cases/UC-003/UC-003-Analytics-and-Reporting-v1.0.0.md'),
    ('UC-004', '01-motivation/03-use-cases/use-cases/UC-004/UC-004-Credit-Risk-v1.0.0.md'),
    ('UC-005', '01-motivation/03-use-cases/use-cases/UC-005/UC-005-Lending-Ops-v1.0.0.md'),
    ('UC-006', '01-motivation/03-use-cases/use-cases/UC-006/UC-006-HyperPersonalization-v1.0.0.md'),
    ('UC-007', '01-motivation/03-use-cases/use-cases/UC-007/UC-007-Contact-Centre-v1.0.0.md'),
    ('UC-008', '01-motivation/03-use-cases/use-cases/UC-008/UC-008-Security-AI-v1.0.0.md'),
    ('UC-009', '01-motivation/03-use-cases/use-cases/UC-009/UC-009-Data-Products-v1.0.0.md'),
    ('UC-010', '01-motivation/03-use-cases/use-cases/UC-010/UC-010-SDLC-v1.0.0.md'),
    ('UC-011', '01-motivation/03-use-cases/use-cases/UC-011/UC-011-Fincrime-v1.0.0.md'),
    ('UC-012', '01-motivation/03-use-cases/use-cases/UC-012/UC-012-QA-QC-v1.0.0.md'),
    ('UC-013', '01-motivation/03-use-cases/use-cases/UC-013/UC-013-Fraud-Ops-v1.0.0.md'),
    ('UC-014', '01-motivation/03-use-cases/use-cases/UC-014/UC-014-Onboarding-v1.0.0.md'),
    ('UC-015', '01-motivation/03-use-cases/use-cases/UC-015/UC-015-Risk-Functions-v1.0.0.md'),
    ('UC-016', '01-motivation/03-use-cases/use-cases/UC-016/UC-016-IT-Ops-v1.0.0.md'),
    ('UC-017', '01-motivation/03-use-cases/use-cases/UC-017/UC-017-FrontLine---CIB-v1.0.0.md'),
    ('UC-018', '01-motivation/03-use-cases/use-cases/UC-018/UC-018-Procurement-v1.0.0.md'),
    ('UC-019', '01-motivation/03-use-cases/use-cases/UC-019/UC-019-Payment-Disputes-v1.0.0.md'),
    ('UC-020', '01-motivation/03-use-cases/use-cases/UC-020/UC-020-Controls-Testing-v1.0.0.md'),
    ('UC-021', '01-motivation/03-use-cases/use-cases/UC-021/UC-021-Wholesale-Underwriting-v1.0.0.md'),
    ('UC-022', '01-motivation/03-use-cases/use-cases/UC-022/UC-022-Learning-Content-v1.0.0.md'),
    ('UC-023', '01-motivation/03-use-cases/use-cases/UC-023/UC-023-Collection-Management-v1.0.0.md'),
    ('UC-024', '01-motivation/03-use-cases/use-cases/UC-024/UC-024-Front-end-App-Personalisation-v1.0.0.md'),
]

# Extract ABB IDs from each use case
for uc_id, file_path in use_case_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Find ABB IDs in the format AB-nnn or [AB-nnn]
        abb_ids = re.findall(r'AB-\d+', content)
        # Get unique ABB IDs for this use case
        unique_abbs = sorted(set(abb_ids))
        uc_abb_mapping[uc_id] = unique_abbs

# Now build reverse mapping: ABB -> [use cases]
abb_to_ucs = {}
for uc_id, abbs in uc_abb_mapping.items():
    for abb in abbs:
        if abb not in abb_to_ucs:
            abb_to_ucs[abb] = []
        abb_to_ucs[abb].append(uc_id)

# Read the CSV file
csv_data = {}
with open('03-building-blocks/architecture-building-blocks/abbs/abbs.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        abb_id = row['ABB ID'].strip('"')
        use_case_count = int(row['Use Case Count'])
        use_cases = row['Use Cases'].strip('"').split(';') if row['Use Cases'].strip('"') else []
        csv_data[abb_id] = {
            'count': use_case_count,
            'use_cases': sorted(use_cases)
        }

# Compare and find discrepancies
print('=== ANALYSIS RESULTS ===\n')
print('Comparing use case documents with abbs.csv...\n')

discrepancies = []
for abb_id in sorted(set(list(csv_data.keys()) + list(abb_to_ucs.keys()))):
    csv_info = csv_data.get(abb_id, {'count': 0, 'use_cases': []})
    doc_ucs = sorted(abb_to_ucs.get(abb_id, []))
    
    csv_count = csv_info['count']
    csv_ucs = csv_info['use_cases']
    doc_count = len(doc_ucs)
    
    # Check if counts match
    if csv_count != doc_count or set(csv_ucs) != set(doc_ucs):
        discrepancies.append({
            'abb_id': abb_id,
            'csv_count': csv_count,
            'doc_count': doc_count,
            'csv_ucs': csv_ucs,
            'doc_ucs': doc_ucs
        })

if discrepancies:
    print(f'Found {len(discrepancies)} ABBs with discrepancies:\n')
    for disc in discrepancies:
        print(f'{disc["abb_id"]}:')
        print(f'  CSV: count={disc["csv_count"]}, use_cases={disc["csv_ucs"]}')
        print(f'  DOC: count={disc["doc_count"]}, use_cases={disc["doc_ucs"]}')
        
        # Show what's different
        csv_set = set(disc['csv_ucs'])
        doc_set = set(disc['doc_ucs'])
        missing_in_csv = doc_set - csv_set
        extra_in_csv = csv_set - doc_set
        
        if missing_in_csv:
            print(f'  Missing in CSV: {sorted(missing_in_csv)}')
        if extra_in_csv:
            print(f'  Extra in CSV: {sorted(extra_in_csv)}')
        print()
else:
    print('✅ No discrepancies found! All ABB mappings match.')

print(f'\n=== SUMMARY ===')
print(f'Total ABBs in CSV: {len(csv_data)}')
print(f'Total ABBs found in use case docs: {len(abb_to_ucs)}')
print(f'Total discrepancies: {len(discrepancies)}')


