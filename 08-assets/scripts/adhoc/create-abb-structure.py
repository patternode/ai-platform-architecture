#!/usr/bin/env python3
"""
Script: create-abb-structure.py
Purpose: Create subfolder structure for all ABBs referenced in patterns and use cases
Author: BNZ Enterprise Architecture
Date: 2025-12-06
"""

import os
from pathlib import Path
from datetime import datetime

# Configuration
ABB_DIR = Path(r"D:\Work\BNZ\ai-platform-architecture\03-building-blocks\architecture-building-blocks")
TEMPLATE_PATH = Path(r"D:\Work\BNZ\ai-platform-architecture\08-assets\templates\abb-template.md")

# Comprehensive ABB catalog extracted from patterns and use cases
# Format: (ABB_ID, ABB_Name, Category, Summary)
ABBS = [
    # GOV (Governance) Category
    ("AB-060", "AI Model Registry", "Governance", "Central registry for AI/ML models with metadata, versioning, and lifecycle management"),
    ("AB-061", "Risk Assessment Engine", "Governance", "Automated risk evaluation for AI models and use cases"),
    ("AB-062", "Approval Workflow Orchestrator", "Governance", "Manages approval workflows for model deployment and changes"),
    ("AB-063", "ML Model Explainability Engine", "Governance", "Generates explanations for ML model predictions"),
    ("AB-064", "Compliance Dashboard", "Governance", "Dashboard for tracking AI governance and compliance metrics"),
    ("AB-065", "Audit Trail & Logging", "Governance", "Comprehensive audit logging for AI system activities"),
    ("AB-066", "AI Gateway", "Governance", "Central gateway for AI service access and policy enforcement"),
    ("AB-067", "Cost Attribution Engine", "Governance", "Tracks and attributes AI infrastructure costs to use cases"),
    ("AB-068", "Explainability Service", "Governance", "Service for providing model explanations to stakeholders"),
    ("AB-069", "Bias Detection Framework", "Governance", "Detects and reports bias in ML models"),
    ("AB-070", "Data Lineage Tracker", "Governance", "Tracks data provenance and lineage for AI models"),
    ("AB-071", "Model Performance Benchmarking", "Governance", "Benchmarks model performance against baselines"),

    # SEC (Security) Category
    ("AB-112", "Data Encryption Service", "Security", "Encryption services for data at rest and in transit"),
    ("AB-113", "Access Control & Identity Management", "Security", "Identity and access management for AI platform"),
    ("AB-114", "PII Detection & Masking Service", "Security", "Detects and masks personally identifiable information"),
    ("AB-115", "Model Security Framework", "Security", "Security controls and vulnerability management for models"),
    ("AB-116", "Audit Logging & Monitoring", "Security", "Security-focused audit logging and threat monitoring"),
    ("AB-117", "Privacy Compliance Engine", "Security", "Ensures compliance with privacy regulations"),
    ("AB-118", "Secrets Management", "Security", "Secure storage and management of credentials and secrets"),
    ("AB-119", "Differential Privacy Engine", "Security", "Implements differential privacy for sensitive data"),
    ("AB-120", "Federated Learning Platform", "Security", "Enables privacy-preserving distributed model training"),
    ("AB-121", "Homomorphic Encryption Service", "Security", "Computation on encrypted data without decryption"),
    ("AB-122", "Secure Multi-Party Computation", "Security", "Enables secure computation across multiple parties"),
    ("AB-123", "Data Lineage & Provenance Tracker", "Security", "Security-focused data lineage and provenance tracking"),
    ("AB-124", "Model Watermarking Service", "Security", "Embeds watermarks in models for IP protection"),
    ("AB-125", "Adversarial Testing Framework", "Security", "Tests models against adversarial attacks"),

    # OBS (Observability) Category
    ("AB-096", "Observability Platform", "Observability", "Centralized platform for metrics, logs, and traces"),
    ("AB-097", "Data Drift Detector", "Observability", "Detects drift in input data distributions"),
    ("AB-098", "Prediction Drift Monitor", "Observability", "Monitors drift in model predictions"),
    ("AB-099", "Concept Drift Detector", "Observability", "Detects changes in underlying data relationships"),
    ("AB-100", "Cost Monitoring Dashboard", "Observability", "Real-time monitoring of AI infrastructure costs"),
    ("AB-101", "Latency Monitor", "Observability", "Tracks inference and pipeline latency metrics"),
    ("AB-102", "Error Tracking System", "Observability", "Captures and categorizes errors across AI systems"),
    ("AB-103", "Business Metrics Tracker", "Observability", "Links model performance to business outcomes"),
    ("AB-104", "Data Quality Monitor", "Observability", "Monitors data quality dimensions in real-time"),
    ("AB-105", "GenAI Quality Monitor", "Observability", "Monitors quality of generative AI outputs"),
    ("AB-106", "Automated Retraining Trigger", "Observability", "Triggers model retraining based on drift thresholds"),
    ("AB-107", "Stakeholder Dashboard", "Observability", "Executive dashboards for AI platform visibility"),

    # INT (Integration) Category
    ("AB-074", "Event Broker", "Integration", "Central event broker for async communication"),
    ("AB-075", "Stream Processing Engine", "Integration", "Processes streaming data in real-time"),
    ("AB-076", "Event Producer Adapter", "Integration", "Adapters for producing events from various sources"),
    ("AB-077", "Event Consumer Framework", "Integration", "Framework for consuming and processing events"),
    ("AB-078", "Dead Letter Queue", "Integration", "Handles failed message processing"),
    ("AB-079", "Event Replay Service", "Integration", "Replays events for recovery and testing"),

    # GEN (Generative AI) Category
    ("AB-050", "Large Language Model Service", "GenAI", "Foundation LLM service for text generation"),
    ("AB-051", "Vector Database", "GenAI", "Vector storage for embeddings and similarity search"),
    ("AB-052", "Semantic Search Engine", "GenAI", "Semantic search across knowledge bases"),
    ("AB-053", "Query Intent Analyzer", "GenAI", "Analyzes and classifies query intent"),
    ("AB-054", "Hybrid Search Engine", "GenAI", "Combines keyword and semantic search"),
    ("AB-055", "Reranking Engine", "GenAI", "Reranks search results for relevance"),
    ("AB-056", "Self-Critique Engine", "GenAI", "LLM self-evaluation and refinement"),
    ("AB-057", "Document Processing Pipeline", "GenAI", "Processes documents for RAG ingestion"),
    ("AB-058", "Citation Generator", "GenAI", "Generates citations for LLM responses"),
    ("AB-059", "Query Rewriting Engine", "GenAI", "Rewrites queries for better retrieval"),

    # AGT (Agentic AI) Category
    ("AB-001", "Agent Orchestrator", "Agentic", "Coordinates agent collaboration and task execution"),
    ("AB-002", "Tool Registry", "Agentic", "Registry of tools available to AI agents"),
    ("AB-003", "Agent Memory System", "Agentic", "Persistent memory for agent context"),
    ("AB-004", "Planning Module", "Agentic", "Strategic planning for agent task execution"),
    ("AB-005", "Execution Engine", "Agentic", "Executes agent plans and actions"),
    ("AB-006", "Reflection Module", "Agentic", "Agent self-reflection and learning"),
    ("AB-007", "Multi-Agent Communication Bus", "Agentic", "Inter-agent communication infrastructure"),
    ("AB-008", "Human-in-the-Loop Gateway", "Agentic", "Human oversight interface for agent actions"),
    ("AB-009", "Agent Cost Monitor", "Agentic", "Monitors token and API costs for agents"),
    ("AB-010", "Agent Versioning Manager", "Agentic", "Version control for agent configurations"),

    # DAT (Data) Category
    ("AB-037", "Feature Store", "Data", "Centralized repository for ML features"),
    ("AB-038", "Data Lake", "Data", "Scalable storage for structured and unstructured data"),
    ("AB-039", "Data Versioning Service", "Data", "Version control for datasets"),

    # MLO (ML Operations) Category
    ("AB-085", "ML Training Pipeline", "MLOps", "Orchestrates model training workflows"),
    ("AB-086", "Model Registry", "MLOps", "Central registry for trained models"),
    ("AB-087", "Model Testing Framework", "MLOps", "Comprehensive model testing and validation"),
    ("AB-088", "Model Deployment Orchestrator", "MLOps", "Automates model deployment workflows"),
    ("AB-089", "Model Monitoring Platform", "MLOps", "Production model performance monitoring"),
    ("AB-090", "Model Fallback Logic", "MLOps", "Handles model failures with fallback strategies"),
    ("AB-091", "Rollback Controller", "MLOps", "Manages model version rollbacks"),
    ("AB-092", "A/B Test Configuration Service", "MLOps", "Configures and manages A/B tests"),
    ("AB-093", "Feature Flag Service", "MLOps", "Feature flag management for ML features"),

    # DOC (Document Processing) Category
    ("AB-040", "Document Classification Engine", "Document", "Classifies documents by type and content"),
    ("AB-041", "OCR Engine", "Document", "Optical character recognition for documents"),
    ("AB-042", "Document Forensics Engine", "Document", "Detects document tampering and fraud"),

    # NLP (Natural Language Processing) Category
    ("AB-095", "NLP Extraction Engine", "NLP", "Extracts entities and relationships from text"),

    # VAL (Validation) Category
    ("AB-127", "Validation Engine", "Validation", "Validates data and model outputs"),

    # WFL (Workflow) Category
    ("AB-129", "Human-in-the-Loop Workflow", "Workflow", "Manages human review workflows"),

    # VIS (Visualization) Category
    ("AB-128", "Explanation Visualization Layer", "Visualization", "Visualizes model explanations"),

    # NLG (Natural Language Generation) Category
    ("AB-094", "Natural Language Generation", "NLG", "Generates natural language from structured data"),

    # FAI (Fairness) Category
    ("AB-046", "Fairness Monitoring Engine", "Fairness", "Monitors and reports on model fairness"),

    # API Category
    ("AB-011", "API Gateway", "API", "Central API gateway for AI services"),
    ("AB-012", "Explanation API Gateway", "API", "API gateway for explanation services"),

    # CAC (Caching) Category
    ("AB-024", "Prediction Caching Layer", "Caching", "Caches predictions for performance"),

    # FTR (Features) Category
    ("AB-047", "Online Feature Store", "Features", "Real-time feature serving"),
    ("AB-048", "Feature Engineering Pipeline", "Features", "Automated feature engineering"),
    ("AB-049", "Offline Feature Store", "Features", "Batch feature storage and retrieval"),

    # STR (Stream) Category
    ("AB-126", "Stream Processing Platform", "Stream", "Platform for stream processing"),

    # LDB (Load Balancing) Category
    ("AB-081", "Load Balancer", "LoadBalancing", "Distributes load across model replicas"),

    # MDL (Model) Category
    ("AB-082", "Model Serving Infrastructure", "Model", "Infrastructure for serving models"),
    ("AB-083", "Model Fallback Logic", "Model", "Fallback strategies for model failures"),
    ("AB-084", "Model Quantization Service", "Model", "Optimizes models through quantization"),

    # INF (Inference) Category
    ("AB-072", "Inference Engine", "Inference", "Core inference execution engine"),
    ("AB-073", "Inference Model Registry", "Inference", "Registry for inference-optimized models"),

    # BAT (Batch) Category
    ("AB-013", "Batch Orchestrator", "Batch", "Orchestrates batch prediction jobs"),
    ("AB-014", "Batch Feature Store", "Batch", "Feature store for batch processing"),
    ("AB-015", "Distributed Processing Engine", "Batch", "Distributed compute for batch jobs"),
    ("AB-016", "Batch Model Registry", "Batch", "Model registry for batch predictions"),
    ("AB-017", "Prediction Storage", "Batch", "Stores batch prediction results"),
    ("AB-018", "Data Quality Validator", "Batch", "Validates data quality in batch pipelines"),
    ("AB-019", "Incremental Processing Manager", "Batch", "Manages incremental batch processing"),
    ("AB-020", "Prediction Version Tracker", "Batch", "Tracks versions of batch predictions"),
    ("AB-021", "Drift Detection Monitor", "Batch", "Monitors drift in batch predictions"),
    ("AB-022", "Result Reconciliation Engine", "Batch", "Reconciles batch prediction results"),
    ("AB-023", "Batch Explainability Service", "Batch", "Generates explanations for batch predictions"),

    # KNW (Knowledge) Category
    ("AB-080", "Knowledge Base", "Knowledge", "Structured knowledge storage for AI"),

    # CNV (Conversational) Category
    ("AB-029", "Conversation State Manager", "Conversational", "Manages conversational context and state"),
    ("AB-030", "Intent Classifier", "Conversational", "Classifies user intent in conversations"),
    ("AB-031", "Response Generator", "Conversational", "Generates conversational responses"),
    ("AB-032", "Handoff Logic Engine", "Conversational", "Manages handoff to human agents"),
    ("AB-033", "Sentiment Analyzer", "Conversational", "Analyzes sentiment in conversations"),
    ("AB-034", "Entity Extractor", "Conversational", "Extracts entities from conversation"),
    ("AB-035", "Conversation Summarizer", "Conversational", "Summarizes conversation history"),
    ("AB-036", "Multi-Channel Orchestrator", "Conversational", "Orchestrates across chat channels"),

    # RTE (Routing) Category
    ("AB-108", "Model Router", "Routing", "Routes requests to appropriate models"),
    ("AB-109", "Cost-Based Router", "Routing", "Routes based on cost optimization"),
    ("AB-110", "Latency-Based Router", "Routing", "Routes based on latency requirements"),
    ("AB-111", "Capability-Based Router", "Routing", "Routes based on model capabilities"),

    # CMP (Champion-Challenger) Category
    ("AB-025", "Traffic Splitter", "ChampionChallenger", "Splits traffic between model versions"),
    ("AB-026", "Performance Comparator", "ChampionChallenger", "Compares model performance metrics"),
    ("AB-027", "Statistical Test Engine", "ChampionChallenger", "Runs statistical significance tests"),
    ("AB-028", "Model Promotion Service", "ChampionChallenger", "Promotes challenger to champion"),

    # DSH (Data Mesh) Category
    ("AB-043", "Data Product Catalog", "DataMesh", "Catalog of data products"),
    ("AB-044", "Domain Data Platform", "DataMesh", "Self-serve domain data platform"),
    ("AB-045", "Data Contract Registry", "DataMesh", "Registry for data contracts"),
]

def create_abb_folder(abb_id, abb_name, category, summary):
    """Create folder and placeholder markdown for an ABB."""
    folder_path = ABB_DIR / abb_id
    folder_path.mkdir(exist_ok=True)

    # Create the ABB markdown file
    md_filename = f"{abb_id}-{abb_name.replace(' ', '-').replace('/', '-').replace('&', 'and')}-v1.0.0.md"
    md_path = folder_path / md_filename

    today = datetime.now().strftime("%Y-%m-%d")

    # Read template
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()

    # Replace template placeholders
    content = template.replace("`ABB-XXX-001` (e.g., AB-050, AB-060)", f"`{abb_id}`")
    content = content.replace("[Name of Architecture Building Block]", abb_name)
    content = content.replace("`Draft` / `Review` / `Approved`", "`Draft`")
    content = content.replace("`YYYY-MM-DD`", f"`{today}`")
    content = content.replace("`GenAI` / `ML` / `Data` / `Governance` / `Security` / `Integration` / `Observability`", f"`{category}`")
    content = content.replace("[Full descriptive name]", abb_name)
    content = content.replace("[Abbreviated name for diagrams]", abb_id.split("-")[1])
    content = content.replace("[Select from: GenAI, ML, Data, Governance, Security, Integration, Observability, Infrastructure]", category)
    content = content.replace("[2-3 sentence description of what this ABB provides. Remember: ABBs are vendor-agnostic logical components that describe WHAT is needed, not HOW it is implemented.]", summary)

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return md_filename

def create_index_file():
    """Create the index.md with table of all ABBs."""
    # Group ABBs by category
    categories = {}
    for abb_id, abb_name, category, summary in ABBS:
        if category not in categories:
            categories[category] = []
        md_filename = f"{abb_id}-{abb_name.replace(' ', '-').replace('/', '-').replace('&', 'and')}-v1.0.0.md"
        categories[category].append((abb_id, abb_name, summary, md_filename))

    today = datetime.now().strftime("%Y-%m-%d")

    content = f"""# Architecture Building Blocks (ABBs) Index

## Overview

This index provides a comprehensive catalog of all Architecture Building Blocks (ABBs) that constitute the BNZ AI Platform architecture. ABBs are **vendor-agnostic logical components** that describe WHAT capability is needed, not HOW it is implemented.

**Key Principle**: ABBs remain stable over time while Solution Building Blocks (SBBs) that implement them may evolve with technology changes.

---

## Document Control

| Property | Value |
|----------|-------|
| **Version** | `1.0.0` |
| **Status** | `Draft` |
| **Last Updated** | `{today}` |
| **Total ABBs** | `{len(ABBS)}` |
| **Categories** | `{len(categories)}` |

---

## ABB Catalog by Category

"""

    # Sort categories alphabetically
    for category in sorted(categories.keys()):
        abbs = categories[category]
        content += f"""### {category}

| ABB ID | Name | Summary | Specification |
|--------|------|---------|---------------|
"""
        for abb_id, abb_name, summary, md_filename in sorted(abbs):
            link = f"[View]({abb_id}/{md_filename})"
            content += f"| {abb_id} | {abb_name} | {summary} | {link} |\n"
        content += "\n"

    # Add complete alphabetical table
    content += """---

## Complete ABB Catalog (Alphabetical)

| ABB ID | Name | Category | Summary | Specification |
|--------|------|----------|---------|---------------|
"""

    all_abbs = [(abb_id, abb_name, category, summary) for abb_id, abb_name, category, summary in ABBS]
    all_abbs.sort(key=lambda x: x[0])

    for abb_id, abb_name, category, summary in all_abbs:
        md_filename = f"{abb_id}-{abb_name.replace(' ', '-').replace('/', '-').replace('&', 'and')}-v1.0.0.md"
        link = f"[View]({abb_id}/{md_filename})"
        content += f"| {abb_id} | {abb_name} | {category} | {summary} | {link} |\n"

    content += """
---

## ABB Naming Convention

ABB IDs follow the pattern: `ABB-{CATEGORY}-{NUMBER}`

| Category Code | Category Name | Description |
|---------------|---------------|-------------|
| AGT | Agentic | AI agent orchestration and management |
| API | API | API management and gateways |
| BAT | Batch | Batch processing and prediction |
| CAC | Caching | Caching layers |
| CMP | Champion-Challenger | Model comparison and promotion |
| CNV | Conversational | Conversational AI components |
| DAT | Data | Data management and storage |
| DOC | Document | Document processing |
| DSH | Data Mesh | Data mesh components |
| FAI | Fairness | Fairness and bias detection |
| FTR | Features | Feature engineering and storage |
| GEN | GenAI | Generative AI components |
| GOV | Governance | AI governance and compliance |
| INF | Inference | Model inference |
| INT | Integration | Integration and messaging |
| KNW | Knowledge | Knowledge management |
| LDB | Load Balancing | Load balancing and routing |
| MDL | Model | Model management |
| MLO | MLOps | ML operations |
| NLG | NLG | Natural language generation |
| NLP | NLP | Natural language processing |
| OBS | Observability | Monitoring and observability |
| RTE | Routing | Request routing |
| SEC | Security | Security and privacy |
| STR | Stream | Stream processing |
| VAL | Validation | Validation services |
| VIS | Visualization | Visualization components |
| WFL | Workflow | Workflow management |

---

## Related Documentation

- [Solution Building Blocks (SBBs)](../solution-building-blocks/README.md) - Vendor-specific implementations
- [Architecture Patterns](../patterns/README.md) - Reusable architectural patterns
- [ABB Template](../../08-assets/templates/abb-template.md) - Template for creating new ABBs

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | {today} | BNZ Enterprise Architecture | Initial ABB catalog creation |
"""

    index_path = ABB_DIR / "README.md"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return len(ABBS)

def main():
    print("=" * 70)
    print("Create ABB Subfolder Structure")
    print("=" * 70)
    print()
    print(f"Target directory: {ABB_DIR}")
    print(f"Total ABBs to create: {len(ABBS)}")
    print()

    # Create folders and markdown files
    created = 0
    for abb_id, abb_name, category, summary in ABBS:
        md_filename = create_abb_folder(abb_id, abb_name, category, summary)
        created += 1
        print(f"  Created: {abb_id}/ -> {md_filename}")

    print()

    # Create index file
    total = create_index_file()
    print(f"Created index.md with {total} ABB entries")

    print()
    print("=" * 70)
    print(f"Summary: Created {created} ABB folders and 1 index file")
    print("=" * 70)

if __name__ == "__main__":
    main()
