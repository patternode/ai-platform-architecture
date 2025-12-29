# Agentic AI Choice Framework

## Overview

The Agentic AI Choice Framework provides a structured approach to evaluate and select appropriate architectural patterns, technologies, and implementation strategies for autonomous AI systems. This framework identifies seven critical dimensions that must be considered when designing and deploying agentic AI solutions, each with specific requirements and directional alignment options ranging from basic implementations to advanced enterprise-grade solutions.

## Framework Dimensions

The dimensions, dimension requirements and directional alignment options.

| **Dimension** | **Requirements** | 1 | 2 | 3 | 4 |
|---------------|------------------|-----------------------------------|------------------------|-------------------------------------|-----------------------------------|
| **1. Agentic software development** | **Aligns with modern LLM tooling**; reduces overhead from mismatch with legacy languages | **Python-native, Agentic stack** Strands<br>• LangChain/Graph | **Java/.NET wrappers**<br>LLM calls inside existing runtimes | **Vendor-managed Low-Code agents**<br/>• AgentBricks<br> | **Open-Sourced Low-Code agents**<br/>• n8n.io |
| **2. Re-usability approach** | **Reusable framework for agents**; keeps services small and efficient, and track performance (cost, efficiency, accuracy.) | **Centralised starter-kit** repo published for teams to self service | **Centralised Platform-hosted blueprints**<br>CI/CD templates + guardrails via NEF / MLFlow3 | **Catalogue of reusable artefacts** curated with use case specifics i.e. MCP config, context engineering patterns | **Bring-your-own w/ gated review**<br>Freedom, but pass risk gates |
| **3. Agent hosting** | Secure hosting and running of each agent with specific controls for access mgmt., tools interactions and observability | Federated hosting for each team to deploy and manage via NEF using any compute offering | Centrally managed blueprint with gated for the blueprint running, and authoring of agents | Centrally authored and deployed agents, with federated hosting for execution runtime<br>• AWS AgentCore<br>• Alternate hosting TBC to test portability | Vendor-managed hosting environment, with centrally governed controls<br>• AgentBricks on top of existing Databricks<br>Note: Currently hosted in US region |
| **4. Agent governance** | Rules and policies to continuously evaluate the behaviour of agents against intent, both online with preventative controls, and offline on trends | Localised governance and evaluation models within each runtime option | Decouple Agent authoring, and allow for distributed model governance to go with runtime | Centralised Agent authoring, with a well defined AgentOps governance model with a common model access approach | Vendor-managed AgentOps governance model to support both high code and low code options |
| **5. Agent Runtime coordination** | Enables scalable workflows with clear handoff logic with short- and long-term memory | Stateless REST endpoint<br>Call-per-query | Ephemeral stateful<br>Short-lived memory in request | Long-running message-driven with persistent memory | Event-driven background worker<br>queue based |
| **6. Protocols / Inter-agent Frameworks** | Simplifies orchestration and enables scalable multi-agent systems | Open standard protocols<br>• MCP + OTEL<br>• A2A (watch) | Framework-native graph / DAG<br>e.g. LangGraph, Crew | Enterprise message bus<br>Kafka (existing) / RedPanda (explore) | Plain REST / gRPC micro-APIs<br>One endpoint per capability |
| **7. Observability & Evaluation** | Keep proof points aligned to real-world quality bars with measures in place to highlight business value | Trace-level structured logging<br>Spans, embeddings, vector traces<br>• Enterprise Open Tel. | Offline batch eval<br>Synthetic or historical tasks nightly<br>• mlFlow 3.0 on Databricks | Continuous online eval + guardrails<br>A/B tests, reward models<br>• Leverage native | Manual spot-check audits<br>Risk & compliance review boards |

## Detailed Framework Analysis

### 1. Agentic Software Development

**Purpose**: This dimension addresses the fundamental technology stack and development approach for building agentic AI systems.

**Requirements**: The framework emphasizes alignment with modern Large Language Model (LLM) tooling while minimizing overhead from legacy language mismatches. This ensures that development teams can leverage the latest AI capabilities without being constrained by outdated technological foundations.

**Directional Alignment Options**:

- **Python-native, Agentic stack**: Represents the most modern approach, utilizing frameworks like Strands and LangChain/Graph that are specifically designed for agentic AI development. This option provides the most direct integration with contemporary LLM tooling and offers maximum flexibility for advanced AI implementations.

- **Java/.NET wrappers**: Accommodates organizations with existing enterprise infrastructure by enabling LLM calls within established runtimes. This approach balances innovation with legacy system compatibility, though it may introduce some overhead.

- **Vendor-managed Low-Code agents**: Offers pre-built solutions like AgentBricks and n8n.io that reduce development complexity while maintaining professional-grade capabilities. This option accelerates time-to-market for organizations seeking rapid deployment.

- **Open-Sourced Low-Code agents**: Provides community-driven alternatives that offer cost-effectiveness and customization potential, though they may require more technical expertise to implement and maintain.

### 2. Re-usability Approach

**Purpose**: This dimension focuses on creating sustainable, efficient agent development practices that promote consistency and performance tracking across the organization.

**Requirements**: The framework mandates reusable frameworks that keep services small and efficient while enabling comprehensive performance tracking across cost, efficiency, and accuracy metrics.

**Directional Alignment Options**:

- **Centralized starter-kit repo**: Enables team self-service through standardized templates and components, promoting consistency while maintaining development autonomy.

- **Centralized Platform-hosted blueprints**: Provides enterprise-grade templates with integrated CI/CD pipelines and guardrails through NEF/MLFlow3, ensuring quality and compliance.

- **Catalogue of reusable artifacts**: Offers curated, use-case-specific components including MCP configurations and context engineering patterns, enabling rapid assembly of specialized solutions.

- **Bring-your-own with gated review**: Balances freedom and innovation with risk management through structured review processes, allowing teams to introduce new approaches while maintaining governance.

### 3. Agent Hosting

**Purpose**: This dimension addresses the critical infrastructure requirements for securely deploying and operating agentic AI systems at scale.

**Requirements**: Secure hosting with granular controls for access management, tool interactions, and comprehensive observability across all agent operations.

**Directional Alignment Options**:

- **Federated hosting**: Enables teams to deploy and manage agents using any compute offering through NEF, providing maximum flexibility and team autonomy.

- **Centrally managed blueprint**: Offers standardized deployment patterns with gated access controls for both blueprint execution and agent authoring, ensuring consistency and security.

- **Centrally authored with federated execution**: Combines centralized development with distributed runtime hosting, utilizing platforms like AWS AgentCore while maintaining execution flexibility.

- **Vendor-managed hosting**: Provides fully managed environments with centralized governance, such as AgentBricks on Databricks, though it may introduce geographic or vendor lock-in considerations.

### 4. Agent Governance

**Purpose**: This dimension establishes the frameworks and processes necessary to ensure agent behavior aligns with organizational intent and regulatory requirements.

**Requirements**: Comprehensive rules and policies for continuous evaluation of agent behavior, incorporating both real-time preventative controls and offline trend analysis.

**Directional Alignment Options**:

- **Localized governance**: Implements evaluation models within each runtime environment, providing immediate feedback and control while maintaining operational independence.

- **Decoupled authoring with distributed governance**: Separates agent development from governance implementation, allowing for flexible deployment models while maintaining consistent oversight.

- **Centralized authoring with unified governance**: Provides comprehensive AgentOps governance through standardized model access approaches, ensuring consistency and compliance across all agents.

- **Vendor-managed governance**: Leverages external platforms to provide governance capabilities for both high-code and low-code implementations, reducing internal overhead while maintaining control.

### 5. Agent Runtime Coordination

**Purpose**: This dimension defines how agents coordinate and communicate to enable complex, scalable workflows with appropriate memory management.

**Requirements**: Support for scalable workflows with clear handoff logic, incorporating both short-term operational memory and long-term strategic memory capabilities.

**Directional Alignment Options**:

- **Stateless REST endpoint**: Provides simple, scalable interactions through call-per-query patterns, suitable for basic agent interactions with minimal state requirements.

- **Ephemeral stateful**: Enables short-lived memory within request contexts, supporting more complex interactions while maintaining system simplicity.

- **Long-running message-driven**: Supports persistent memory and complex workflows through message-driven architectures, enabling sophisticated multi-step processes.

- **Event-driven background worker**: Provides queue-based processing for complex, asynchronous workflows that require robust state management and coordination.

### 6. Protocols / Inter-agent Frameworks

**Purpose**: This dimension establishes the communication and coordination mechanisms that enable effective multi-agent system orchestration.

**Requirements**: Simplified orchestration capabilities that support scalable multi-agent systems through standardized communication protocols and coordination patterns.

**Directional Alignment Options**:

- **Open standard protocols**: Utilizes industry standards like MCP + OTEL and A2A for maximum interoperability and future-proofing.

- **Framework-native graph/DAG**: Leverages specialized frameworks like LangGraph and Crew for sophisticated workflow orchestration with built-in coordination capabilities.

- **Enterprise message bus**: Integrates with existing enterprise infrastructure through platforms like Kafka or emerging alternatives like RedPanda for robust, scalable communication.

- **Plain REST/gRPC micro-APIs**: Provides simple, standardized communication through one endpoint per capability, ensuring clarity and maintainability.

### 7. Observability & Evaluation

**Purpose**: This dimension ensures that agent performance and behavior can be effectively monitored, evaluated, and improved over time.

**Requirements**: Alignment with real-world quality standards through comprehensive measurement systems that demonstrate clear business value and operational effectiveness.

**Directional Alignment Options**:

- **Trace-level structured logging**: Provides comprehensive observability through spans, embeddings, and vector traces using Enterprise OpenTelemetry for detailed performance analysis.

- **Offline batch evaluation**: Enables systematic assessment through synthetic or historical tasks using platforms like MLFlow 3.0 on Databricks for consistent quality measurement.

- **Continuous online evaluation**: Implements real-time assessment with guardrails, A/B testing, and reward models for immediate feedback and optimization.

- **Manual spot-check audits**: Provides human oversight through risk and compliance review boards for high-stakes or regulated environments where human judgment is essential.

## Implementation Considerations

### Strategic Alignment

Organizations should select options across dimensions based on their specific context, including:

- **Technical maturity**: Current development capabilities and infrastructure
- **Risk tolerance**: Regulatory requirements and organizational risk appetite  
- **Resource availability**: Development team skills and available budget
- **Timeline constraints**: Urgency of deployment and time-to-value requirements
- **Scalability needs**: Expected growth and complexity evolution

### Integration Patterns

The framework supports various integration patterns:

- **Uniform approach**: Selecting the same directional alignment across all dimensions for consistency
- **Hybrid approach**: Mixing different alignments based on specific organizational needs and constraints
- **Evolutionary approach**: Starting with simpler options and progressing toward more sophisticated implementations over time

### Success Metrics

Organizations should establish clear metrics for evaluating framework implementation success:

- **Performance metrics**: Cost efficiency, accuracy, response time
- **Operational metrics**: Deployment frequency, error rates, recovery time
- **Business metrics**: Value delivered, user satisfaction, competitive advantage
- **Governance metrics**: Compliance adherence, risk mitigation, audit readiness
