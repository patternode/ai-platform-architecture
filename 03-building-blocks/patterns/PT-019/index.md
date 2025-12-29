# Graph-Enhanced Retrieval Augmented Generation (GraphRAG) Pattern

## Document Control

| Property | Value |
|----------|-------|
| **Pattern ID** | `PT-019` |
| **Pattern Name** | GraphRAG Pattern |
| **Version** | `1.1.0` |
| **Status** | `Draft` |
| **Created Date** | `2025-12-07` |
| **Last Modified** | `2025-12-26` |
| **Pattern Category** | `GenAI` |
| **Maturity Level** | `Emerging` |

---

## 1. Pattern Overview

### 1.1 Pattern Name and Classification

**Pattern Name**: Graph-Enhanced Retrieval Augmented Generation (GraphRAG)

**Short Name**: GraphRAG

**Pattern Category**: GenAI

**Pattern Type**: AI/ML Architecture, Knowledge Management

### 1.2 Intent and Context

**Intent Statement**:
Enhance Large Language Model (LLM) responses with structured knowledge graphs that capture entity relationships, enabling superior reasoning over complex interconnected data compared to traditional vector-only RAG approaches.

**Problem Statement**:
Traditional Retrieval Augmented Generation (RAG) using vector similarity search alone has significant limitations when dealing with complex enterprise queries:
- **Lost Relationships**: Vector embeddings capture semantic similarity but lose explicit entity relationships (e.g., "Customer X is connected to Company Y which has exposure to Risk Z").
- **Multi-Hop Reasoning Failure**: Cannot answer questions requiring multiple steps of reasoning across connected entities.
- **Context Fragmentation**: Documents chunked for embedding lose structural context and cross-document relationships.
- **Hallucination on Complex Queries**: LLMs fabricate relationships when vector retrieval returns semantically similar but unrelated content.
- **Poor Performance on Structured Data**: Financial data with rich entity relationships (customers, accounts, transactions, risks) poorly served by vector-only approaches.

**Context**:
Organizations have vast amounts of structured and semi-structured data with rich entity relationships: customers linked to accounts, accounts linked to transactions, transactions linked to merchants, merchants linked to risk categories, etc. GraphRAG combines the semantic understanding of LLMs with the precise relational reasoning of knowledge graphs to enable complex queries like:

- "What is the total exposure across all customers connected to companies in the construction sector?"
- "Trace the relationship path between this suspicious transaction and known fraud patterns"
- "Find all regulatory documents relevant to this customer's product portfolio and compliance history"

**Forces**:
- **Accuracy vs. Latency**: Graph traversal adds latency but significantly improves accuracy for complex queries
- **Knowledge Maintenance vs. Freshness**: Graph construction requires investment but enables real-time relationship reasoning
- **Complexity vs. Capability**: More complex architecture enables more sophisticated use cases
- **Vector Similarity vs. Explicit Relationships**: Both are needed for comprehensive knowledge retrieval
- **Structured vs. Unstructured Data**: GraphRAG bridges both data types effectively

### 1.3 Pattern Maturity and Industry Adoption

**Maturity Level**: Emerging

**Industry Adoption**:
- **Adoption Rate**: Approximately 25-35% of enterprises implementing RAG are exploring or piloting GraphRAG as of late 2025, up from 15-25% in early 2025
- **Reference Implementations**:
  - Microsoft GraphRAG (open-source framework released 2024, enterprise adoption 2025) - now integrated with Microsoft Discovery platform
  - JPMorgan Chase (financial knowledge graphs for regulatory compliance)
  - Goldman Sachs (entity relationship graphs for risk assessment)
  - Bloomberg (financial entity resolution and relationship mapping)
  - LinkedIn (reduced ticket resolution time from 40 hours to 15 hours - 63% improvement)
  - FalkorDB implementations (documented 90% hallucination reduction vs. traditional RAG)
- **Timeframe**: Evolved from research (2023) to frameworks (2024) to production implementations and benchmarking standards (2025)

**Standards Alignment**:
- W3C RDF and SPARQL: Semantic web standards for knowledge representation
- OpenCypher: Graph query language standard
- LangChain/LlamaIndex: Integration with popular RAG frameworks
- ISO 27001: Information security for knowledge management systems
- TOGAF 10: Knowledge management architecture patterns

**2025 State of the Art**:
- **Microsoft GraphRAG**: Community summarization, hierarchical indexing, global/local search - now available via Microsoft Discovery platform
- **LazyGraphRAG** (Microsoft, Nov 2024-2025): Zero upfront indexing cost approach with 0.1% of GraphRAG indexing costs and 700x lower query costs while matching quality
- **LightRAG** (HKUST, EMNLP 2025): Simple and fast dual-level retrieval with entity/relationship-based retrieval instead of chunk-based
- **HippoRAG 2** (OSU/UIUC, ICML 2025): Neurobiologically-inspired long-term memory framework with 7% improvement on associative memory tasks
- **Neo4j GenAI Stack**: Native graph database with LLM integration and official neo4j-graphrag-python package
- **Amazon Neptune Analytics**: Managed graph database with vector search
- **LlamaIndex Knowledge Graphs**: Python framework for graph-based RAG
- **Hybrid Approaches**: Combining vector, graph, and keyword search for optimal retrieval

**Late 2025 Emerging Frameworks**:
- **LinearRAG** (PolyU, Oct 2025): Relation-free graph construction with zero LLM token consumption and linear complexity
- **E²GraphRAG** (2025): Streamlined framework achieving 10x speedup over LightRAG with state-of-the-art effectiveness
- **ArchRAG** (2025): Attributed community-based hierarchical RAG with 10% higher accuracy and 250x token savings vs. GraphRAG
- **HopRAG** (ACL Findings 2025): Multi-hop reasoning via LLM-generated pseudo-query edges, 76.78% higher accuracy vs. conventional methods
- **StepChain GraphRAG** (2025): BFS reasoning flow with on-the-fly knowledge graph parsing, state-of-the-art on MuSiQue and HotpotQA
- **DIGIMON** (2025): Unified modular graph-based RAG framework with flexible benchmarking support

**Benchmarking Standard**:
- **GraphRAG-Bench** (May 2025): Comprehensive benchmark with 1,018 college-level questions across 16 CS disciplines, evaluating graph construction, retrieval, and generation stages

---

## 2. Architecture Specification

### 2.1 Architecture Building Blocks (ABBs)

**Primary ABBs** (Core components required):

| ABB ID | ABB Name | Purpose in Pattern | Criticality |
|--------|----------|-------------------|-------------|
| [AB-051](../../architecture-building-blocks/abbs/AB-051/AB-051-Vector-Database-v1.0.0.md) | Vector Database | Store document embeddings for semantic similarity search | Critical |
| [AB-050](../../architecture-building-blocks/abbs/AB-050/AB-050-Large-Language-Model-Service-v1.0.0.md) | Large Language Model Service | Generate responses using retrieved context from graph and vectors | Critical |
| [AB-080](../../architecture-building-blocks/abbs/AB-080/AB-080-Knowledge-Base-v1.0.0.md) | Knowledge Base | Store and manage knowledge graph with entity relationships | Critical |
| [AB-052](../../architecture-building-blocks/abbs/AB-052/AB-052-Semantic-Search-Engine-v1.0.0.md) | Semantic Search Engine | Coordinate hybrid retrieval across vector and graph stores | Critical |
| [AB-057](../../architecture-building-blocks/abbs/AB-057/AB-057-Document-Processing-Pipeline-v1.0.0.md) | Document Processing Pipeline | Extract entities and relationships from documents for graph construction | High |
| [AB-034](../../architecture-building-blocks/abbs/AB-034/AB-034-Entity-Extractor-v1.0.0.md) | Entity Extractor | Identify and extract named entities from text (NER) | High |

**Supporting ABBs** (Optional or scenario-specific):

| ABB ID | ABB Name | Purpose in Pattern | When Required |
|--------|----------|-------------------|---------------|
| [AB-059](../../architecture-building-blocks/abbs/AB-059/AB-059-Query-Rewriting-Engine-v1.0.0.md) | Query Rewriting Engine | Decompose complex queries into sub-queries for graph and vector search | For complex multi-hop queries |
| [AB-055](../../architecture-building-blocks/abbs/AB-055/AB-055-Reranking-Engine-v1.0.0.md) | Reranking Engine | Rerank combined graph and vector results for relevance | For high-precision applications |
| [AB-058](../../architecture-building-blocks/abbs/AB-058/AB-058-Citation-Generator-v1.0.0.md) | Citation Generator | Generate source citations from graph paths and documents | For explainable answers |
| [AB-056](../../architecture-building-blocks/abbs/AB-056/AB-056-Self-Critique-Engine-v1.0.0.md) | Self-Critique Engine | Validate LLM responses against graph relationships | For high-stakes applications |
| [AB-054](../../architecture-building-blocks/abbs/AB-054/AB-054-Hybrid-Search-Engine-v1.0.0.md) | Hybrid Search Engine | Combine vector, graph, and keyword search results | For comprehensive retrieval |

**Cross-Cutting ABBs** (Always required):

| ABB ID | ABB Name | Purpose |
|--------|----------|---------|
| [AB-060](../../architecture-building-blocks/abbs/AB-060/AB-060-AI-Model-Registry-v1.0.0.md) | AI Governance Platform | Compliance, risk management, audit for AI responses |
| [AB-112](../../architecture-building-blocks/abbs/AB-112/AB-112-Data-Encryption-Service-v1.0.0.md) | Security & Identity | Authentication, authorization, encryption for knowledge access |
| [AB-096](../../architecture-building-blocks/abbs/AB-096/AB-096-Observability-Platform-v1.0.0.md) | Observability Platform | Monitoring, logging, alerting for RAG pipeline health |
| [AB-105](../../architecture-building-blocks/abbs/AB-105/AB-105-GenAI-Quality-Monitor-v1.0.0.md) | GenAI Quality Monitor | Monitor response quality, hallucination rates, retrieval accuracy |

### 2.2 Pattern Structure

**Architectural Diagram**:

![PT-019 GraphRAG Architecture](Architecture.png)

**Component Interaction Flow**:

![PT-019 GraphRAG Data Flow](Data-Flow.png)

**Key Interactions**:

1. **Document Ingestion & Graph Construction**: Documents processed to extract entities and relationships
   - Protocol: Batch processing pipeline (REST APIs for orchestration)
   - Data Format: PDF, DOCX, HTML → JSON entities → Graph triples (RDF/Property Graph)
   - Latency Target: Batch processing (minutes to hours depending on corpus size)

2. **Entity Extraction & Resolution**: NLP models identify and disambiguate entities
   - Protocol: REST API to Entity Extraction Service
   - Data Format: Text → Named entities with types and confidence scores
   - Latency Target: < 500ms per document chunk

3. **Graph Population**: Entities and relationships stored in knowledge graph
   - Protocol: Graph database API (Cypher/SPARQL/Gremlin)
   - Data Format: Nodes (entities) and edges (relationships) with properties
   - Latency Target: < 100ms per triple insertion

4. **Query Processing**: User query analyzed and decomposed
   - Protocol: REST API
   - Data Format: Natural language query → Query plan (vector search + graph traversal)
   - Latency Target: < 200ms for query planning

5. **Hybrid Retrieval**: Parallel vector similarity and graph traversal
   - Protocol: Vector DB API + Graph DB API
   - Data Format: Embeddings → Similar chunks; Graph queries → Related entities and paths
   - Latency Target: < 1 second for combined retrieval

6. **Context Assembly & LLM Generation**: Retrieved context fed to LLM for response
   - Protocol: LLM API (REST/gRPC)
   - Data Format: Structured context (graph paths + document chunks) → Natural language response
   - Latency Target: < 3 seconds for complete response (streaming supported)

### 2.3 Data Flow

**Data Sources**:
- **Enterprise Documents**: Policies, procedures, regulatory filings, contracts, reports
- **Structured Data**: Customer data, transaction data, product catalogs, organizational hierarchies
- **External Knowledge**: Regulatory databases, industry taxonomies, market data feeds
- **Existing Knowledge Bases**: Wikis, FAQs, support tickets, case management systems

**Data Transformations**:

1. **Document Processing**: Raw documents → Cleaned text → Chunks with metadata
   - Performed by Document Processing Pipeline (AB-057)
   - Chunking strategies: semantic, recursive, sentence-based

2. **Entity Extraction**: Text chunks → Named entities with types (Person, Organization, Product, Risk, etc.)
   - Performed by Entity Extractor (AB-034) using NER models
   - Domain fine-tuned models for relevant entities

3. **Relationship Extraction**: Entity pairs → Relationships with types (works_for, owns, exposed_to, etc.)
   - Performed by LLM-based or rule-based extraction
   - Domain ontology guides relationship types

4. **Graph Construction**: Entities + Relationships → Knowledge graph triples
   - Entity resolution to merge duplicate entities
   - Graph normalization and schema enforcement

5. **Embedding Generation**: Text chunks → Vector embeddings
   - Performed by embedding models (e.g., text-embedding-3-large, bge-large)
   - Stored in Vector Database (AB-051)

6. **Community Detection**: Graph clustering → Entity communities with summaries
   - Microsoft GraphRAG approach: Hierarchical community summarization
   - Enables global queries over entire knowledge base

**Data Sinks**:
- **Knowledge Graph Database**: Neo4j, Amazon Neptune, Azure Cosmos DB (Gremlin)
- **Vector Database**: Pinecone, Weaviate, Qdrant, Azure AI Search
- **Response Cache**: Redis for frequent query results
- **Audit Log**: Complete trace of queries, retrievals, and responses

**Data Governance**:
- **Classification**: Inherited from source documents (Public / Internal / Confidential / Restricted)
- **Retention**: Per document source policy; graph entities follow most restrictive policy
- **Lineage**: Tracked from source document → entity → relationship → query → response
- **Quality**: Entity resolution accuracy, relationship extraction precision, response faithfulness
- **Access Control**: Graph-level and document-level access control with RBAC

### 2.4 Interface Specifications

**Inbound Interfaces** (Inputs to pattern):

| Interface ID | Interface Name | Type | Protocol | Data Format | SLA |
|--------------|---------------|------|----------|-------------|-----|
| IF-IN-001 | Document Ingestion | Batch / API | REST / S3 | PDF, DOCX, HTML, JSON | Batch: 24hr, API: < 5s ack |
| IF-IN-002 | User Query | API | REST / WebSocket | Natural language text | < 100ms acknowledgment |
| IF-IN-003 | Structured Data Feed | Batch / Streaming | REST / Kafka | JSON, CSV | Per source SLA |
| IF-IN-004 | Graph Updates | API | REST / Cypher | JSON / Graph Triples | < 1s for updates |

**Outbound Interfaces** (Outputs from pattern):

| Interface ID | Interface Name | Type | Protocol | Data Format | SLA |
|--------------|---------------|------|----------|-------------|-----|
| IF-OUT-001 | Query Response | API | REST / WebSocket | JSON (answer + citations) | < 5s (streaming available) |
| IF-OUT-002 | Entity Search | API | REST | JSON (entities + relationships) | < 1s |
| IF-OUT-003 | Graph Exploration | API | REST / GraphQL | JSON (subgraph) | < 2s |
| IF-OUT-004 | Analytics Events | Stream | Kafka | JSON (usage metrics) | Real-time |

**Internal Interfaces** (Between ABBs within pattern):

| Interface ID | Source ABB | Target ABB | Protocol | Purpose |
|--------------|-----------|-----------|----------|---------|
| IF-INT-001 | AB-057 Document Pipeline | AB-034 Entity Extractor | REST | Extract entities from document chunks |
| IF-INT-002 | AB-034 Entity Extractor | AB-080 Knowledge Base | Cypher/REST | Populate graph with entities |
| IF-INT-003 | AB-052 Semantic Search | AB-051 Vector Database | REST | Vector similarity search |
| IF-INT-004 | AB-052 Semantic Search | AB-080 Knowledge Base | Cypher | Graph traversal queries |
| IF-INT-005 | AB-052 Semantic Search | AB-050 LLM Service | REST | Generate response from context |
| IF-INT-006 | AB-055 Reranking Engine | AB-050 LLM Service | REST | Cross-encoder reranking |
| IF-INT-007 | AB-059 Query Rewriter | AB-050 LLM Service | REST | Query decomposition |

---

## 3. Pattern Variants and Options

### 3.1 Pattern Variations

**Variant 1: Microsoft GraphRAG (Community Summarization)**
- **When to Use**: Large document corpora requiring global reasoning (enterprise-wide queries)
- **Key Differences**:
  - Hierarchical community detection on knowledge graph
  - Pre-computed community summaries for global search
  - Map-reduce approach for answering global questions
  - Now available via Microsoft Discovery platform for Azure-based deployments
- **Trade-offs**:
  - **Gain**: Superior performance on "What are the main themes across all documents?" type queries
  - **Lose**: Higher indexing cost (community detection and summarization), more complex pipeline
- **2025 Update**: Consider LazyGraphRAG variant (see Variant 5) for cost-sensitive deployments

**Variant 2: Local GraphRAG (Entity-Centric)**
- **When to Use**: Entity-focused queries requiring relationship traversal
- **Key Differences**:
  - Direct graph traversal from query entities
  - No pre-computed summaries; real-time graph exploration
  - Combines with vector search for hybrid retrieval
- **Trade-offs**:
  - **Gain**: Lower indexing overhead, real-time graph updates reflected immediately
  - **Lose**: Less effective for global/thematic queries spanning entire knowledge base

**Variant 3: Hybrid Vector-Graph RAG**
- **When to Use**: Balanced use cases requiring both semantic similarity and relationship reasoning
- **Key Differences**:
  - Query routing: simple queries → vector-only; complex queries → graph + vector
  - Weighted fusion of vector and graph results
  - Adaptive retrieval based on query complexity
- **Trade-offs**:
  - **Gain**: Optimal latency-accuracy trade-off, handles diverse query types
  - **Lose**: More complex query routing logic, requires tuning of fusion weights

**Variant 4: Agentic GraphRAG**
- **When to Use**: Complex multi-step reasoning requiring iterative graph exploration
- **Key Differences**:
  - LLM agent decides graph traversal strategy dynamically
  - Multi-turn retrieval with reasoning traces
  - Can expand search based on intermediate findings
- **Trade-offs**:
  - **Gain**: Most powerful for complex investigative queries (fraud tracing, compliance review)
  - **Lose**: Higher latency (multiple LLM calls), higher cost, harder to predict behavior

**Variant 5: LazyGraphRAG (Cost-Optimized)**
- **When to Use**: Cost-sensitive deployments where full GraphRAG indexing is prohibitive
- **Key Differences**:
  - No prior summarization of source data required
  - Combines best-first and breadth-first search in iterative deepening
  - Indexing costs identical to vector RAG (0.1% of full GraphRAG)
  - Query costs 700x lower than GraphRAG Global Search
- **Trade-offs**:
  - **Gain**: Dramatic cost reduction while matching GraphRAG quality for global queries
  - **Lose**: May have higher query latency due to on-the-fly processing
- **Reference**: Microsoft Research (Nov 2024)

**Variant 6: LightRAG (Speed-Optimized)**
- **When to Use**: Applications requiring fast retrieval with incremental updates
- **Key Differences**:
  - Dual-level retrieval (low-level and high-level knowledge discovery)
  - Entity and relationship retrieval instead of chunk-based
  - Incremental graph updates without full index rebuild
  - Eliminates community-based traversal overhead
- **Trade-offs**:
  - **Gain**: Faster retrieval, lower computational overhead, real-time graph updates
  - **Lose**: Less sophisticated global reasoning than community-based approaches
- **Reference**: HKUST, EMNLP 2025

**Variant 7: HippoRAG 2 (Memory-Optimized)**
- **When to Use**: Long-term memory applications requiring continual learning
- **Key Differences**:
  - Neurobiologically-inspired architecture (artificial neocortex, parahippocampal encoder, open KG)
  - Dense-sparse integration (passage nodes and phrase nodes coexist)
  - Recognition memory via LLM-based filtering
  - Personalized PageRank for multi-hop reasoning
- **Trade-offs**:
  - **Gain**: 7% improvement on associative memory tasks, superior factual and sense-making memory
  - **Lose**: More complex architecture, requires careful tuning of memory components
- **Reference**: OSU/UIUC, ICML 2025

**Variant 8: LinearRAG (Efficiency-Optimized)**
- **When to Use**: Large-scale deployments requiring minimal token consumption
- **Key Differences**:
  - Relation-free graph construction (no explicit relationship extraction)
  - Semantic bridging for multi-hop reasoning in single retrieval pass
  - Zero LLM token consumption during graph construction
  - Linear time and space complexity
- **Trade-offs**:
  - **Gain**: Fastest overall efficiency, zero token usage for graph building
  - **Lose**: May miss nuanced relationships that require explicit extraction
- **Reference**: PolyU, Oct 2025

### 3.2 Composition with Other Patterns

**Commonly Combined With**:

| Pattern | Integration Point | Combined Benefit |
|---------|------------------|------------------|
| PT-005 RAG | GraphRAG extends basic RAG with relationship reasoning | Comprehensive knowledge retrieval: semantic + relational |
| PT-007 Agentic AI | Agent uses GraphRAG for knowledge-intensive tool calls | Agent can reason over complex enterprise knowledge |
| PT-008 Multi-Agent | Specialized graph agent collaborates with other agents | Distributed reasoning across knowledge domains |
| PT-011 IDP | IDP extracts entities for graph; GraphRAG queries processed docs | End-to-end document intelligence pipeline |
| PT-013 Conversational AI | Conversational interface powered by GraphRAG knowledge | Context-aware, relationship-aware chatbot |

**Anti-Patterns** (What NOT to do):

- **Anti-Pattern 1: Graph Without Vector Search**
  - **Why Problematic**: Pure graph queries miss semantically related but lexically different content
  - **Better Approach**: Always combine graph traversal with vector similarity for hybrid retrieval

- **Anti-Pattern 2: Over-Extracting Relationships**
  - **Why Problematic**: Noisy graphs with low-confidence relationships degrade retrieval quality
  - **Better Approach**: Use confidence thresholds, focus on high-value relationship types

- **Anti-Pattern 3: Ignoring Entity Resolution**
  - **Why Problematic**: Duplicate entities fragment knowledge, break relationship paths
  - **Better Approach**: Invest in entity resolution before graph population

- **Anti-Pattern 4: Static Graph Without Updates**
  - **Why Problematic**: Knowledge graph becomes stale, leading to incorrect or outdated answers
  - **Better Approach**: Implement continuous or scheduled graph updates from source systems

- **Anti-Pattern 5: Monolithic Knowledge Graph**
  - **Why Problematic**: Single graph becomes unmanageable, slow, and hard to govern
  - **Better Approach**: Domain-partitioned graphs with cross-domain linking

---

## 4. Implementation Guidance

### 4.1 Key Principles

**1. Hybrid Retrieval by Default**
- Always combine vector similarity search with graph traversal
- Vector search finds semantically relevant content; graph search adds relationship context
- Fusion strategies: reciprocal rank fusion (RRF), weighted score combination, LLM-based selection

**2. Domain-Specific Ontology**
- Define entity types and relationship types specific to the relevant domain
- Entity types: Customer, Account, Transaction, Product, Risk, Regulation, Employee, Branch, etc.
- Relationship types: owns, transacts_with, exposed_to, regulated_by, managed_by, etc.
- Ontology guides extraction and enables structured queries

**3. Incremental Graph Construction**
- Start with high-value entity types and relationships
- Expand ontology based on query patterns and user feedback
- Balance extraction precision vs. coverage

**4. Query Understanding is Critical**
- Invest in query analysis to route appropriately (simple vs. complex)
- Query decomposition for multi-hop questions
- Entity linking from query to graph entities

**5. Explainability and Citations**
- Always provide source attribution (document, graph path, entity)
- Show reasoning trace for complex queries
- Enable users to explore underlying knowledge graph

### 4.2 GraphRAG Pipeline Components

Every GraphRAG implementation MUST include the following components:

| Component | Description | Example |
|-----------|-------------|---------|
| **Document Processor** | Parse, clean, chunk documents | PDF parser → text cleaner → semantic chunker |
| **Entity Extractor** | Identify named entities with types | "Apple" → Organization, "iPhone" → Product |
| **Relationship Extractor** | Identify relationships between entities | "Apple" --offers--> "iPhone" |
| **Entity Resolver** | Merge duplicate entities | "Apple", "Apple Inc.", "Apple Corporation" → same entity |
| **Graph Store** | Persist entities and relationships | Neo4j, Neptune, Cosmos DB |
| **Vector Store** | Persist document embeddings | Pinecone, Weaviate, Qdrant |
| **Query Processor** | Analyze and route queries | Query type classification, entity linking, query decomposition |
| **Hybrid Retriever** | Combine graph and vector results | Graph traversal + vector similarity → merged context |
| **Response Generator** | Generate answers from context | LLM with structured prompt including graph paths and documents |
| **Quality Monitor** | Track retrieval and response quality | Faithfulness, relevance, hallucination detection |

### 4.3 When to Use

**Ideal Scenarios**:
- Complex queries requiring multi-hop reasoning across entities
- Rich entity relationships in source data (customers, accounts, products, risks)
- Regulatory and compliance use cases requiring precise relationship tracing
- Fraud investigation requiring path analysis across transaction networks
- Knowledge management with interconnected documents and policies
- Customer 360 views requiring relationship context

**Not Recommended For**:
- Simple FAQ or single-document Q&A (basic RAG sufficient)
- Highly unstructured creative content with no clear entities
- Real-time streaming queries requiring sub-100ms latency
- Small document collections with no entity relationships
- Use cases where approximate semantic matching is sufficient

### 4.4 Use Cases

**Primary Use Cases** (Direct dependency on GraphRAG):

| Use Case | GraphRAG Application | Key Entity Types |
|----------|---------------------|------------------|
| **[UC-011](../../../01-motivation/03-use-cases/use-cases/UC-011/index.md): Fincrime** | Trace suspicious transaction paths across accounts and entities | Transaction, Account, Customer, Merchant, Alert |
| **[UC-004](../../../01-motivation/03-use-cases/use-cases/UC-004/index.md): Credit Risk** | Analyze exposure relationships across customer networks | Customer, Company, Industry, Exposure, Collateral |
| **[UC-015](../../../01-motivation/03-use-cases/use-cases/UC-015/index.md): Risk Functions** | Navigate regulatory requirements and control relationships | Regulation, Control, Risk, Policy, Audit |
| **[UC-007](../../../01-motivation/03-use-cases/use-cases/UC-007/index.md): Contact Centre** | Knowledge graph of products, policies, and customer context | Product, Policy, FAQ, Procedure, Customer |
| **[UC-020](../../../01-motivation/03-use-cases/use-cases/UC-020/index.md): Controls Testing** | Map controls to risks, regulations, and evidence | Control, Risk, Regulation, Evidence, TestResult |

**Secondary Use Cases** (Benefit from GraphRAG enhancement):

- **[UC-001](../../../01-motivation/03-use-cases/use-cases/UC-001/index.md): Partnership Banking** - Customer relationship networks for referral insights
- **[UC-008](../../../01-motivation/03-use-cases/use-cases/UC-008/index.md): Security AI** - Threat entity relationships and attack path analysis
- **[UC-013](../../../01-motivation/03-use-cases/use-cases/UC-013/index.md): Fraud Ops** - Fraud ring detection via graph analysis
- **[UC-021](../../../01-motivation/03-use-cases/use-cases/UC-021/index.md): Wholesale Underwriting** - Corporate relationship and exposure mapping

### 4.5 Implementation Components

**Technology Stack** (2025 Recommendations):

**Graph Database**:
- **Neo4j** - Leading property graph database with Cypher query language, GenAI extensions
- **Amazon Neptune** - Managed graph database supporting Gremlin and SPARQL, Neptune Analytics for ML
- **Azure Cosmos DB (Gremlin API)** - Globally distributed graph database
- **TigerGraph** - High-performance graph analytics with GraphStudio

**Vector Database**:
- **Pinecone** - Managed vector database with hybrid search
- **Weaviate** - Open-source vector database with native graph relationships
- **Qdrant** - High-performance vector similarity search
- **Azure AI Search** - Enterprise search with vector and semantic capabilities
- **MongoDB Atlas Vector Search** - Document database with native vector search, supports unified storage for documents, vectors, and metadata
- **pgvector** - PostgreSQL extension for vector similarity

**LLM Services**:
- **Azure OpenAI (GPT-4o, GPT-4 Turbo)** - Enterprise-grade LLM with compliance features
- **AWS Bedrock (Claude, Titan)** - Multi-model access with VPC integration
- **Anthropic Claude** - Strong reasoning capabilities for complex queries
- **OpenAI API** - Latest models with function calling for graph queries

**Graph Construction Frameworks**:
- **Microsoft GraphRAG** - Open-source framework for entity extraction and community summarization; LazyGraphRAG variant for cost-sensitive deployments
- **LightRAG** (HKUST) - Simple and fast RAG with dual-level retrieval, EMNLP 2025
- **Neo4j GraphRAG** - Official neo4j-graphrag-python package with native graph database integration
- **LlamaIndex** - Python framework with knowledge graph modules
- **LangChain** - RAG framework with graph integrations and Neo4j/Cypher generation
- **Haystack** - End-to-end NLP framework with graph retrievers
- **LinearRAG** (PolyU) - Relation-free graph construction for efficiency
- **DIGIMON** - Unified modular framework with flexible benchmarking support

**Entity Extraction**:
- **spaCy** - Industrial-strength NLP with NER models
- **Azure AI Language** - Managed NER with custom entity training
- **AWS Comprehend** - Managed NLP with entity recognition
- **Hugging Face Transformers** - Fine-tuned NER models for domain-specific entities

### 4.6 Performance Benchmarks (2025)

Based on GraphRAG-Bench and industry evaluations:

| Metric | GraphRAG vs. Vector RAG | Source |
|--------|------------------------|--------|
| **Multi-hop Query Accuracy** | 80-85% vs. 45-50% (complex legal queries) | AWS/Lettria Study |
| **Hallucination Reduction** | Up to 90% reduction | FalkorDB |
| **Query Latency** | Sub-50ms achievable | FalkorDB |
| **RobustQA Accuracy** | Up to 86.31% | Industry Benchmarks |
| **Response Accuracy** | 3x improvement | Comparative Studies |

**Framework-Specific Benchmarks (Late 2025)**:

| Framework | Key Performance Metric |
|-----------|----------------------|
| LazyGraphRAG | 700x lower query cost vs. GraphRAG, matching quality |
| LightRAG | 10x retrieval speed improvement over GraphRAG |
| E²GraphRAG | 10x speedup over LightRAG |
| LinearRAG | Zero LLM tokens for graph construction |
| ArchRAG | 250x token savings vs. GraphRAG |
| HopRAG | 76.78% higher accuracy vs. conventional RAG |
| HippoRAG 2 | 7% improvement on associative memory tasks |

### 4.7 Best Practices (2025)

**Graph Schema Design**:
- Define core entity types aligned with the relevant domain (Customer, Account, Product, Risk, Regulation)
- Limit relationship types to meaningful, query-relevant connections
- Include temporal properties for point-in-time graph queries
- Plan for entity versioning and historical relationship tracking

**Entity Extraction Quality**:
- Fine-tune NER models on domain-specific entities
- Use confidence thresholds (e.g., > 0.8) for graph population
- Implement human-in-the-loop validation for critical entity types
- Regular evaluation on labeled datasets

**Hybrid Retrieval Tuning**:
- Tune vector similarity weight vs. graph relevance weight
- Experiment with retrieval depth (number of hops, number of documents)
- Use reciprocal rank fusion (RRF) for combining ranked lists
- Consider query-dependent weighting based on query type

**Response Quality**:
- Always include source attribution in responses
- Implement faithfulness checking (LLM response grounded in retrieved context)
- Use self-critique for high-stakes applications
- Monitor hallucination rates and retrieval relevance

**Performance Optimization**:
- Cache frequent graph traversal patterns
- Pre-compute common relationship paths
- Index graph properties used in filtering
- Partition large graphs by domain or time

### 4.8 Migration Strategy

**Phase 1: Foundation (Months 1-2)**
- Deploy graph database infrastructure (Neo4j or Neptune)
- Deploy vector database infrastructure (Pinecone or Azure AI Search)
- Define initial ontology (5-10 entity types, 10-15 relationship types)
- Implement basic document processing pipeline

**Phase 2: Graph Construction (Months 3-4)**
- Implement entity extraction with NER models
- Implement relationship extraction (LLM-based or rule-based)
- Implement entity resolution for duplicate merging
- Populate graph with pilot document corpus (1000-5000 documents)
- Populate vector store with document embeddings

**Phase 3: Retrieval Pipeline (Months 5-6)**
- Implement hybrid retriever (vector + graph)
- Implement query processor with entity linking
- Integrate LLM for response generation
- Build evaluation dataset for retrieval quality
- Deploy for internal testing with pilot users

**Phase 4: Production & Optimization (Months 7-9)**
- Production deployment with monitoring
- Tune retrieval parameters based on user feedback
- Expand ontology based on query patterns
- Implement continuous graph updates from source systems
- Scale infrastructure based on usage

**Phase 5: Advanced Features (Months 10+)**
- Community summarization (Microsoft GraphRAG approach)
- Agentic graph exploration for complex queries
- Multi-domain graph linking
- Self-critique and hallucination reduction
- Graph analytics for insights (centrality, clustering)

---

## 5. Quality Attributes and NFRs

### 5.1 Performance

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Query Latency (Simple)** | < 2 seconds (p95) | Vector search + graph 1-hop + LLM generation |
| **Query Latency (Complex)** | < 5 seconds (p95) | Multi-hop graph traversal + LLM generation |
| **Document Ingestion** | 100 docs/minute | End-to-end from upload to searchable |
| **Entity Extraction** | < 500ms per chunk | NER model inference |
| **Graph Traversal** | < 200ms (3 hops) | Graph database query performance |

### 5.2 Availability

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Query Service Uptime** | 99.9% | API availability for query endpoints |
| **Graph Database Uptime** | 99.95% | Neo4j/Neptune cluster availability |
| **Vector Database Uptime** | 99.9% | Pinecone/Weaviate availability |
| **LLM Service Uptime** | 99.5% | Azure OpenAI / AWS Bedrock availability |

### 5.3 Scalability

| Dimension | Target | Approach |
|-----------|--------|----------|
| **Knowledge Graph Size** | 10M+ nodes, 100M+ edges | Graph database partitioning, distributed cluster |
| **Document Corpus** | 1M+ documents | Distributed vector storage, incremental indexing |
| **Query Throughput** | 1000 queries/min | Horizontal scaling of retrieval layer, caching |
| **Concurrent Users** | 500+ | API gateway scaling, connection pooling |

### 5.4 Security

| Requirement | Implementation | Standard |
|-------------|----------------|----------|
| **Authentication** | OAuth 2.0, JWT tokens | Industry standard |
| **Authorization** | Node-level and relationship-level RBAC | Least privilege principle |
| **Encryption at Rest** | AES-256 for graph and vector stores | FIPS 140-2 compliant |
| **Encryption in Transit** | TLS 1.3 | Industry standard |
| **PII Protection** | Entity-level access control, PII masking | GDPR, Privacy Act compliance |
| **Audit Logging** | Complete query and response logging | SOC 2, regulatory compliance |

### 5.5 AI Quality

| Metric | Target | Enforcement |
|--------|--------|-------------|
| **Retrieval Relevance** | > 85% (relevant context in top-5) | Automated evaluation on labeled queries |
| **Response Faithfulness** | > 95% (grounded in retrieved context) | LLM-based faithfulness scoring |
| **Hallucination Rate** | < 5% | Self-critique validation, human evaluation |
| **Entity Extraction F1** | > 0.85 | Evaluation on labeled entity dataset |
| **Relationship Extraction F1** | > 0.75 | Evaluation on labeled relationship dataset |

---

## 6. Risks and Mitigations

### 6.1 Key Risks

| Risk | Impact | Likelihood | Mitigation |
|------|--------|------------|------------|
| **Low entity extraction quality** | High | Medium | Fine-tune NER for relevant domain, human validation |
| **Noisy knowledge graph** | High | Medium | Confidence thresholds, graph cleaning pipelines |
| **Query latency exceeds targets** | Medium | Medium | Caching, query optimization, graph indexing |
| **LLM hallucination on complex queries** | High | Medium | Self-critique, source attribution, human review |
| **Graph schema evolution complexity** | Medium | High | Version graph schema, migration tooling |
| **Entity resolution errors** | High | Medium | Multiple resolution signals, confidence scoring |
| **Stale knowledge graph** | Medium | Medium | Continuous update pipelines, freshness monitoring |

### 6.2 Change Management

**Organizational Change**:
- Data teams need to understand graph data modeling
- Application teams need to integrate with GraphRAG APIs
- Business users need to understand graph-powered answers

**Training Requirements**:
- Data Engineers: Graph modeling, Cypher/SPARQL, entity extraction (2 weeks)
- ML Engineers: LLM integration, retrieval evaluation, prompt engineering (1 week)
- Application Developers: GraphRAG API integration, streaming responses (1 week)
- Business Users: Understanding graph-powered answers, providing feedback (2 hours)

**Communication Plan**:
- Executive sponsorship: Demonstrate value through pilot use case
- Quarterly showcases: Show improved answer quality vs. basic RAG
- Monthly community of practice: Share learnings across teams

## 7. References and Resources

### 7.1 Related Patterns

| Pattern ID | Pattern Name | Relationship | Reference |
|-----------|-------------|--------------|-----------|
| PT-005 | RAG | GraphRAG extends basic RAG with graph capabilities | [PT-005-Retrieval-Augmented-Generation-v1.0.0.md](../PT-005/index.md) |
| PT-007 | Agentic AI | Agent can use GraphRAG for knowledge retrieval | [PT-007-Agentic-AI-v1.0.0.md](../PT-007/index.md) |
| PT-011 | IDP | IDP feeds documents to GraphRAG pipeline | [PT-011-Intelligent-Document-Processing-v1.0.0.md](../PT-011/index.md) |
| PT-013 | Conversational AI | Conversational interface powered by GraphRAG | [PT-013-Conversational-AI-v1.0.0.md](../PT-013/index.md) |
| PT-001 | Enterprise AI Governance | Governance for GraphRAG responses | [PT-001-Enterprise-AI-Governance-v1.0.0.md](../PT-001/index.md) |

### 7.2 Related ABBs

| ABB ID | ABB Name | Document Link |
|--------|----------|---------------|
| [AB-051](../../architecture-building-blocks/abbs/AB-051/AB-051-Vector-Database-v1.0.0.md) | Vector Database | [AB-051-Vector-Database-v1.0.0.md](../../architecture-building-blocks/abbs/AB-051/AB-051-Vector-Database-v1.0.0.md) |
| [AB-050](../../architecture-building-blocks/abbs/AB-050/AB-050-Large-Language-Model-Service-v1.0.0.md) | Large Language Model Service | [AB-050-Large-Language-Model-Service-v1.0.0.md](../../architecture-building-blocks/abbs/AB-050/AB-050-Large-Language-Model-Service-v1.0.0.md) |
| [AB-080](../../architecture-building-blocks/abbs/AB-080/AB-080-Knowledge-Base-v1.0.0.md) | Knowledge Base | [AB-080-Knowledge-Base-v1.0.0.md](../../architecture-building-blocks/abbs/AB-080/AB-080-Knowledge-Base-v1.0.0.md) |
| [AB-052](../../architecture-building-blocks/abbs/AB-052/AB-052-Semantic-Search-Engine-v1.0.0.md) | Semantic Search Engine | [AB-052-Semantic-Search-Engine-v1.0.0.md](../../architecture-building-blocks/abbs/AB-052/AB-052-Semantic-Search-Engine-v1.0.0.md) |
| [AB-057](../../architecture-building-blocks/abbs/AB-057/AB-057-Document-Processing-Pipeline-v1.0.0.md) | Document Processing Pipeline | [AB-057-Document-Processing-Pipeline-v1.0.0.md](../../architecture-building-blocks/abbs/AB-057/AB-057-Document-Processing-Pipeline-v1.0.0.md) |
| [AB-034](../../architecture-building-blocks/abbs/AB-034/AB-034-Entity-Extractor-v1.0.0.md) | Entity Extractor | [AB-034-Entity-Extractor-v1.0.0.md](../../architecture-building-blocks/abbs/AB-034/AB-034-Entity-Extractor-v1.0.0.md) |
| [AB-059](../../architecture-building-blocks/abbs/AB-059/AB-059-Query-Rewriting-Engine-v1.0.0.md) | Query Rewriting Engine | [AB-059-Query-Rewriting-Engine-v1.0.0.md](../../architecture-building-blocks/abbs/AB-059/AB-059-Query-Rewriting-Engine-v1.0.0.md) |
| [AB-055](../../architecture-building-blocks/abbs/AB-055/AB-055-Reranking-Engine-v1.0.0.md) | Reranking Engine | [AB-055-Reranking-Engine-v1.0.0.md](../../architecture-building-blocks/abbs/AB-055/AB-055-Reranking-Engine-v1.0.0.md) |
| [AB-058](../../architecture-building-blocks/abbs/AB-058/AB-058-Citation-Generator-v1.0.0.md) | Citation Generator | [AB-058-Citation-Generator-v1.0.0.md](../../architecture-building-blocks/abbs/AB-058/AB-058-Citation-Generator-v1.0.0.md) |
| [AB-056](../../architecture-building-blocks/abbs/AB-056/AB-056-Self-Critique-Engine-v1.0.0.md) | Self-Critique Engine | [AB-056-Self-Critique-Engine-v1.0.0.md](../../architecture-building-blocks/abbs/AB-056/AB-056-Self-Critique-Engine-v1.0.0.md) |
| [AB-054](../../architecture-building-blocks/abbs/AB-054/AB-054-Hybrid-Search-Engine-v1.0.0.md) | Hybrid Search Engine | [AB-054-Hybrid-Search-Engine-v1.0.0.md](../../architecture-building-blocks/abbs/AB-054/AB-054-Hybrid-Search-Engine-v1.0.0.md) |
| [AB-060](../../architecture-building-blocks/abbs/AB-060/AB-060-AI-Model-Registry-v1.0.0.md) | AI Governance Platform | [AB-060-AI-Model-Registry-v1.0.0.md](../../architecture-building-blocks/abbs/AB-060/AB-060-AI-Model-Registry-v1.0.0.md) |
| [AB-112](../../architecture-building-blocks/abbs/AB-112/AB-112-Data-Encryption-Service-v1.0.0.md) | Security & Identity | [AB-112-Data-Encryption-Service-v1.0.0.md](../../architecture-building-blocks/abbs/AB-112/AB-112-Data-Encryption-Service-v1.0.0.md) |
| [AB-096](../../architecture-building-blocks/abbs/AB-096/AB-096-Observability-Platform-v1.0.0.md) | Observability Platform | [AB-096-Observability-Platform-v1.0.0.md](../../architecture-building-blocks/abbs/AB-096/AB-096-Observability-Platform-v1.0.0.md) |
| [AB-105](../../architecture-building-blocks/abbs/AB-105/AB-105-GenAI-Quality-Monitor-v1.0.0.md) | GenAI Quality Monitor | [AB-105-GenAI-Quality-Monitor-v1.0.0.md](../../architecture-building-blocks/abbs/AB-105/AB-105-GenAI-Quality-Monitor-v1.0.0.md) |

### 7.3 Standards and Guidelines

**Internal Standards**:
- AI Governance Standard (TBD)
- Data Classification Policy (TBD)
- API Design Standard (TBD)
- Visual Design Standard: [05-governance/standards/visual-design/visual-design-standard.md](../../../../05-governance/standards/visual-design/visual-design-standard.md)

**Industry Standards**:
- W3C RDF 1.1: Resource Description Framework
- W3C SPARQL 1.1: Graph query language
- OpenCypher: Property graph query language
- ISO 27001: Information security management
- NIST AI RMF: AI Risk Management Framework

**Regulatory Compliance**:
- GDPR: General Data Protection Regulation (data in knowledge graphs)
- Relevant privacy legislation: Personal information in entity graphs
- Relevant requirements for AI explainability

### 7.4 External References

**Research & Frameworks (2024-2025)**:
- Microsoft GraphRAG: "From Local to Global: A Graph RAG Approach to Query-Focused Summarization" (2024, updated Feb 2025) - https://arxiv.org/abs/2404.16130
- Microsoft GraphRAG GitHub: https://github.com/microsoft/graphrag
- LazyGraphRAG: "Setting a New Standard for Quality and Cost" (Microsoft Research, Nov 2024) - https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/
- LightRAG: "Simple and Fast Retrieval-Augmented Generation" (EMNLP 2025) - https://arxiv.org/abs/2410.05779
- LightRAG GitHub: https://github.com/HKUDS/LightRAG
- HippoRAG 2: "From RAG to Memory: Non-Parametric Continual Learning for LLMs" (ICML 2025) - https://arxiv.org/abs/2502.14802
- HippoRAG GitHub: https://github.com/OSU-NLP-Group/HippoRAG
- LinearRAG: "Linear Graph Retrieval Augmented Generation on Large-scale Corpora" (Oct 2025) - https://arxiv.org/abs/2510.10114
- LinearRAG GitHub: https://github.com/DEEP-PolyU/LinearRAG
- E²GraphRAG: "Streamlining Graph-based RAG for High Efficiency and Effectiveness" (2025) - https://arxiv.org/abs/2505.24226
- ArchRAG: "Attributed Community-based Hierarchical RAG" (2025) - https://arxiv.org/abs/2502.09891
- HopRAG: "Multi-Hop Reasoning for Logic-Aware RAG" (ACL Findings 2025) - https://arxiv.org/abs/2502.12442
- StepChain GraphRAG: "Reasoning Over Knowledge Graphs for Multi-Hop QA" (2025) - https://arxiv.org/abs/2510.02827
- Inference-Scaled GraphRAG: "Improving Multi Hop QA on Knowledge Graphs" (2025) - https://arxiv.org/abs/2506.19967
- "RAG vs. GraphRAG: A Systematic Evaluation and Key Insights" (2025) - https://arxiv.org/abs/2502.11371
- Comprehensive GraphRAG Survey (Jan 2025) - https://arxiv.org/abs/2501.00309

**Benchmarks & Datasets**:
- GraphRAG-Bench: "Challenging Domain-Specific Reasoning for Evaluating GraphRAG" (Jun 2025) - https://arxiv.org/abs/2506.02404
- GraphRAG-Bench GitHub: https://github.com/GraphRAG-Bench/GraphRAG-Benchmark
- GraphRAG-Bench Dataset (Hugging Face): https://huggingface.co/datasets/GraphRAG-Bench/GraphRAG-Bench
- Awesome-GraphRAG (curated resources): https://github.com/DEEP-PolyU/Awesome-GraphRAG

**Technology Documentation**:
- Neo4j GenAI: https://neo4j.com/generativeai/
- Neo4j GraphRAG Python: https://github.com/neo4j/neo4j-graphrag-python
- Neo4j Developer Guide: https://neo4j.com/developer/genai-ecosystem/
- Amazon Neptune Analytics: https://docs.aws.amazon.com/neptune-analytics/
- Azure AI Search: https://learn.microsoft.com/en-us/azure/search/
- Weaviate: https://weaviate.io/developers/weaviate
- FalkorDB: https://www.falkordb.com/
- LlamaIndex Knowledge Graphs: https://docs.llamaindex.ai/en/stable/module_guides/indexing/knowledge_graph/
- LangChain Graph RAG: https://python.langchain.com/docs/use_cases/graph/
- GraphRAG.com (community resource): https://graphrag.com/

**Industry Analysis**:
- Gartner: "Emerging Tech: Graph RAG Will Transform Enterprise AI" (2025)
- Forrester: "Knowledge Graphs Meet Generative AI" (2025)
- IDC: "Graph-Enhanced RAG Market Forecast" (2025)
- Neo4j: "What Is GraphRAG?" - https://neo4j.com/blog/genai/what-is-graphrag/
- GraphRAG Enterprise Guide: https://towardsdatascience.com/do-you-really-need-graphrag-a-practitioners-guide-beyond-the-hype/

**Books**:
- "Knowledge Graphs: Fundamentals, Techniques, and Applications" by Mayank Kejriwal (MIT Press, 2021)
- "Building Knowledge Graphs" by Jesus Barrasa (O'Reilly, 2024)
- "Designing Machine Learning Systems" by Chip Huyen (O'Reilly, 2022)

## Appendix A: Glossary

| Term | Definition |
|------|------------|
| **GraphRAG** | Graph-enhanced Retrieval Augmented Generation: combining knowledge graphs with LLM-based RAG for improved reasoning |
| **Knowledge Graph** | A structured representation of entities and their relationships, enabling graph-based reasoning |
| **Entity Extraction** | The process of identifying and classifying named entities (people, organizations, products) in text |
| **Relationship Extraction** | The process of identifying semantic relationships between entities in text |
| **Entity Resolution** | The process of identifying and merging duplicate entity references across sources |
| **Hybrid Retrieval** | Combining multiple retrieval methods (vector similarity, graph traversal, keyword search) |
| **Multi-Hop Reasoning** | Answering questions that require traversing multiple relationship steps in a knowledge graph |
| **Community Detection** | Graph algorithm that identifies clusters of densely connected nodes |
| **Vector Embedding** | Dense numerical representation of text enabling semantic similarity comparison |
| **Semantic Search** | Search based on meaning rather than exact keyword matching |
| **Hallucination** | LLM generating content not supported by retrieved context or factual knowledge |
| **Faithfulness** | Degree to which LLM response is grounded in and consistent with retrieved context |
| **Cypher** | Graph query language for property graphs (Neo4j) |
| **SPARQL** | Graph query language for RDF knowledge graphs (W3C standard) |
| **Property Graph** | Graph model where nodes and edges can have properties (key-value pairs) |
| **LazyGraphRAG** | Microsoft's cost-optimized GraphRAG variant with zero upfront indexing cost |
| **LightRAG** | Fast dual-level retrieval GraphRAG framework from HKUST with entity/relationship-based retrieval |
| **HippoRAG** | Neurobiologically-inspired long-term memory framework using Personalized PageRank |
| **LinearRAG** | Relation-free graph construction approach with zero LLM token consumption |
| **GraphRAG-Bench** | Standardized benchmark for evaluating GraphRAG models across construction, retrieval, and generation |
| **Dual-Level Retrieval** | Retrieval paradigm that queries at both detailed (entity) and abstract (concept) levels |
| **Community Summarization** | Pre-computing summaries for clusters of related entities to enable global queries |

## Appendix B: Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-12-07 | Enterprise Architecture | Initial version - comprehensive GraphRAG pattern based on 2025 best practices. |
| 1.1.0 | 2025-12-26 | Enterprise Architecture | Updated with late 2025 research: Added LazyGraphRAG, LightRAG, HippoRAG 2, LinearRAG, E²GraphRAG, ArchRAG, HopRAG, StepChain variants; Added performance benchmarks section; Updated adoption rates and industry examples; Added GraphRAG-Bench benchmarking standard; Expanded external references with 15+ new sources. |

## Appendix C: Review and Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **Pattern Author** | Enterprise Architecture | | 2025-12-07 |
| **Enterprise Architect** | TBD | | |
| **Security Architect** | TBD | | |
| **TAF** | TBD | | |

## Appendix D: Implementation Checklist

Use this checklist when implementing GraphRAG pattern:

**Phase 1: Foundation**
- [ ] Select graph database (Neo4j or Amazon Neptune)
- [ ] Select vector database (Pinecone, Weaviate, or Azure AI Search)
- [ ] Define initial ontology (entity types and relationship types)
- [ ] Implement document processing pipeline
- [ ] Deploy embedding model for vector generation
- [ ] Define security and access control model

**Phase 2: Graph Construction**
- [ ] Implement entity extraction pipeline (NER model)
- [ ] Implement relationship extraction (LLM-based or rule-based)
- [ ] Implement entity resolution for duplicate merging
- [ ] Populate graph with pilot document corpus
- [ ] Populate vector store with document embeddings
- [ ] Validate graph quality (entity accuracy, relationship precision)

**Phase 3: Retrieval Pipeline**
- [ ] Implement query processor with entity linking
- [ ] Implement hybrid retriever (vector + graph)
- [ ] Implement context assembly for LLM
- [ ] Integrate LLM for response generation
- [ ] Implement citation generation
- [ ] Build evaluation dataset for retrieval quality
- [ ] Deploy for internal testing with pilot users

**Phase 4: Production & Optimization**
- [ ] Production deployment with monitoring (AB-096)
- [ ] Implement GenAI quality monitoring (AB-105)
- [ ] Tune retrieval parameters based on user feedback
- [ ] Implement response caching for frequent queries
- [ ] Expand ontology based on query patterns
- [ ] Implement continuous graph updates from source systems
- [ ] Scale infrastructure based on usage

**Phase 5: Advanced Features**
- [ ] Community summarization (Microsoft GraphRAG approach)
- [ ] Query decomposition for complex multi-hop questions
- [ ] Agentic graph exploration for investigative queries
- [ ] Self-critique for hallucination reduction
- [ ] Multi-domain graph linking
- [ ] Graph analytics dashboards (centrality, clustering)
- [ ] A/B testing for retrieval strategies

**Ongoing Governance**
- [ ] Monthly retrieval quality evaluation
- [ ] Monthly hallucination rate monitoring
- [ ] Quarterly ontology reviews and expansions
- [ ] Quarterly user satisfaction surveys
- [ ] Annual pattern maturity assessment
