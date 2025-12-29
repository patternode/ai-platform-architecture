#!/usr/bin/env python3
"""
Update all ABB documents to:
1. Change status from 'Draft' to 'Preliminary'
2. Add relevant glossary terms based on ABB category and name
"""

import os
import re
from pathlib import Path

# ABB base directory
ABB_DIR = Path(r"D:\Work\BNZ\ai-platform-architecture\03-building-blocks\architecture-building-blocks\abbs")

# Category-based glossary terms
CATEGORY_GLOSSARY = {
    "Agentic": {
        "Agent": "An autonomous AI system that can perceive its environment, make decisions, and take actions to achieve goals without constant human supervision.",
        "Orchestration": "The automated coordination and management of multiple components, services, or agents to work together in a defined workflow.",
        "Task Decomposition": "Breaking down complex goals into smaller, manageable sub-tasks that can be executed independently or in sequence.",
        "Tool": "A function or API that an AI agent can invoke to perform specific actions or retrieve information from external systems.",
        "Context Window": "The maximum amount of text (measured in tokens) that a language model can process in a single request.",
    },
    "API": {
        "API Gateway": "A server that acts as a single entry point for API requests, handling routing, authentication, rate limiting, and request transformation.",
        "Rate Limiting": "Controlling the number of requests a client can make within a specified time period to prevent abuse and ensure fair resource usage.",
        "API Versioning": "The practice of managing changes to an API over time by maintaining multiple versions simultaneously.",
        "REST": "Representational State Transfer - an architectural style for designing networked applications using HTTP methods.",
    },
    "Batch": {
        "Batch Processing": "Processing data in groups (batches) at scheduled intervals rather than in real-time, often for large-scale data transformations.",
        "Orchestrator": "A system that coordinates and manages the execution of batch jobs, handling dependencies, scheduling, and failure recovery.",
        "ETL": "Extract, Transform, Load - a process of extracting data from sources, transforming it, and loading into target systems.",
        "Data Pipeline": "A series of data processing steps where the output of one step becomes the input of the next.",
    },
    "Champion-Challenger": {
        "Champion Model": "The current production model that serves as the baseline for comparison against new candidate models.",
        "Challenger Model": "A new or updated model being tested against the champion to determine if it should replace the current production model.",
        "A/B Testing": "A method of comparing two versions (A and B) by exposing different user groups to each and measuring performance differences.",
        "Traffic Splitting": "Distributing incoming requests between multiple model versions based on defined percentages or rules.",
    },
    "Conversational": {
        "Intent Classification": "Identifying the purpose or goal behind a user's message to route it to the appropriate response handler.",
        "Entity Extraction": "Identifying and extracting specific pieces of information (entities) from text, such as names, dates, or amounts.",
        "Sentiment Analysis": "Determining the emotional tone or attitude expressed in text, typically classified as positive, negative, or neutral.",
        "Dialogue Management": "Managing the flow and context of a conversation to maintain coherent multi-turn interactions.",
        "NLU": "Natural Language Understanding - the ability of a system to comprehend and interpret human language.",
    },
    "Data": {
        "Feature Store": "A centralized repository for storing, managing, and serving machine learning features for both training and inference.",
        "Data Lake": "A centralized repository that stores large volumes of raw data in its native format until needed for analysis.",
        "Data Lineage": "Tracking the origin, movement, and transformation of data throughout its lifecycle in a system.",
        "Data Contract": "A formal agreement between data producers and consumers specifying schema, quality, and SLA requirements.",
    },
    "DataMesh": {
        "Data Mesh": "A decentralized data architecture paradigm where domain teams own and publish data as products with federated governance.",
        "Data Product": "A self-contained, discoverable data asset with clear ownership, SLAs, and quality guarantees.",
        "Domain Ownership": "The principle that business domains are responsible for their own data, including quality, access, and lifecycle.",
        "Federated Governance": "A governance model combining centralized policies with decentralized execution by domain teams.",
    },
    "Document": {
        "OCR": "Optical Character Recognition - technology that converts images of text into machine-readable text.",
        "Document Classification": "Categorizing documents into predefined classes based on their content, structure, or metadata.",
        "Information Extraction": "Automatically identifying and extracting structured information from unstructured documents.",
        "Document Forensics": "Analyzing documents to detect forgery, tampering, or authenticity issues.",
    },
    "Fairness": {
        "Algorithmic Fairness": "Ensuring AI systems treat all groups equitably and do not discriminate based on protected characteristics.",
        "Bias Detection": "Identifying systematic errors or prejudices in AI model predictions across different population groups.",
        "Protected Attribute": "A characteristic (e.g., race, gender, age) that should not influence model predictions in discriminatory ways.",
        "Disparate Impact": "When a model's predictions disproportionately affect one group compared to others, even if unintentional.",
    },
    "Features": {
        "Feature": "A measurable property or characteristic of the data used as input to a machine learning model.",
        "Feature Engineering": "The process of creating, selecting, and transforming features to improve model performance.",
        "Feature Serving": "Providing features to models at inference time with low latency and high availability.",
        "Feature Versioning": "Tracking different versions of feature definitions and values over time.",
    },
    "GenAI": {
        "Large Language Model (LLM)": "A neural network trained on vast amounts of text data capable of generating human-like text and understanding language.",
        "Vector Database": "A database optimized for storing and querying high-dimensional vector embeddings.",
        "Semantic Search": "Search that understands the meaning and context of queries rather than just matching keywords.",
        "RAG": "Retrieval-Augmented Generation - combining retrieval of relevant documents with generative AI to produce grounded responses.",
        "Embedding": "A numerical representation of text, images, or other data in a high-dimensional vector space.",
        "Prompt Engineering": "Designing and optimizing input prompts to elicit desired outputs from language models.",
    },
    "Governance": {
        "Model Registry": "A central repository for storing, versioning, and managing machine learning models throughout their lifecycle.",
        "Model Governance": "Policies and processes ensuring AI models are developed, deployed, and operated responsibly and compliantly.",
        "Explainability": "The ability to understand and explain how an AI model makes its predictions or decisions.",
        "Audit Trail": "A chronological record of system activities and changes for compliance and forensic purposes.",
        "Compliance": "Adherence to laws, regulations, policies, and standards governing AI systems.",
    },
    "Inference": {
        "Inference": "The process of using a trained model to make predictions on new, unseen data.",
        "Model Serving": "Deploying and running models to handle inference requests in production environments.",
        "Latency": "The time delay between receiving a request and returning a response.",
        "Throughput": "The number of requests a system can handle per unit of time.",
    },
    "Integration": {
        "Event Broker": "A system that receives events from producers and delivers them to consumers, enabling asynchronous communication.",
        "Event-Driven Architecture": "A software design pattern where the flow of the program is determined by events.",
        "Message Queue": "A form of asynchronous service-to-service communication used in distributed systems.",
        "Pub/Sub": "Publish-Subscribe pattern where publishers send messages to topics and subscribers receive messages from topics they're interested in.",
    },
    "Knowledge": {
        "Knowledge Base": "A structured repository of information that can be queried and reasoned over by AI systems.",
        "Knowledge Graph": "A database that stores information as a network of entities and their relationships.",
        "Semantic Layer": "An abstraction that provides a business-friendly view of data relationships and meanings.",
    },
    "LoadBalancing": {
        "Load Balancer": "A system that distributes incoming network traffic across multiple servers to ensure reliability and performance.",
        "Health Check": "Periodic verification that a service or system is functioning correctly.",
        "Failover": "Automatic switching to a backup system when the primary system fails.",
    },
    "Model": {
        "Model Serving": "The infrastructure and processes for deploying models to handle production inference requests.",
        "Model Versioning": "Tracking different versions of trained models for reproducibility and rollback capabilities.",
        "Fallback Model": "A backup model used when the primary model is unavailable or produces unreliable results.",
        "Model Quantization": "Reducing model precision (e.g., from 32-bit to 8-bit) to decrease size and improve inference speed.",
    },
    "MLOps": {
        "MLOps": "A set of practices for collaboration and communication between data scientists and operations to automate ML lifecycle.",
        "Training Pipeline": "An automated workflow for training, validating, and packaging machine learning models.",
        "Model Deployment": "The process of making a trained model available for use in production systems.",
        "Model Monitoring": "Continuous observation of model performance, data quality, and system health in production.",
        "Continuous Training": "Automatically retraining models when performance degrades or new data becomes available.",
    },
    "NLP": {
        "NLP": "Natural Language Processing - the ability of computers to understand, interpret, and generate human language.",
        "NLG": "Natural Language Generation - automatically producing human-readable text from structured data.",
        "Named Entity Recognition (NER)": "Identifying and classifying named entities (people, organizations, locations) in text.",
        "Text Classification": "Categorizing text into predefined classes based on its content.",
    },
    "Observability": {
        "Observability": "The ability to understand the internal state of a system by examining its outputs (logs, metrics, traces).",
        "Metrics": "Quantitative measurements of system behavior and performance over time.",
        "Distributed Tracing": "Tracking requests as they flow through distributed systems to understand latency and identify issues.",
        "Alerting": "Automatically notifying operators when metrics exceed defined thresholds.",
        "Data Drift": "Changes in the statistical properties of input data over time that may affect model performance.",
        "Model Drift": "Degradation in model performance over time due to changes in data patterns or relationships.",
    },
    "Routing": {
        "Model Router": "A component that directs requests to appropriate models based on request characteristics or routing rules.",
        "Intelligent Routing": "Using ML or rules to dynamically select the best model or service for each request.",
        "Cost-Based Routing": "Selecting models or services based on cost optimization while meeting quality requirements.",
    },
    "Security": {
        "Encryption": "The process of encoding data so that only authorized parties can access it.",
        "PII": "Personally Identifiable Information - data that can identify a specific individual.",
        "Data Masking": "Obscuring sensitive data to protect it from unauthorized access while maintaining usability.",
        "RBAC": "Role-Based Access Control - restricting system access based on users' roles within an organization.",
        "Zero Trust": "A security model that requires strict identity verification for every person and device accessing resources.",
    },
    "Streaming": {
        "Stream Processing": "Processing data continuously as it arrives, rather than in batches.",
        "Event Streaming": "The practice of capturing and processing events in real-time as they occur.",
        "Windowing": "Grouping stream data into finite sets based on time or count for aggregation and analysis.",
        "Exactly-Once Processing": "Guarantee that each message is processed exactly once, even in case of failures.",
    },
    "Validation": {
        "Validation": "Verifying that data, models, or outputs meet specified criteria and quality standards.",
        "Data Quality": "Measure of data's fitness for purpose including accuracy, completeness, consistency, and timeliness.",
        "Schema Validation": "Checking that data conforms to its expected structure and data types.",
    },
    "Visualization": {
        "Dashboard": "A visual display of key metrics and information, typically updated in real-time.",
        "Visualization": "The graphical representation of data and information to aid understanding and decision-making.",
    },
    "Workflow": {
        "Human-in-the-Loop": "A design pattern where humans review, validate, or override AI decisions at critical points.",
        "Workflow Orchestration": "Coordinating the execution of multiple tasks or processes in a defined sequence.",
        "Approval Workflow": "A process requiring human authorization before certain actions can be taken.",
    },
}

# Common terms for all ABBs
COMMON_GLOSSARY = {
    "ABB": "Architecture Building Block - a vendor-agnostic logical component that defines required capabilities.",
    "SBB": "Solution Building Block - a specific technology implementation of an ABB.",
    "SLA": "Service Level Agreement - a commitment on service quality, availability, and performance.",
    "API": "Application Programming Interface - a set of protocols for building and integrating software.",
}


def get_glossary_for_abb(abb_name: str, category: str) -> dict:
    """Generate appropriate glossary terms for an ABB based on its name and category."""
    glossary = dict(COMMON_GLOSSARY)

    # Add category-specific terms
    if category in CATEGORY_GLOSSARY:
        glossary.update(CATEGORY_GLOSSARY[category])

    # Add terms based on ABB name keywords
    name_lower = abb_name.lower()

    # Check for specific keywords and add relevant terms
    keyword_terms = {
        "agent": CATEGORY_GLOSSARY.get("Agentic", {}),
        "llm": CATEGORY_GLOSSARY.get("GenAI", {}),
        "language model": CATEGORY_GLOSSARY.get("GenAI", {}),
        "vector": CATEGORY_GLOSSARY.get("GenAI", {}),
        "embedding": CATEGORY_GLOSSARY.get("GenAI", {}),
        "search": CATEGORY_GLOSSARY.get("GenAI", {}),
        "rag": CATEGORY_GLOSSARY.get("GenAI", {}),
        "feature": CATEGORY_GLOSSARY.get("Features", {}),
        "model": CATEGORY_GLOSSARY.get("Model", {}),
        "inference": CATEGORY_GLOSSARY.get("Inference", {}),
        "training": CATEGORY_GLOSSARY.get("MLOps", {}),
        "drift": CATEGORY_GLOSSARY.get("Observability", {}),
        "monitor": CATEGORY_GLOSSARY.get("Observability", {}),
        "observability": CATEGORY_GLOSSARY.get("Observability", {}),
        "security": CATEGORY_GLOSSARY.get("Security", {}),
        "encryption": CATEGORY_GLOSSARY.get("Security", {}),
        "pii": CATEGORY_GLOSSARY.get("Security", {}),
        "governance": CATEGORY_GLOSSARY.get("Governance", {}),
        "registry": CATEGORY_GLOSSARY.get("Governance", {}),
        "compliance": CATEGORY_GLOSSARY.get("Governance", {}),
        "audit": CATEGORY_GLOSSARY.get("Governance", {}),
        "explainability": CATEGORY_GLOSSARY.get("Governance", {}),
        "bias": CATEGORY_GLOSSARY.get("Fairness", {}),
        "fairness": CATEGORY_GLOSSARY.get("Fairness", {}),
        "stream": CATEGORY_GLOSSARY.get("Streaming", {}),
        "event": CATEGORY_GLOSSARY.get("Integration", {}),
        "kafka": CATEGORY_GLOSSARY.get("Integration", {}),
        "batch": CATEGORY_GLOSSARY.get("Batch", {}),
        "document": CATEGORY_GLOSSARY.get("Document", {}),
        "ocr": CATEGORY_GLOSSARY.get("Document", {}),
        "nlp": CATEGORY_GLOSSARY.get("NLP", {}),
        "nlg": CATEGORY_GLOSSARY.get("NLP", {}),
        "intent": CATEGORY_GLOSSARY.get("Conversational", {}),
        "sentiment": CATEGORY_GLOSSARY.get("Conversational", {}),
        "conversation": CATEGORY_GLOSSARY.get("Conversational", {}),
        "data": CATEGORY_GLOSSARY.get("Data", {}),
        "lineage": CATEGORY_GLOSSARY.get("Data", {}),
        "quality": CATEGORY_GLOSSARY.get("Validation", {}),
        "validation": CATEGORY_GLOSSARY.get("Validation", {}),
        "dashboard": CATEGORY_GLOSSARY.get("Visualization", {}),
        "workflow": CATEGORY_GLOSSARY.get("Workflow", {}),
        "human": CATEGORY_GLOSSARY.get("Workflow", {}),
        "router": CATEGORY_GLOSSARY.get("Routing", {}),
        "routing": CATEGORY_GLOSSARY.get("Routing", {}),
        "load": CATEGORY_GLOSSARY.get("LoadBalancing", {}),
        "balancer": CATEGORY_GLOSSARY.get("LoadBalancing", {}),
        "api": CATEGORY_GLOSSARY.get("API", {}),
        "gateway": CATEGORY_GLOSSARY.get("API", {}),
        "champion": CATEGORY_GLOSSARY.get("Champion-Challenger", {}),
        "challenger": CATEGORY_GLOSSARY.get("Champion-Challenger", {}),
        "a/b": CATEGORY_GLOSSARY.get("Champion-Challenger", {}),
        "knowledge": CATEGORY_GLOSSARY.get("Knowledge", {}),
    }

    for keyword, terms in keyword_terms.items():
        if keyword in name_lower:
            glossary.update(terms)

    # Limit to most relevant 8-10 terms
    # Prioritize terms that appear in the ABB name
    prioritized = {}
    other = {}

    for term, definition in glossary.items():
        if term.lower() in name_lower or any(word in name_lower for word in term.lower().split()):
            prioritized[term] = definition
        else:
            other[term] = definition

    # Combine prioritized terms first, then fill with others up to 10 total
    result = dict(prioritized)
    remaining_slots = 10 - len(result)
    for term, definition in list(other.items())[:remaining_slots]:
        result[term] = definition

    return result


def format_glossary_table(glossary: dict) -> str:
    """Format glossary as a markdown table."""
    lines = ["| Term | Definition |", "|------|------------|"]
    for term, definition in sorted(glossary.items()):
        # Escape pipe characters in definition
        definition = definition.replace("|", "\\|")
        lines.append(f"| {term} | {definition} |")
    return "\n".join(lines)


def update_abb_file(filepath: Path) -> bool:
    """Update a single ABB file with status change and glossary."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Extract ABB name and category
        name_match = re.search(r'\| \*\*ABB Name\*\* \| (.+?) \|', content)
        category_match = re.search(r'\| \*\*Category\*\* \| `(.+?)` \|', content)

        abb_name = name_match.group(1) if name_match else "Unknown"
        category = category_match.group(1) if category_match else "Unknown"

        # Update status from Draft to Preliminary
        content = re.sub(
            r'\| \*\*Status\*\* \| `Draft` \|',
            '| **Status** | `Preliminary` |',
            content
        )

        # Generate glossary
        glossary = get_glossary_for_abb(abb_name, category)
        glossary_table = format_glossary_table(glossary)

        # Replace the placeholder glossary with actual terms
        old_glossary_pattern = r'## Appendix A: Glossary\n\n\| Term \| Definition \|\n\|------\|------------\|\n\| \[Term 1\] \| \[Definition\] \|\n\| \[Term 2\] \| \[Definition\] \|'

        new_glossary = f"## Appendix A: Glossary\n\n{glossary_table}"

        if re.search(old_glossary_pattern, content):
            content = re.sub(old_glossary_pattern, new_glossary, content)
        else:
            # Try alternative pattern (may already have some terms)
            alt_pattern = r'## Appendix A: Glossary\n\n\| Term \| Definition \|\n\|------\|------------\|(\n\| .+ \| .+ \|)*'
            if re.search(alt_pattern, content):
                content = re.sub(alt_pattern, new_glossary, content)

        # Only write if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False


def main():
    """Process all ABB files."""
    abb_dirs = sorted(ABB_DIR.iterdir())
    updated_count = 0
    total_count = 0

    for abb_dir in abb_dirs:
        if not abb_dir.is_dir() or not abb_dir.name.startswith("AB-"):
            continue

        # Find the markdown file in this directory
        md_files = list(abb_dir.glob("*.md"))
        if not md_files:
            print(f"Warning: No markdown file in {abb_dir.name}")
            continue

        for md_file in md_files:
            total_count += 1
            if update_abb_file(md_file):
                updated_count += 1
                print(f"Updated: {md_file.name}")
            else:
                print(f"No changes: {md_file.name}")

    print(f"\nSummary: Updated {updated_count} of {total_count} ABB files")


if __name__ == "__main__":
    main()
