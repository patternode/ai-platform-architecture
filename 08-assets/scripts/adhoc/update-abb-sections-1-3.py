#!/usr/bin/env python3
"""
Script to update sections 1 (ABB Overview) and 3 (Integration Specification)
in all ABB files with meaningful, category-specific content.
"""

import csv
import re
from pathlib import Path
from collections import defaultdict

# Paths
REPO_ROOT = Path(r"D:\Work\BNZ\ai-platform-architecture")
CAPS_CSV_PATH = REPO_ROOT / "02-capabilities" / "capabilities-consolidated.csv"
PATTERNS_CSV_PATH = REPO_ROOT / "03-building-blocks" / "patterns" / "patterns-consolidated.csv"
ABB_ROOT = REPO_ROOT / "03-building-blocks" / "architecture-building-blocks" / "abbs"

# Category definitions with business/technical purposes
CATEGORY_DEFINITIONS = {
    'AGT': {
        'full_name': 'Agentic AI',
        'business_purpose': 'Enable autonomous AI-driven task execution that reduces manual effort, accelerates decision-making, and improves operational efficiency by allowing AI agents to perform complex multi-step tasks independently.',
        'technical_purpose': 'Provide the foundational infrastructure for autonomous agent execution, including task orchestration, tool invocation, memory management, and multi-agent coordination within the AI platform.',
    },
    'GEN': {
        'full_name': 'Generative AI',
        'business_purpose': 'Enable natural language understanding and generation capabilities that power customer-facing chatbots, document automation, content generation, and intelligent assistance across business units.',
        'technical_purpose': 'Provide large language model services, retrieval-augmented generation, and semantic search capabilities that form the foundation of generative AI applications.',
    },
    'SEC': {
        'full_name': 'Security',
        'business_purpose': 'Protect AI systems and data from security threats while ensuring compliance with regulatory requirements and maintaining customer trust through robust security controls.',
        'technical_purpose': 'Implement security controls, threat detection, privacy protection, and access management across all AI platform components.',
    },
    'GOV': {
        'full_name': 'Governance',
        'business_purpose': 'Ensure responsible AI deployment through comprehensive governance frameworks that maintain regulatory compliance, enable model transparency, and support risk management.',
        'technical_purpose': 'Provide centralized model governance, compliance monitoring, explainability, and audit capabilities across the AI platform.',
    },
    'OBS': {
        'full_name': 'Observability',
        'business_purpose': 'Maintain operational excellence and business value by detecting performance issues, model drift, and anomalies before they impact customers or business outcomes.',
        'technical_purpose': 'Provide unified monitoring, logging, alerting, and drift detection capabilities across all AI systems and models.',
    },
    'MLO': {
        'full_name': 'MLOps',
        'business_purpose': 'Accelerate time-to-value for machine learning initiatives by automating the ML lifecycle from development through production deployment and monitoring.',
        'technical_purpose': 'Provide automated CI/CD pipelines for ML models, including training, testing, deployment, and monitoring infrastructure.',
    },
    'DAT': {
        'full_name': 'Data Management',
        'business_purpose': 'Enable data-driven AI by providing reliable, high-quality data access and management capabilities that support model training and inference.',
        'technical_purpose': 'Provide data storage, versioning, cataloging, and access management infrastructure for AI/ML workloads.',
    },
    'FTR': {
        'full_name': 'Feature Engineering',
        'business_purpose': 'Accelerate ML development and improve model quality by providing reusable, consistent features that reduce duplication and ensure training-serving consistency.',
        'technical_purpose': 'Provide feature storage, computation, and serving infrastructure for both batch and real-time ML use cases.',
    },
    'INF': {
        'full_name': 'Inference',
        'business_purpose': 'Enable real-time AI-driven decisions and predictions that power customer-facing applications, fraud detection, and personalization use cases.',
        'technical_purpose': 'Provide low-latency model serving infrastructure that supports real-time inference at scale.',
    },
    'INT': {
        'full_name': 'Integration',
        'business_purpose': 'Enable seamless AI integration with existing systems and real-time event processing that powers immediate business responses.',
        'technical_purpose': 'Provide event-driven architecture, stream processing, and integration infrastructure for AI systems.',
    },
    'CNV': {
        'full_name': 'Conversational AI',
        'business_purpose': 'Deliver intelligent customer service and support through natural language interfaces that improve customer experience and reduce contact center costs.',
        'technical_purpose': 'Provide conversation management, intent classification, entity extraction, and response generation capabilities for chatbots and virtual assistants.',
    },
    'DOC': {
        'full_name': 'Document Intelligence',
        'business_purpose': 'Automate document-heavy business processes by extracting, classifying, and validating information from unstructured documents to improve efficiency and accuracy.',
        'technical_purpose': 'Provide document classification, OCR, extraction, and validation capabilities for intelligent document processing.',
    },
    'RTE': {
        'full_name': 'Routing',
        'business_purpose': 'Optimize AI system performance and cost by intelligently routing requests to the most appropriate models and services.',
        'technical_purpose': 'Provide intelligent request routing, load balancing, and model selection capabilities.',
    },
    'BAT': {
        'full_name': 'Batch Processing',
        'business_purpose': 'Enable large-scale AI processing for analytics, reporting, and scheduled decision-making that supports business planning and risk management.',
        'technical_purpose': 'Provide batch orchestration, distributed processing, and scheduled inference capabilities for large-scale ML workloads.',
    },
    'CMP': {
        'full_name': 'Model Comparison',
        'business_purpose': 'De-risk model deployments by enabling controlled experiments that validate model performance before full production rollout.',
        'technical_purpose': 'Provide A/B testing, champion/challenger comparison, and statistical validation infrastructure for model deployment.',
    },
    'KNW': {
        'full_name': 'Knowledge Management',
        'business_purpose': 'Improve AI response quality and consistency by providing centralized access to enterprise knowledge and documentation.',
        'technical_purpose': 'Provide knowledge storage, indexing, and retrieval capabilities that support RAG and knowledge-intensive AI applications.',
    },
    'VAL': {
        'full_name': 'Validation',
        'business_purpose': 'Ensure AI output quality and reliability by validating predictions, detecting anomalies, and enforcing business rules.',
        'technical_purpose': 'Provide prediction validation, quality checks, and business rule enforcement for AI outputs.',
    },
    'VIS': {
        'full_name': 'Visualization',
        'business_purpose': 'Enable data-driven decisions by providing intuitive visualizations of AI model performance, predictions, and business impact.',
        'technical_purpose': 'Provide dashboard, charting, and reporting capabilities for AI analytics and monitoring.',
    },
    'WFL': {
        'full_name': 'Workflow',
        'business_purpose': 'Automate and orchestrate complex business processes that involve multiple AI and human steps.',
        'technical_purpose': 'Provide workflow orchestration, task management, and process automation capabilities.',
    },
    'API': {
        'full_name': 'API Management',
        'business_purpose': 'Enable secure and scalable AI service access for internal and external consumers through managed API interfaces.',
        'technical_purpose': 'Provide API gateway, rate limiting, authentication, and request management for AI services.',
    },
    'CAC': {
        'full_name': 'Caching',
        'business_purpose': 'Improve AI system performance and reduce costs by caching frequently requested predictions and responses.',
        'technical_purpose': 'Provide prediction caching, response storage, and cache management for AI services.',
    },
    'DSH': {
        'full_name': 'Data Sharing',
        'business_purpose': 'Enable data democratization and domain-driven data ownership through data products and contracts.',
        'technical_purpose': 'Provide data product catalogs, domain platforms, and contract management for federated data access.',
    },
    'FAI': {
        'full_name': 'AI Fairness',
        'business_purpose': 'Ensure responsible AI by detecting and mitigating bias in ML models to maintain regulatory compliance and customer trust.',
        'technical_purpose': 'Provide fairness monitoring, bias detection, and mitigation capabilities for ML models.',
    },
    'LDB': {
        'full_name': 'Load Distribution',
        'business_purpose': 'Ensure high availability and optimal performance of AI services through intelligent load distribution.',
        'technical_purpose': 'Provide load balancing, traffic management, and service discovery for AI infrastructure.',
    },
    'MDL': {
        'full_name': 'Model Infrastructure',
        'business_purpose': 'Optimize model serving performance and reliability through infrastructure optimizations.',
        'technical_purpose': 'Provide model serving optimization, quantization, and infrastructure management capabilities.',
    },
    'NLG': {
        'full_name': 'Natural Language Generation',
        'business_purpose': 'Automate content creation and report generation to improve productivity and consistency.',
        'technical_purpose': 'Provide text generation, summarization, and content creation capabilities.',
    },
    'NLP': {
        'full_name': 'Natural Language Processing',
        'business_purpose': 'Extract insights and structure from unstructured text to enable automation and decision support.',
        'technical_purpose': 'Provide text extraction, parsing, and analysis capabilities for NLP applications.',
    },
    'PII': {
        'full_name': 'Privacy Protection',
        'business_purpose': 'Protect customer privacy and ensure regulatory compliance by detecting and handling sensitive data appropriately.',
        'technical_purpose': 'Provide PII detection, masking, and privacy-preserving capabilities for AI systems.',
    },
    'PRO': {
        'full_name': 'Prompt Engineering',
        'business_purpose': 'Improve LLM response quality and consistency through systematic prompt management and optimization.',
        'technical_purpose': 'Provide prompt storage, versioning, A/B testing, and optimization capabilities.',
    },
    'RAG': {
        'full_name': 'Retrieval-Augmented Generation',
        'business_purpose': 'Improve LLM response accuracy and reduce hallucinations by grounding responses in enterprise knowledge.',
        'technical_purpose': 'Provide document chunking, embedding, retrieval, and response synthesis capabilities.',
    },
    'TKN': {
        'full_name': 'Token Management',
        'business_purpose': 'Optimize LLM costs and performance through intelligent token management and budgeting.',
        'technical_purpose': 'Provide token counting, budgeting, and optimization capabilities for LLM applications.',
    },
}

# Category-specific responsibilities
CATEGORY_RESPONSIBILITIES = {
    'AGT': [
        'Manage agent lifecycle including creation, configuration, and termination',
        'Coordinate task execution across multiple agents and tools',
        'Maintain agent state and context across interactions',
        'Provide agent-to-agent communication protocols',
    ],
    'GEN': [
        'Process natural language inputs and generate coherent responses',
        'Manage model context windows and token limits',
        'Support multiple LLM providers and model versions',
        'Enable prompt management and template substitution',
    ],
    'SEC': [
        'Enforce access controls and authentication policies',
        'Detect and respond to security threats',
        'Protect sensitive data through encryption and masking',
        'Maintain audit trails for security events',
    ],
    'GOV': [
        'Track and manage AI model metadata and versions',
        'Enforce governance policies and approval workflows',
        'Provide explainability and transparency for AI decisions',
        'Monitor compliance with regulatory requirements',
    ],
    'OBS': [
        'Collect and aggregate metrics from AI systems',
        'Detect anomalies and performance degradation',
        'Provide alerting and notification capabilities',
        'Enable root cause analysis and debugging',
    ],
    'MLO': [
        'Automate model training and deployment pipelines',
        'Manage model versions and artifacts',
        'Execute model testing and validation',
        'Coordinate model rollout and rollback procedures',
    ],
    'DAT': [
        'Store and manage datasets for ML workloads',
        'Track data versions and lineage',
        'Provide data access and query capabilities',
        'Ensure data quality and consistency',
    ],
    'FTR': [
        'Compute and store ML features',
        'Serve features for real-time inference',
        'Ensure training-serving consistency',
        'Support feature discovery and reuse',
    ],
    'INF': [
        'Serve ML models for real-time predictions',
        'Manage model loading and warm-up',
        'Handle concurrent prediction requests',
        'Provide response caching and optimization',
    ],
    'INT': [
        'Process events in real-time',
        'Route messages between systems',
        'Handle event replay and recovery',
        'Manage event schemas and contracts',
    ],
    'CNV': [
        'Manage conversation state and context',
        'Classify user intents and extract entities',
        'Generate contextually appropriate responses',
        'Handle conversation handoff and escalation',
    ],
    'DOC': [
        'Classify documents by type and content',
        'Extract text and data from documents',
        'Validate extracted information',
        'Detect document fraud and anomalies',
    ],
    'RTE': [
        'Route requests to appropriate models',
        'Balance load across service instances',
        'Select optimal models based on requirements',
        'Manage failover and fallback logic',
    ],
    'BAT': [
        'Schedule and orchestrate batch jobs',
        'Process large datasets in parallel',
        'Track batch execution progress',
        'Handle batch failures and retries',
    ],
    'CMP': [
        'Split traffic between model versions',
        'Compare model performance metrics',
        'Execute statistical significance tests',
        'Manage model promotion decisions',
    ],
    'KNW': [
        'Store and index enterprise knowledge',
        'Provide search and retrieval capabilities',
        'Manage knowledge updates and versioning',
        'Support knowledge curation and validation',
    ],
}

# Category-specific scope definitions
CATEGORY_SCOPE = {
    'AGT': {
        'in_scope': [
            'Agent lifecycle management and configuration',
            'Task decomposition and execution coordination',
            'Tool invocation and result handling',
            'Agent state persistence and recovery',
        ],
        'out_scope': [
            'Specific tool implementations (handled by Tool Registry)',
            'LLM model hosting (handled by LLM Service)',
            'Security policy enforcement (handled by Security ABBs)',
        ],
    },
    'GEN': {
        'in_scope': [
            'LLM model invocation and response handling',
            'Prompt template management and rendering',
            'Token counting and context management',
            'Response streaming and formatting',
        ],
        'out_scope': [
            'Document retrieval (handled by RAG components)',
            'Conversation state management (handled by Conversational ABBs)',
            'Model training and fine-tuning (handled by MLOps ABBs)',
        ],
    },
    'SEC': {
        'in_scope': [
            'Security policy enforcement and access control',
            'Threat detection and response',
            'Data encryption and key management',
            'Security audit logging',
        ],
        'out_scope': [
            'Business logic implementation',
            'Model training and inference',
            'Data storage (handled by Data ABBs)',
        ],
    },
    'GOV': {
        'in_scope': [
            'Model metadata management and versioning',
            'Governance policy enforcement',
            'Compliance monitoring and reporting',
            'Explainability and transparency features',
        ],
        'out_scope': [
            'Model training execution (handled by MLOps ABBs)',
            'Real-time inference (handled by Inference ABBs)',
            'Security enforcement (handled by Security ABBs)',
        ],
    },
    'OBS': {
        'in_scope': [
            'Metric collection and aggregation',
            'Alerting and notification',
            'Log management and analysis',
            'Drift detection and monitoring',
        ],
        'out_scope': [
            'Automated remediation (handled by MLOps ABBs)',
            'Model retraining triggers (handled by Governance ABBs)',
            'Business-level reporting (handled by BI tools)',
        ],
    },
    'MLO': {
        'in_scope': [
            'ML pipeline orchestration and automation',
            'Model artifact management',
            'Training job execution and scheduling',
            'Deployment automation and rollback',
        ],
        'out_scope': [
            'Real-time model serving (handled by Inference ABBs)',
            'Feature computation (handled by Feature ABBs)',
            'Data storage (handled by Data ABBs)',
        ],
    },
    'DAT': {
        'in_scope': [
            'Data storage and retrieval',
            'Data versioning and lineage tracking',
            'Data cataloging and discovery',
            'Data access control',
        ],
        'out_scope': [
            'Feature computation (handled by Feature ABBs)',
            'Model training (handled by MLOps ABBs)',
            'Real-time streaming (handled by Integration ABBs)',
        ],
    },
    'FTR': {
        'in_scope': [
            'Feature computation and storage',
            'Feature serving for inference',
            'Feature versioning and metadata',
            'Feature discovery and documentation',
        ],
        'out_scope': [
            'Raw data storage (handled by Data ABBs)',
            'Model inference (handled by Inference ABBs)',
            'Data pipeline orchestration (handled by MLOps ABBs)',
        ],
    },
    'INF': {
        'in_scope': [
            'Model loading and serving',
            'Prediction request handling',
            'Response formatting and delivery',
            'Inference optimization and caching',
        ],
        'out_scope': [
            'Model training (handled by MLOps ABBs)',
            'Feature retrieval (handled by Feature ABBs)',
            'Business logic (handled by application layer)',
        ],
    },
    'INT': {
        'in_scope': [
            'Event production and consumption',
            'Stream processing and transformation',
            'Event routing and delivery',
            'Message persistence and replay',
        ],
        'out_scope': [
            'Business logic implementation',
            'Data storage (handled by Data ABBs)',
            'API management (handled by API ABBs)',
        ],
    },
    'CNV': {
        'in_scope': [
            'Conversation state and context management',
            'Intent classification and entity extraction',
            'Response generation and formatting',
            'Channel integration and handoff',
        ],
        'out_scope': [
            'LLM model hosting (handled by GenAI ABBs)',
            'Knowledge retrieval (handled by Knowledge ABBs)',
            'Customer data management (handled by CRM systems)',
        ],
    },
    'DOC': {
        'in_scope': [
            'Document classification and categorization',
            'Text extraction and OCR',
            'Data extraction and validation',
            'Document fraud detection',
        ],
        'out_scope': [
            'Document storage (handled by Data ABBs)',
            'Business process orchestration (handled by Workflow ABBs)',
            'Customer notifications (handled by Integration ABBs)',
        ],
    },
    'BAT': {
        'in_scope': [
            'Batch job scheduling and orchestration',
            'Distributed data processing',
            'Batch prediction execution',
            'Result storage and delivery',
        ],
        'out_scope': [
            'Real-time inference (handled by Inference ABBs)',
            'Data storage (handled by Data ABBs)',
            'Model management (handled by MLOps ABBs)',
        ],
    },
    'CMP': {
        'in_scope': [
            'Traffic splitting and routing',
            'Performance metric collection',
            'Statistical analysis and testing',
            'Model promotion decisions',
        ],
        'out_scope': [
            'Model serving (handled by Inference ABBs)',
            'Model deployment (handled by MLOps ABBs)',
            'Monitoring dashboards (handled by Observability ABBs)',
        ],
    },
}

# Default scope for categories not explicitly defined
DEFAULT_SCOPE = {
    'in_scope': [
        'Core functionality as described in capability mapping',
        'Integration with related ABBs in the platform',
        'Configuration and management interfaces',
        'Monitoring and health check endpoints',
    ],
    'out_scope': [
        'Functionality covered by other ABBs in the same pattern',
        'Business logic implementation (handled by application layer)',
        'Infrastructure provisioning (handled by platform teams)',
    ],
}

# ABB-specific dependency mappings based on typical patterns
# Format: {abb_category: {'upstream': [(category, name, type, desc)], 'downstream': [...]}}
CATEGORY_DEPENDENCIES = {
    'AGT': {
        'upstream': [
            ('GEN-001', 'Large Language Model Service', 'Required', 'LLM for agent reasoning and response generation'),
            ('AGT-002', 'Tool Registry', 'Required', 'Registry of available tools for agent execution'),
            ('AGT-003', 'Agent Memory System', 'Required', 'Persistent memory for agent context'),
        ],
        'downstream': [
            ('API-001', 'API Gateway', 'Optional', 'Exposes agent capabilities via API'),
            ('OBS-001', 'Observability Platform', 'Required', 'Monitors agent execution and performance'),
        ],
    },
    'GEN': {
        'upstream': [
            ('SEC-001', 'AI Security Gateway', 'Required', 'Security controls for LLM requests'),
            ('GOV-007', 'AI Gateway', 'Required', 'Request routing and governance'),
        ],
        'downstream': [
            ('AGT-001', 'Agent Orchestrator', 'Optional', 'Uses LLM for agent reasoning'),
            ('CNV-003', 'Response Generator', 'Optional', 'Uses LLM for response generation'),
            ('RAG-001', 'RAG Pipeline', 'Optional', 'Uses LLM for answer synthesis'),
        ],
    },
    'SEC': {
        'upstream': [],
        'downstream': [
            ('GEN-001', 'Large Language Model Service', 'Required', 'Protects LLM services'),
            ('API-001', 'API Gateway', 'Required', 'Provides security for API endpoints'),
        ],
    },
    'GOV': {
        'upstream': [
            ('MLO-002', 'Model Registry', 'Required', 'Source of model metadata'),
            ('OBS-001', 'Observability Platform', 'Required', 'Source of monitoring data'),
        ],
        'downstream': [
            ('MLO-004', 'Model Deployment Orchestrator', 'Required', 'Enforces deployment policies'),
        ],
    },
    'OBS': {
        'upstream': [],
        'downstream': [
            ('GOV-005', 'Compliance Dashboard', 'Optional', 'Provides metrics for dashboards'),
            ('MLO-005', 'Model Monitoring Platform', 'Required', 'Provides observability infrastructure'),
        ],
    },
    'MLO': {
        'upstream': [
            ('DAT-001', 'Feature Store', 'Required', 'Training data and features'),
            ('GOV-001', 'AI Model Registry', 'Required', 'Model registration and governance'),
        ],
        'downstream': [
            ('INF-001', 'Inference Engine', 'Required', 'Deployed models for serving'),
            ('BAT-001', 'Batch Orchestrator', 'Optional', 'Models for batch processing'),
        ],
    },
    'DAT': {
        'upstream': [],
        'downstream': [
            ('FTR-001', 'Online Feature Store', 'Required', 'Source data for features'),
            ('MLO-001', 'ML Training Pipeline', 'Required', 'Training datasets'),
        ],
    },
    'FTR': {
        'upstream': [
            ('DAT-001', 'Feature Store', 'Required', 'Raw data for feature computation'),
            ('DAT-002', 'Data Lake', 'Required', 'Historical data for offline features'),
        ],
        'downstream': [
            ('INF-001', 'Inference Engine', 'Required', 'Features for real-time inference'),
            ('MLO-001', 'ML Training Pipeline', 'Required', 'Features for model training'),
        ],
    },
    'INF': {
        'upstream': [
            ('MLO-002', 'Model Registry', 'Required', 'Source of deployed models'),
            ('FTR-001', 'Online Feature Store', 'Required', 'Features for inference'),
            ('CAC-001', 'Prediction Caching Layer', 'Optional', 'Cached predictions'),
        ],
        'downstream': [
            ('API-001', 'API Gateway', 'Required', 'Exposes inference endpoints'),
            ('OBS-001', 'Observability Platform', 'Required', 'Reports inference metrics'),
        ],
    },
    'INT': {
        'upstream': [],
        'downstream': [
            ('INF-001', 'Inference Engine', 'Optional', 'Triggers real-time inference'),
            ('FTR-002', 'Feature Engineering Pipeline', 'Optional', 'Provides streaming data'),
        ],
    },
    'CNV': {
        'upstream': [
            ('GEN-001', 'Large Language Model Service', 'Required', 'LLM for response generation'),
            ('KNW-001', 'Knowledge Base', 'Required', 'Knowledge for responses'),
        ],
        'downstream': [
            ('API-001', 'API Gateway', 'Required', 'Exposes conversation endpoints'),
        ],
    },
    'DOC': {
        'upstream': [
            ('GEN-001', 'Large Language Model Service', 'Optional', 'LLM for document understanding'),
            ('DAT-002', 'Data Lake', 'Required', 'Document storage'),
        ],
        'downstream': [
            ('WFL-001', 'Workflow Engine', 'Optional', 'Triggers downstream workflows'),
        ],
    },
    'BAT': {
        'upstream': [
            ('DAT-001', 'Feature Store', 'Required', 'Batch input data'),
            ('MLO-002', 'Model Registry', 'Required', 'Models for batch inference'),
        ],
        'downstream': [
            ('DAT-002', 'Data Lake', 'Required', 'Stores batch results'),
        ],
    },
    'CMP': {
        'upstream': [
            ('INF-001', 'Inference Engine', 'Required', 'Models under comparison'),
            ('OBS-001', 'Observability Platform', 'Required', 'Performance metrics'),
        ],
        'downstream': [
            ('MLO-004', 'Model Deployment Orchestrator', 'Required', 'Triggers model promotion'),
        ],
    },
}

# Interface definitions by category
CATEGORY_INTERFACES = {
    'AGT': {
        'input': [
            ('IF-IN-001', 'Task Request API', 'REST', 'JSON', 'Receives agent task requests with goals and context'),
            ('IF-IN-002', 'Agent Configuration', 'REST', 'JSON', 'Receives agent configuration and tool permissions'),
        ],
        'output': [
            ('IF-OUT-001', 'Task Response API', 'REST', 'JSON', 'Returns task execution results and status'),
            ('IF-OUT-002', 'Agent Events', 'Kafka', 'Avro', 'Publishes agent execution events for monitoring'),
        ],
    },
    'GEN': {
        'input': [
            ('IF-IN-001', 'Completion API', 'REST', 'JSON', 'Receives text generation requests with prompts'),
            ('IF-IN-002', 'Streaming API', 'WebSocket', 'JSON', 'Receives streaming generation requests'),
        ],
        'output': [
            ('IF-OUT-001', 'Completion Response', 'REST', 'JSON', 'Returns generated text and token usage'),
            ('IF-OUT-002', 'Token Stream', 'WebSocket', 'JSON', 'Streams generated tokens in real-time'),
        ],
    },
    'SEC': {
        'input': [
            ('IF-IN-001', 'Security Validation', 'gRPC', 'Protobuf', 'Validates security tokens and permissions'),
            ('IF-IN-002', 'Threat Events', 'Kafka', 'Avro', 'Receives security events for analysis'),
        ],
        'output': [
            ('IF-OUT-001', 'Validation Response', 'gRPC', 'Protobuf', 'Returns validation results and claims'),
            ('IF-OUT-002', 'Security Alerts', 'Kafka', 'Avro', 'Publishes security alerts and incidents'),
        ],
    },
    'GOV': {
        'input': [
            ('IF-IN-001', 'Governance API', 'REST', 'JSON', 'Receives governance queries and requests'),
            ('IF-IN-002', 'Model Events', 'Kafka', 'Avro', 'Receives model lifecycle events'),
        ],
        'output': [
            ('IF-OUT-001', 'Governance Response', 'REST', 'JSON', 'Returns governance status and decisions'),
            ('IF-OUT-002', 'Compliance Events', 'Kafka', 'Avro', 'Publishes compliance and audit events'),
        ],
    },
    'OBS': {
        'input': [
            ('IF-IN-001', 'Metrics Ingestion', 'gRPC', 'Protobuf', 'Receives metrics from AI systems'),
            ('IF-IN-002', 'Log Ingestion', 'REST', 'JSON', 'Receives structured logs'),
        ],
        'output': [
            ('IF-OUT-001', 'Query API', 'REST', 'JSON', 'Provides metric and log queries'),
            ('IF-OUT-002', 'Alerts', 'Kafka', 'Avro', 'Publishes alerts based on thresholds'),
        ],
    },
    'MLO': {
        'input': [
            ('IF-IN-001', 'Pipeline Trigger', 'REST', 'JSON', 'Triggers ML pipeline execution'),
            ('IF-IN-002', 'Model Artifacts', 'S3', 'Binary', 'Receives model artifacts for registration'),
        ],
        'output': [
            ('IF-OUT-001', 'Pipeline Status', 'REST', 'JSON', 'Returns pipeline execution status'),
            ('IF-OUT-002', 'Model Events', 'Kafka', 'Avro', 'Publishes model lifecycle events'),
        ],
    },
    'INF': {
        'input': [
            ('IF-IN-001', 'Prediction Request', 'REST/gRPC', 'JSON/Protobuf', 'Receives prediction requests with features'),
            ('IF-IN-002', 'Batch Predictions', 'Kafka', 'Avro', 'Receives batch prediction requests'),
        ],
        'output': [
            ('IF-OUT-001', 'Prediction Response', 'REST/gRPC', 'JSON/Protobuf', 'Returns predictions with confidence scores'),
            ('IF-OUT-002', 'Prediction Events', 'Kafka', 'Avro', 'Publishes predictions for downstream processing'),
        ],
    },
    'CNV': {
        'input': [
            ('IF-IN-001', 'Message API', 'REST', 'JSON', 'Receives user messages and context'),
            ('IF-IN-002', 'Channel Events', 'Kafka', 'Avro', 'Receives events from messaging channels'),
        ],
        'output': [
            ('IF-OUT-001', 'Response API', 'REST', 'JSON', 'Returns bot responses with actions'),
            ('IF-OUT-002', 'Conversation Events', 'Kafka', 'Avro', 'Publishes conversation events'),
        ],
    },
    'DOC': {
        'input': [
            ('IF-IN-001', 'Document Upload', 'REST', 'Multipart', 'Receives documents for processing'),
            ('IF-IN-002', 'Processing Request', 'Kafka', 'Avro', 'Receives batch processing requests'),
        ],
        'output': [
            ('IF-OUT-001', 'Extraction Results', 'REST', 'JSON', 'Returns extracted data and classifications'),
            ('IF-OUT-002', 'Document Events', 'Kafka', 'Avro', 'Publishes document processing events'),
        ],
    },
    'BAT': {
        'input': [
            ('IF-IN-001', 'Job Submission', 'REST', 'JSON', 'Receives batch job configurations'),
            ('IF-IN-002', 'Schedule Trigger', 'Cron', 'N/A', 'Receives scheduled execution triggers'),
        ],
        'output': [
            ('IF-OUT-001', 'Job Status', 'REST', 'JSON', 'Returns job execution status and results'),
            ('IF-OUT-002', 'Batch Events', 'Kafka', 'Avro', 'Publishes batch execution events'),
        ],
    },
}

# Default interfaces for undefined categories
DEFAULT_INTERFACES = {
    'input': [
        ('IF-IN-001', 'Service API', 'REST', 'JSON', 'Primary service interface for requests'),
        ('IF-IN-002', 'Event Consumer', 'Kafka', 'Avro', 'Consumes events from upstream systems'),
    ],
    'output': [
        ('IF-OUT-001', 'Service Response', 'REST', 'JSON', 'Returns service responses'),
        ('IF-OUT-002', 'Event Producer', 'Kafka', 'Avro', 'Publishes events for downstream systems'),
    ],
}

# Data contract templates by category
CATEGORY_DATA_CONTRACTS = {
    'AGT': {
        'input': '''# Agent task request schema
input_schema:
  type: object
  properties:
    task_id:
      type: string
      description: "Unique identifier for the task"
    goal:
      type: string
      description: "Natural language description of the task goal"
    context:
      type: object
      description: "Additional context and constraints for task execution"
    tools:
      type: array
      items:
        type: string
      description: "List of allowed tool identifiers"
  required:
    - task_id
    - goal''',
        'output': '''# Agent task response schema
output_schema:
  type: object
  properties:
    task_id:
      type: string
      description: "Task identifier matching the request"
    status:
      type: string
      enum: [completed, failed, pending]
      description: "Task execution status"
    result:
      type: object
      description: "Task execution result and artifacts"
    steps:
      type: array
      description: "Execution steps and tool invocations"
    metadata:
      type: object
      description: "Execution metadata including duration and token usage"''',
    },
    'GEN': {
        'input': '''# LLM completion request schema
input_schema:
  type: object
  properties:
    prompt:
      type: string
      description: "The prompt text for generation"
    model:
      type: string
      description: "Model identifier to use"
    max_tokens:
      type: integer
      description: "Maximum tokens to generate"
    temperature:
      type: number
      description: "Sampling temperature (0-1)"
    system_prompt:
      type: string
      description: "Optional system prompt for context"
  required:
    - prompt''',
        'output': '''# LLM completion response schema
output_schema:
  type: object
  properties:
    completion:
      type: string
      description: "Generated text response"
    model:
      type: string
      description: "Model used for generation"
    usage:
      type: object
      properties:
        prompt_tokens:
          type: integer
        completion_tokens:
          type: integer
        total_tokens:
          type: integer
      description: "Token usage statistics"
    finish_reason:
      type: string
      description: "Reason for completion termination"''',
    },
    'INF': {
        'input': '''# Prediction request schema
input_schema:
  type: object
  properties:
    model_id:
      type: string
      description: "Model identifier for prediction"
    features:
      type: object
      description: "Feature values keyed by feature name"
    request_id:
      type: string
      description: "Unique request identifier for tracing"
    options:
      type: object
      description: "Optional inference parameters"
  required:
    - model_id
    - features''',
        'output': '''# Prediction response schema
output_schema:
  type: object
  properties:
    request_id:
      type: string
      description: "Request identifier matching input"
    prediction:
      type: object
      description: "Prediction results with scores"
    confidence:
      type: number
      description: "Prediction confidence score"
    model_version:
      type: string
      description: "Model version used for prediction"
    latency_ms:
      type: integer
      description: "Inference latency in milliseconds"''',
    },
    'CNV': {
        'input': '''# Conversation message schema
input_schema:
  type: object
  properties:
    conversation_id:
      type: string
      description: "Unique conversation identifier"
    message:
      type: string
      description: "User message text"
    channel:
      type: string
      description: "Source channel (web, mobile, voice)"
    user_context:
      type: object
      description: "User profile and session context"
  required:
    - conversation_id
    - message''',
        'output': '''# Conversation response schema
output_schema:
  type: object
  properties:
    conversation_id:
      type: string
      description: "Conversation identifier"
    response:
      type: string
      description: "Bot response text"
    intent:
      type: string
      description: "Detected user intent"
    entities:
      type: array
      description: "Extracted entities from message"
    actions:
      type: array
      description: "Suggested actions or quick replies"
    handoff_required:
      type: boolean
      description: "Whether human handoff is needed"''',
    },
    'DOC': {
        'input': '''# Document processing request schema
input_schema:
  type: object
  properties:
    document_id:
      type: string
      description: "Unique document identifier"
    document_type:
      type: string
      description: "Expected document type hint"
    content:
      type: string
      format: base64
      description: "Base64 encoded document content"
    extraction_config:
      type: object
      description: "Fields and rules for extraction"
  required:
    - document_id
    - content''',
        'output': '''# Document processing result schema
output_schema:
  type: object
  properties:
    document_id:
      type: string
      description: "Document identifier"
    classification:
      type: object
      description: "Document type and confidence"
    extracted_data:
      type: object
      description: "Extracted field values"
    validation_results:
      type: array
      description: "Data validation outcomes"
    quality_score:
      type: number
      description: "Overall extraction quality score"''',
    },
}

# Default data contract
DEFAULT_DATA_CONTRACT = {
    'input': '''# Service request schema
input_schema:
  type: object
  properties:
    request_id:
      type: string
      description: "Unique request identifier"
    payload:
      type: object
      description: "Request-specific payload data"
    metadata:
      type: object
      description: "Request metadata and tracing info"
  required:
    - request_id
    - payload''',
    'output': '''# Service response schema
output_schema:
  type: object
  properties:
    request_id:
      type: string
      description: "Request identifier for correlation"
    status:
      type: string
      description: "Processing status"
    result:
      type: object
      description: "Processing result data"
    metadata:
      type: object
      description: "Response metadata and timing"''',
}


def get_abb_info(abb_file):
    """Extract ABB ID, name, and category from file."""
    filename = abb_file.name
    match = re.match(r'(ABB-([A-Z]+)-\d+)-(.+)-v\d+\.\d+\.\d+\.md', filename)
    if match:
        abb_id = match.group(1)
        category = match.group(2)
        abb_name = match.group(3).replace('-', ' ')
        return abb_id, category, abb_name
    return None, None, None


def get_abb_description(abb_file):
    """Extract existing description from ABB file."""
    with open(abb_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find description in section 1.1
    match = re.search(r'\*\*Description\*\*:\s*\n(.+?)(?:\n\n|\n###)', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def generate_responsibilities(category, abb_name):
    """Generate key responsibilities based on category and ABB name."""
    base_responsibilities = CATEGORY_RESPONSIBILITIES.get(category, [
        'Provide core functionality as defined by capability mapping',
        'Integrate with related platform components',
        'Support monitoring and observability requirements',
    ])

    # Take first 3 or customize based on ABB name
    responsibilities = base_responsibilities[:3]

    # Add ABB-specific responsibility based on name patterns
    abb_name_lower = abb_name.lower()
    if 'registry' in abb_name_lower:
        responsibilities.append('Maintain registry of registered items with metadata and versioning')
    elif 'monitor' in abb_name_lower:
        responsibilities.append('Track and alert on key metrics and thresholds')
    elif 'engine' in abb_name_lower:
        responsibilities.append('Execute core processing logic with high performance')
    elif 'gateway' in abb_name_lower:
        responsibilities.append('Manage request routing and access control')
    elif 'store' in abb_name_lower:
        responsibilities.append('Provide reliable storage and retrieval with appropriate durability')
    elif 'pipeline' in abb_name_lower:
        responsibilities.append('Orchestrate multi-step processing workflows')
    elif 'service' in abb_name_lower:
        responsibilities.append('Expose managed service capabilities via well-defined APIs')

    return responsibilities[:4]  # Return up to 4 responsibilities


def generate_scope(category, abb_name):
    """Generate in-scope and out-of-scope items."""
    scope_def = CATEGORY_SCOPE.get(category, DEFAULT_SCOPE)

    in_scope = scope_def['in_scope'][:4]
    out_scope = scope_def['out_scope'][:3]

    return in_scope, out_scope


def generate_dependencies(category, abb_id):
    """Generate upstream and downstream dependencies."""
    deps = CATEGORY_DEPENDENCIES.get(category, {
        'upstream': [('OBS-001', 'Observability Platform', 'Required', 'Provides monitoring and logging infrastructure')],
        'downstream': [],
    })

    upstream = []
    downstream = []

    for dep in deps.get('upstream', []):
        dep_id = f"ABB-{dep[0]}"
        if dep_id != abb_id:  # Don't include self-reference
            upstream.append((dep_id, dep[1], dep[2], dep[3]))

    for dep in deps.get('downstream', []):
        dep_id = f"ABB-{dep[0]}"
        if dep_id != abb_id:
            downstream.append((dep_id, dep[1], dep[2], dep[3]))

    return upstream, downstream


def generate_interfaces(category):
    """Generate input and output interfaces."""
    interfaces = CATEGORY_INTERFACES.get(category, DEFAULT_INTERFACES)
    return interfaces.get('input', DEFAULT_INTERFACES['input']), interfaces.get('output', DEFAULT_INTERFACES['output'])


def generate_data_contracts(category):
    """Generate input and output data contracts."""
    contracts = CATEGORY_DATA_CONTRACTS.get(category, DEFAULT_DATA_CONTRACT)
    return contracts.get('input', DEFAULT_DATA_CONTRACT['input']), contracts.get('output', DEFAULT_DATA_CONTRACT['output'])


def update_section_1(content, abb_id, category, abb_name, description):
    """Update section 1 (ABB Overview) with meaningful content."""
    cat_def = CATEGORY_DEFINITIONS.get(category, {
        'full_name': category,
        'business_purpose': 'Enable AI platform capabilities that support business objectives.',
        'technical_purpose': 'Provide technical infrastructure and services for AI workloads.',
    })

    business_purpose = cat_def['business_purpose']
    technical_purpose = cat_def['technical_purpose']

    responsibilities = generate_responsibilities(category, abb_name)
    in_scope, out_scope = generate_scope(category, abb_name)

    # Build section 1.2 content
    section_1_2 = f"""**Business Purpose**:
{business_purpose}

**Technical Purpose**:
{technical_purpose}

**Key Responsibilities**:
"""
    for resp in responsibilities:
        section_1_2 += f"- {resp}\n"

    # Build section 1.3 content
    section_1_3 = """**In Scope**:
"""
    for item in in_scope:
        section_1_3 += f"- {item}\n"

    section_1_3 += "\n**Out of Scope**:\n"
    for item in out_scope:
        section_1_3 += f"- {item}\n"

    # Replace section 1.2
    pattern_1_2 = r'(### 1\.2 Purpose and Rationale\s*\n)(.*?)(### 1\.3 Scope)'
    match = re.search(pattern_1_2, content, re.DOTALL)
    if match:
        content = content[:match.start(2)] + "\n" + section_1_2.rstrip() + "\n\n" + content[match.start(3):]

    # Replace section 1.3
    pattern_1_3 = r'(### 1\.3 Scope\s*\n)(.*?)(---\s*\n## 2\.)'
    match = re.search(pattern_1_3, content, re.DOTALL)
    if match:
        content = content[:match.start(2)] + "\n" + section_1_3.rstrip() + "\n\n" + content[match.start(3):]

    return content


def update_section_3(content, abb_id, category, abb_name):
    """Update section 3 (Integration Specification) with meaningful content."""
    upstream, downstream = generate_dependencies(category, abb_id)
    input_interfaces, output_interfaces = generate_interfaces(category)
    input_contract, output_contract = generate_data_contracts(category)

    # Build section 3.1 - Dependencies
    section_3_1_upstream = "**Upstream Dependencies** (ABBs this building block depends on):\n\n"
    section_3_1_upstream += "| ABB ID | ABB Name | Dependency Type | Description |\n"
    section_3_1_upstream += "|--------|----------|-----------------|-------------|\n"

    if upstream:
        for dep in upstream:
            section_3_1_upstream += f"| {dep[0]} | {dep[1]} | {dep[2]} | {dep[3]} |\n"
    else:
        section_3_1_upstream += "| *None* | - | - | *This ABB has no upstream dependencies* |\n"

    section_3_1_downstream = "\n**Downstream Consumers** (ABBs that depend on this building block):\n\n"
    section_3_1_downstream += "| ABB ID | ABB Name | Dependency Type | Description |\n"
    section_3_1_downstream += "|--------|----------|-----------------|-------------|\n"

    if downstream:
        for dep in downstream:
            section_3_1_downstream += f"| {dep[0]} | {dep[1]} | {dep[2]} | {dep[3]} |\n"
    else:
        section_3_1_downstream += "| *None identified* | - | - | *Consumers to be documented during implementation* |\n"

    section_3_1 = section_3_1_upstream + section_3_1_downstream

    # Build section 3.2 - Interfaces
    section_3_2_input = "**Input Interfaces**:\n\n"
    section_3_2_input += "| Interface ID | Interface Name | Protocol | Data Format | Description |\n"
    section_3_2_input += "|--------------|----------------|----------|-------------|-------------|\n"
    for iface in input_interfaces:
        section_3_2_input += f"| {iface[0]} | {iface[1]} | {iface[2]} | {iface[3]} | {iface[4]} |\n"

    section_3_2_output = "\n**Output Interfaces**:\n\n"
    section_3_2_output += "| Interface ID | Interface Name | Protocol | Data Format | Description |\n"
    section_3_2_output += "|--------------|----------------|----------|-------------|-------------|\n"
    for iface in output_interfaces:
        section_3_2_output += f"| {iface[0]} | {iface[1]} | {iface[2]} | {iface[3]} | {iface[4]} |\n"

    section_3_2 = section_3_2_input + section_3_2_output

    # Build section 3.3 - Data Contracts
    section_3_3 = f"**Input Data**:\n```yaml\n{input_contract}\n```\n\n"
    section_3_3 += f"**Output Data**:\n```yaml\n{output_contract}\n```\n"

    # Replace section 3.1
    pattern_3_1 = r'(### 3\.1 Dependencies\s*\n)(.*?)(### 3\.2 Interfaces)'
    match = re.search(pattern_3_1, content, re.DOTALL)
    if match:
        content = content[:match.start(2)] + "\n" + section_3_1.rstrip() + "\n\n" + content[match.start(3):]

    # Replace section 3.2
    pattern_3_2 = r'(### 3\.2 Interfaces\s*\n)(.*?)(### 3\.3 Data Contracts)'
    match = re.search(pattern_3_2, content, re.DOTALL)
    if match:
        content = content[:match.start(2)] + "\n" + section_3_2.rstrip() + "\n\n" + content[match.start(3):]

    # Replace section 3.3
    pattern_3_3 = r'(### 3\.3 Data Contracts\s*\n)(.*?)(---\s*\n## 4\.)'
    match = re.search(pattern_3_3, content, re.DOTALL)
    if match:
        content = content[:match.start(2)] + "\n" + section_3_3.rstrip() + "\n\n" + content[match.start(3):]

    return content


def update_abb_file(abb_file):
    """Update sections 1 and 3 in an ABB file."""
    abb_id, category, abb_name = get_abb_info(abb_file)
    if not abb_id:
        return False, "Could not parse ABB info"

    description = get_abb_description(abb_file)

    with open(abb_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update sections
    content = update_section_1(content, abb_id, category, abb_name, description)
    content = update_section_3(content, abb_id, category, abb_name)

    with open(abb_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return True, None


def main():
    print("Updating ABB sections 1 and 3...")
    print(f"ABB Root: {ABB_ROOT}")

    # Find all ABB files
    abb_files = list(ABB_ROOT.glob("**/ABB-*.md"))
    print(f"Found {len(abb_files)} ABB files\n")

    updated = 0
    skipped = 0
    errors = 0

    category_counts = defaultdict(int)

    for abb_file in sorted(abb_files):
        abb_id, category, abb_name = get_abb_info(abb_file)
        if not abb_id:
            print(f"  SKIP: Could not parse ABB info from {abb_file.name}")
            skipped += 1
            continue

        category_counts[category] += 1
        print(f"Processing {abb_id} ({category}): {abb_name}")

        try:
            success, error = update_abb_file(abb_file)
            if success:
                updated += 1
            else:
                print(f"  ERROR: {error}")
                errors += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            errors += 1

    print(f"\nSummary:")
    print(f"  Updated: {updated}")
    print(f"  Skipped: {skipped}")
    print(f"  Errors: {errors}")

    print(f"\nABBs by category:")
    for cat, count in sorted(category_counts.items()):
        cat_name = CATEGORY_DEFINITIONS.get(cat, {}).get('full_name', cat)
        print(f"  {cat} ({cat_name}): {count}")


if __name__ == "__main__":
    main()
