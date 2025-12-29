# Glossary

Common terms and definitions used throughout the AI Platform Architecture repository.

## A

**ABB (Architecture Building Block)**
: A vendor-agnostic, logical component that defines WHAT is needed to realize platform capabilities. ABBs are stable and describe functional requirements without specifying implementation technologies.

**ADR (Architecture Decision Record)**
: A document that captures an important architectural decision, including context, options considered, decision made, and consequences.

**Agent**
: An autonomous AI system that can perceive its environment, make decisions, and take actions to achieve specific goals, often using LLMs and tools.

**API Gateway**
: An architectural component that acts as a reverse proxy to accept API calls, aggregate services, and return results.

## B

**Bounded Context**
: A logical boundary within which a particular domain model is defined and applicable. Part of Domain-Driven Design (DDD).

**Building Block**
: A reusable architecture component that can be combined with other building blocks to create solutions. See ABB and SBB.

## C

**Capability**
: A business outcome or function that the platform enables, independent of how it's implemented. Capabilities are organized hierarchically (L0, L1, L2).

**C4 Model**
: A notation for visualizing software architecture at different levels of abstraction (Context, Container, Component, Code).

## D

**Domain**
: A sphere of knowledge or activity. In DDD, refers to the business problem space.

**Drift Detection**
: The process of monitoring machine learning models to identify when their performance degrades over time due to changes in data patterns.

## E

**Embedding**
: A dense vector representation of data (text, images, etc.) in a continuous vector space, often used for semantic search and similarity.

**Epic**
: A large body of work that can be broken down into features and stories, typically delivered over 1-6 months.

## F

**Feature**
: A distinct, shippable capability or functionality, typically delivered within 2-6 weeks.

**Feature Store**
: A centralized repository for storing, managing, and serving machine learning features for training and inference.

## G

**Guardrails**
: Safety mechanisms that constrain AI system behavior to prevent harmful or undesired outputs.

## I

**Inference**
: The process of using a trained machine learning model to make predictions on new data.

**IaC (Infrastructure as Code)**
: Managing and provisioning infrastructure through machine-readable definition files rather than manual processes.

## L

**LLM (Large Language Model)**
: A type of AI model trained on vast amounts of text data, capable of understanding and generating human-like text.

**LLM Gateway**
: An architectural component that provides centralized access to multiple LLM providers, handling routing, security, monitoring, and cost management.

## M

**MLOps**
: A set of practices that combines Machine Learning, DevOps, and Data Engineering to deploy and maintain ML systems in production reliably and efficiently.

**Model Registry**
: A centralized repository for storing, versioning, and managing machine learning models and their metadata.

## O

**Observability**
: The ability to understand the internal state of a system based on its external outputs, typically through metrics, logs, and traces.

## P

**Pattern**
: A reusable solution to a common problem in software architecture, providing proven approaches to recurring challenges.

**PII (Personally Identifiable Information)**
: Information that can be used to identify an individual, requiring special handling for privacy and compliance.

**Prompt**
: The input text or instructions provided to an LLM to elicit a desired response.

**Prompt Engineering**
: The practice of designing and refining prompts to achieve optimal results from LLMs.

## R

**RAG (Retrieval-Augmented Generation)**
: A pattern that enhances LLM responses by retrieving relevant information from external knowledge sources before generating output.

**Reference Architecture**
: A template solution architecture that demonstrates best practices and provides a standardized approach for implementing systems.

## S

**SBB (Solution Building Block)**
: A concrete, vendor-specific implementation of an ABB, including specific technologies, versions, and configurations.

**Semantic Search**
: A search technique that understands the intent and contextual meaning of search queries, often using vector embeddings.

**Service Mesh**
: An infrastructure layer that manages service-to-service communication, providing features like load balancing, service discovery, and observability.

**Spike**
: A time-boxed research activity to investigate a question or gather information, producing knowledge rather than production code.

## T

**Theme**
: A strategic investment area that organizes related epics, typically spanning 12-24 months.

**Traceability**
: The ability to track relationships between architecture artifacts, from vision through capabilities to implementation.

## V

**Vector Database**
: A specialized database optimized for storing and querying vector embeddings, enabling semantic search and similarity matching.

**Vector Store**
: See Vector Database.

## Z

**Zero Trust**
: A security model that assumes no implicit trust and verifies every access request regardless of location or network.

---

## Acronyms

| Acronym | Full Term |
|---------|-----------|
| ABB | Architecture Building Block |
| ADR | Architecture Decision Record |
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| CI/CD | Continuous Integration/Continuous Deployment |
| DDD | Domain-Driven Design |
| GPU | Graphics Processing Unit |
| IaC | Infrastructure as Code |
| LLM | Large Language Model |
| ML | Machine Learning |
| MLOps | Machine Learning Operations |
| PII | Personally Identifiable Information |
| RAG | Retrieval-Augmented Generation |
| REST | Representational State Transfer |
| SBB | Solution Building Block |
| SDK | Software Development Kit |

---

*This glossary is a living document. Please submit pull requests to add or clarify terms.*
