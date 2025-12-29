#!/usr/bin/env python3
"""
Script to update sections 2.2 (Functional Requirements) and 2.3 (Non-Functional Requirements)
in all ABB files based on ABB category and capabilities.
"""

import csv
import re
from pathlib import Path
from collections import defaultdict

# Paths
REPO_ROOT = Path(r"D:\Work\BNZ\ai-platform-architecture")
CSV_PATH = REPO_ROOT / "02-capabilities" / "capabilities-consolidated.csv"
ABB_ROOT = REPO_ROOT / "03-building-blocks" / "architecture-building-blocks" / "abbs"

# ABB category to functional requirements mapping
CATEGORY_FUNCTIONAL_REQUIREMENTS = {
    'AGT': [
        ('FR-001', 'Agent Lifecycle Management', 'Manage agent creation, configuration, and termination', 'Agents can be started, stopped, and configured via API'),
        ('FR-002', 'Task Orchestration', 'Coordinate multi-step task execution across agents', 'Complex tasks decomposed and executed with proper sequencing'),
        ('FR-003', 'State Management', 'Maintain agent state and conversation context', 'State persists across interactions and recovers from failures'),
        ('FR-004', 'Tool Integration', 'Enable agents to invoke registered tools and APIs', 'Agents can successfully call and receive results from tools'),
    ],
    'GEN': [
        ('FR-001', 'Model Invocation', 'Invoke LLM models with prompts and retrieve responses', 'Responses returned within latency SLA with proper formatting'),
        ('FR-002', 'Prompt Management', 'Support prompt templates and variable substitution', 'Prompts rendered correctly with injected context'),
        ('FR-003', 'Response Streaming', 'Support streaming responses for real-time output', 'Tokens streamed as generated with <500ms time-to-first-token'),
        ('FR-004', 'Context Management', 'Handle conversation context and token limits', 'Context truncated intelligently when approaching limits'),
    ],
    'SEC': [
        ('FR-001', 'Authentication', 'Verify identity of users and services', 'Valid credentials authenticated, invalid rejected with audit log'),
        ('FR-002', 'Authorization', 'Enforce role-based and attribute-based access control', 'Access granted/denied based on policies with proper logging'),
        ('FR-003', 'Encryption', 'Encrypt data at rest and in transit', 'All sensitive data encrypted with approved algorithms'),
        ('FR-004', 'Audit Logging', 'Record security events for compliance', 'All security events logged with timestamps and context'),
    ],
    'GOV': [
        ('FR-001', 'Policy Enforcement', 'Enforce governance policies on AI operations', 'Policy violations detected and blocked or flagged'),
        ('FR-002', 'Compliance Monitoring', 'Monitor AI systems for regulatory compliance', 'Compliance status tracked and reported in real-time'),
        ('FR-003', 'Audit Trail', 'Maintain comprehensive audit trail of AI decisions', 'All decisions traceable with full context and rationale'),
        ('FR-004', 'Risk Assessment', 'Assess and score AI model risk levels', 'Risk scores calculated and updated based on model behavior'),
    ],
    'OBS': [
        ('FR-001', 'Metrics Collection', 'Collect and aggregate system and business metrics', 'Metrics collected at configured intervals with <1% data loss'),
        ('FR-002', 'Alerting', 'Generate alerts based on threshold breaches', 'Alerts triggered within 60 seconds of threshold breach'),
        ('FR-003', 'Visualization', 'Provide dashboards and visualizations for metrics', 'Dashboards render within 3 seconds with real-time updates'),
        ('FR-004', 'Anomaly Detection', 'Detect anomalies in metrics and logs', 'Anomalies detected with configurable sensitivity'),
    ],
    'MLO': [
        ('FR-001', 'Pipeline Orchestration', 'Orchestrate ML training and deployment pipelines', 'Pipelines execute in correct sequence with dependency handling'),
        ('FR-002', 'Experiment Tracking', 'Track experiments, parameters, and results', 'All experiment metadata captured and queryable'),
        ('FR-003', 'Model Versioning', 'Version control for models and artifacts', 'Models versioned with lineage to training data and code'),
        ('FR-004', 'Automated Retraining', 'Trigger model retraining based on drift or schedule', 'Retraining initiated within configured triggers'),
    ],
    'DAT': [
        ('FR-001', 'Data Ingestion', 'Ingest data from multiple sources', 'Data ingested with schema validation and error handling'),
        ('FR-002', 'Data Storage', 'Store data with appropriate partitioning and indexing', 'Data stored with query performance meeting SLAs'),
        ('FR-003', 'Data Retrieval', 'Retrieve data with filtering and aggregation', 'Queries return results within latency requirements'),
        ('FR-004', 'Data Versioning', 'Maintain versions of datasets for reproducibility', 'Data versions tracked with point-in-time recovery'),
    ],
    'FTR': [
        ('FR-001', 'Feature Computation', 'Compute features from raw data', 'Features computed with defined transformations'),
        ('FR-002', 'Feature Storage', 'Store features for training and serving', 'Features available for both batch and real-time access'),
        ('FR-003', 'Feature Serving', 'Serve features with low latency for inference', 'Features served within <10ms p99 latency'),
        ('FR-004', 'Feature Consistency', 'Ensure training-serving consistency', 'Same feature values for training and inference'),
    ],
    'INF': [
        ('FR-001', 'Model Loading', 'Load and initialize models for inference', 'Models loaded and ready within startup time SLA'),
        ('FR-002', 'Inference Execution', 'Execute model inference on input data', 'Predictions returned within latency SLA'),
        ('FR-003', 'Batch Processing', 'Process inference requests in batches', 'Batches processed with optimal throughput'),
        ('FR-004', 'Model Switching', 'Switch between model versions without downtime', 'Model updates applied with zero-downtime'),
    ],
    'INT': [
        ('FR-001', 'Event Processing', 'Process events from message queues', 'Events processed with at-least-once delivery'),
        ('FR-002', 'API Integration', 'Integrate with external APIs', 'API calls made with retry and circuit breaker patterns'),
        ('FR-003', 'Data Transformation', 'Transform data between formats', 'Data transformed with schema validation'),
        ('FR-004', 'Error Handling', 'Handle integration errors gracefully', 'Errors logged and retried per configuration'),
    ],
    'CNV': [
        ('FR-001', 'Conversation Management', 'Manage multi-turn conversations', 'Context maintained across conversation turns'),
        ('FR-002', 'Intent Recognition', 'Recognize user intent from input', 'Intent classified with confidence score'),
        ('FR-003', 'Response Generation', 'Generate appropriate responses', 'Responses generated matching intent and context'),
        ('FR-004', 'Channel Adaptation', 'Adapt responses for different channels', 'Responses formatted appropriately per channel'),
    ],
    'DOC': [
        ('FR-001', 'Document Ingestion', 'Ingest documents in various formats', 'Documents parsed with format detection'),
        ('FR-002', 'Text Extraction', 'Extract text from documents including OCR', 'Text extracted with >95% accuracy'),
        ('FR-003', 'Classification', 'Classify documents by type and content', 'Documents classified with confidence scores'),
        ('FR-004', 'Entity Extraction', 'Extract entities and key-value pairs', 'Entities extracted with validation'),
    ],
    'RTE': [
        ('FR-001', 'Request Routing', 'Route requests to appropriate backends', 'Requests routed based on configured rules'),
        ('FR-002', 'Load Balancing', 'Balance load across multiple instances', 'Load distributed evenly with health checks'),
        ('FR-003', 'Traffic Splitting', 'Split traffic for A/B testing', 'Traffic split according to configured percentages'),
        ('FR-004', 'Fallback Handling', 'Handle backend failures with fallbacks', 'Fallback activated within configured timeout'),
    ],
    'BAT': [
        ('FR-001', 'Job Scheduling', 'Schedule batch jobs for execution', 'Jobs executed at scheduled times'),
        ('FR-002', 'Parallel Processing', 'Process data in parallel partitions', 'Data partitioned and processed concurrently'),
        ('FR-003', 'Checkpoint Management', 'Manage checkpoints for recovery', 'Jobs resumable from last checkpoint'),
        ('FR-004', 'Result Aggregation', 'Aggregate results from parallel tasks', 'Results merged with consistency guarantees'),
    ],
    'CMP': [
        ('FR-001', 'Model Comparison', 'Compare performance of multiple models', 'Models evaluated on same test data'),
        ('FR-002', 'Statistical Testing', 'Perform statistical significance tests', 'Tests performed with configured confidence level'),
        ('FR-003', 'Metric Tracking', 'Track comparison metrics over time', 'Metrics recorded with timestamps'),
        ('FR-004', 'Promotion Decision', 'Recommend model promotion based on results', 'Recommendations generated with supporting evidence'),
    ],
    'KNW': [
        ('FR-001', 'Knowledge Ingestion', 'Ingest documents into knowledge base', 'Documents chunked and embedded'),
        ('FR-002', 'Semantic Search', 'Search knowledge base semantically', 'Relevant results returned for queries'),
        ('FR-003', 'Knowledge Retrieval', 'Retrieve relevant context for queries', 'Context retrieved within latency SLA'),
        ('FR-004', 'Knowledge Update', 'Update knowledge base with new information', 'Updates reflected in search results'),
    ],
    'VAL': [
        ('FR-001', 'Schema Validation', 'Validate data against schemas', 'Invalid data rejected with error details'),
        ('FR-002', 'Business Rule Validation', 'Apply business rules to data', 'Rules evaluated with pass/fail results'),
        ('FR-003', 'Anomaly Detection', 'Detect anomalous values in data', 'Anomalies flagged with confidence scores'),
        ('FR-004', 'Validation Reporting', 'Report validation results', 'Reports generated with statistics'),
    ],
    'VIS': [
        ('FR-001', 'Dashboard Rendering', 'Render interactive dashboards', 'Dashboards load within 3 seconds'),
        ('FR-002', 'Chart Generation', 'Generate various chart types', 'Charts rendered with correct data'),
        ('FR-003', 'Real-time Updates', 'Update visualizations in real-time', 'Updates reflected within 5 seconds'),
        ('FR-004', 'Export Functionality', 'Export visualizations to various formats', 'Exports generated in requested format'),
    ],
    'WFL': [
        ('FR-001', 'Workflow Definition', 'Define workflows with steps and transitions', 'Workflows created and validated'),
        ('FR-002', 'Workflow Execution', 'Execute workflows with proper sequencing', 'Steps executed in defined order'),
        ('FR-003', 'Human Task Management', 'Manage human review tasks', 'Tasks assigned and tracked to completion'),
        ('FR-004', 'Workflow Monitoring', 'Monitor workflow execution status', 'Status visible in real-time'),
    ],
    'API': [
        ('FR-001', 'Request Handling', 'Handle API requests with validation', 'Requests validated and processed'),
        ('FR-002', 'Rate Limiting', 'Enforce rate limits per client', 'Limits enforced with proper error responses'),
        ('FR-003', 'Response Formatting', 'Format responses consistently', 'Responses follow API contract'),
        ('FR-004', 'API Versioning', 'Support multiple API versions', 'Versions coexist without conflicts'),
    ],
    'CAC': [
        ('FR-001', 'Cache Storage', 'Store data in cache with TTL', 'Data cached with configurable expiration'),
        ('FR-002', 'Cache Retrieval', 'Retrieve data from cache', 'Cache hits return data within <5ms'),
        ('FR-003', 'Cache Invalidation', 'Invalidate cache entries', 'Invalidation propagates within configured time'),
        ('FR-004', 'Cache Statistics', 'Track cache hit/miss statistics', 'Statistics available for monitoring'),
    ],
}

# Default functional requirements for unmapped categories
DEFAULT_FUNCTIONAL_REQUIREMENTS = [
    ('FR-001', 'Core Processing', 'Execute primary processing function', 'Processing completes within SLA'),
    ('FR-002', 'Configuration Management', 'Manage component configuration', 'Configuration changes applied without restart'),
    ('FR-003', 'Error Handling', 'Handle errors gracefully', 'Errors logged with context and recovery attempted'),
    ('FR-004', 'Health Reporting', 'Report component health status', 'Health status available via standard endpoint'),
]

# ABB category to NFR targets mapping
CATEGORY_NFR_TARGETS = {
    'AGT': {'latency': '<500ms p99', 'throughput': '100 concurrent agents', 'availability': '99.9%'},
    'GEN': {'latency': '<2s p99 (first token <500ms)', 'throughput': '1000 req/min', 'availability': '99.9%'},
    'SEC': {'latency': '<50ms p99', 'throughput': '10,000 req/sec', 'availability': '99.99%'},
    'GOV': {'latency': '<100ms p99', 'throughput': '5000 req/sec', 'availability': '99.9%'},
    'OBS': {'latency': '<1s for dashboards', 'throughput': '100,000 metrics/sec', 'availability': '99.9%'},
    'MLO': {'latency': 'N/A (batch)', 'throughput': '100 concurrent pipelines', 'availability': '99.5%'},
    'DAT': {'latency': '<100ms p99 for queries', 'throughput': '10,000 queries/sec', 'availability': '99.9%'},
    'FTR': {'latency': '<10ms p99 for online', 'throughput': '50,000 req/sec', 'availability': '99.99%'},
    'INF': {'latency': '<100ms p99', 'throughput': '10,000 req/sec', 'availability': '99.9%'},
    'INT': {'latency': '<200ms p99', 'throughput': '5000 events/sec', 'availability': '99.9%'},
    'CNV': {'latency': '<1s p99', 'throughput': '1000 concurrent sessions', 'availability': '99.9%'},
    'DOC': {'latency': '<5s per document', 'throughput': '100 docs/min', 'availability': '99.5%'},
    'RTE': {'latency': '<10ms p99 overhead', 'throughput': '50,000 req/sec', 'availability': '99.99%'},
    'BAT': {'latency': 'N/A (batch)', 'throughput': '1M records/hour', 'availability': '99.5%'},
    'CMP': {'latency': 'N/A (batch)', 'throughput': '100 experiments/day', 'availability': '99.5%'},
    'KNW': {'latency': '<200ms p99', 'throughput': '1000 queries/sec', 'availability': '99.9%'},
    'VAL': {'latency': '<50ms p99', 'throughput': '10,000 validations/sec', 'availability': '99.9%'},
    'VIS': {'latency': '<3s page load', 'throughput': '1000 concurrent users', 'availability': '99.5%'},
    'WFL': {'latency': '<500ms p99', 'throughput': '1000 workflows/hour', 'availability': '99.9%'},
    'API': {'latency': '<100ms p99', 'throughput': '10,000 req/sec', 'availability': '99.9%'},
    'CAC': {'latency': '<5ms p99', 'throughput': '100,000 req/sec', 'availability': '99.99%'},
}

DEFAULT_NFR_TARGETS = {'latency': '<500ms p99', 'throughput': '1000 req/sec', 'availability': '99.9%'}


def get_abb_info(abb_file):
    """Extract ABB ID and name from file."""
    filename = abb_file.name
    match = re.match(r'(ABB-[A-Z]+-\d+)-(.+)-v\d+\.\d+\.\d+\.md', filename)
    if match:
        abb_id = match.group(1)
        abb_name = match.group(2).replace('-', ' ')
        return abb_id, abb_name
    return None, None


def get_abb_category(abb_id):
    """Extract category from ABB ID."""
    parts = abb_id.split('-')
    if len(parts) >= 2:
        return parts[1]
    return None


def generate_functional_requirements(abb_id, abb_name):
    """Generate functional requirements table for an ABB."""
    category = get_abb_category(abb_id)
    requirements = CATEGORY_FUNCTIONAL_REQUIREMENTS.get(category, DEFAULT_FUNCTIONAL_REQUIREMENTS)

    lines = []
    lines.append("**Primary Functions**:")
    lines.append("")
    lines.append("| Requirement ID | Requirement | Description | Acceptance Criteria |")
    lines.append("|----------------|-------------|-------------|---------------------|")

    for req_id, req_name, description, criteria in requirements:
        lines.append(f"| {req_id} | {req_name} | {description} | {criteria} |")

    return "\n".join(lines)


def generate_nfr_table(abb_id, abb_name):
    """Generate non-functional requirements table for an ABB."""
    category = get_abb_category(abb_id)
    targets = CATEGORY_NFR_TARGETS.get(category, DEFAULT_NFR_TARGETS)

    lines = []
    lines.append("| Category | Requirement | Target | Rationale |")
    lines.append("|----------|-------------|--------|-----------|")
    lines.append(f"| **Performance** | Response time | {targets['latency']} | User experience and SLA compliance |")
    lines.append(f"| **Scalability** | Throughput capacity | {targets['throughput']} | Handle peak load with headroom |")
    lines.append(f"| **Availability** | Uptime SLA | {targets['availability']} | Business continuity requirements |")
    lines.append("| **Security** | Data encryption | TLS 1.3 in transit, AES-256 at rest | Compliance with security standards |")
    lines.append("| **Compliance** | Data residency | Australia/New Zealand only | Regulatory requirement for financial data |")
    lines.append("| **Reliability** | Error rate | <0.1% of requests | Quality of service guarantee |")
    lines.append("| **Maintainability** | Deployment frequency | Daily deployments supported | CI/CD pipeline requirements |")

    return "\n".join(lines)


def update_abb_file(abb_file, abb_id, abb_name):
    """Update sections 2.2 and 2.3 in an ABB file."""
    with open(abb_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update section 2.2 - Functional Requirements
    pattern_22 = r'(### 2\.2 Functional Requirements\s*\n)(.*?)(\n### 2\.3|\n---)'
    match_22 = re.search(pattern_22, content, re.DOTALL)

    if not match_22:
        print(f"  WARNING: Could not find section 2.2 in {abb_file.name}")
        return False

    new_fr = generate_functional_requirements(abb_id, abb_name)
    content = content[:match_22.start(2)] + "\n" + new_fr + "\n" + content[match_22.end(2):]

    # Update section 2.3 - Non-Functional Requirements (need to re-search after modification)
    pattern_23 = r'(### 2\.3 Non-Functional Requirements\s*\n)(.*?)(\n---|\n## 3\.)'
    match_23 = re.search(pattern_23, content, re.DOTALL)

    if not match_23:
        print(f"  WARNING: Could not find section 2.3 in {abb_file.name}")
        return False

    new_nfr = generate_nfr_table(abb_id, abb_name)
    content = content[:match_23.start(2)] + "\n" + new_nfr + "\n" + content[match_23.end(2):]

    with open(abb_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return True


def main():
    print("Updating sections 2.2 and 2.3 for all ABBs...")

    # Find all ABB files
    abb_files = list(ABB_ROOT.glob("**/ABB-*.md"))
    print(f"Found {len(abb_files)} ABB files")

    updated = 0
    skipped = 0
    errors = 0

    for abb_file in sorted(abb_files):
        abb_id, abb_name = get_abb_info(abb_file)
        if not abb_id:
            print(f"  SKIP: Could not parse ABB ID from {abb_file.name}")
            skipped += 1
            continue

        category = get_abb_category(abb_id)
        print(f"Processing {abb_id} ({category}): {abb_name}")

        try:
            if update_abb_file(abb_file, abb_id, abb_name):
                updated += 1
            else:
                errors += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            errors += 1

    print(f"\nSummary:")
    print(f"  Updated: {updated}")
    print(f"  Skipped: {skipped}")
    print(f"  Errors: {errors}")


if __name__ == "__main__":
    main()
