# AWS AgentCore Architecture with Vector and Graph Databases

This directory contains comprehensive documentation and cost modeling for AWS AgentCore architecture enhanced with vector and graph database capabilities for AI knowledge systems.

## 📁 Files Overview

### 🎨 Architecture Diagrams
- **`AWS-AgentCore-Architecture.drawio`** - Comprehensive draw.io architecture diagram showing:
  - 3 environments (Sandbox, Development, Production)
  - 7 AgentCore core services (Runtime, Gateway, Memory, Identity, Browser, Code Interpreter, Observability)
  - 4 Bedrock foundation models (Claude 3.5 Sonnet/Haiku, Llama 3.1 70B/8B)
  - Vector database layer (S3 Vectors, OpenSearch, Pinecone)
  - Graph database layer (Neptune, Neo4j)
  - Supporting AWS services and networking
  - Data flow connections and cost optimization zones

### 📊 Cost Modeling
- **`AWS-AgentCore-Cost-Model-Enhanced.xlsx`** - Enhanced Excel cost model with:
  - Vector database services integration (S3 Vectors, OpenSearch, Pinecone)
  - Graph database services integration (Neptune, Neo4j, GraphRAG)
  - 7 worksheets covering complete cost analysis
  - Usage scenarios including database-heavy workloads
  - Cost optimization guidance for AI knowledge systems

### 🔧 Generation Scripts
- **`create_enhanced_cost_model.py`** - Python script to generate the Excel cost model
- **`create_cost_model.py`** - Original cost model script (legacy)

## 🏗️ Architecture Components

### Core AgentCore Services
| Service | Purpose | Billing Model |
|---------|---------|---------------|
| **Runtime** | Firecracker serverless execution | Consumption-based (vCPU-second + GB-second) |
| **Gateway** | MCP protocol compatibility | Per operation + search queries |
| **Memory** | Session + long-term memory | Storage + query-based |
| **Identity** | IAM + zero-trust security | Integrated with AWS IAM |
| **Browser** | Web automation | Same as Runtime |
| **Code Interpreter** | Sandboxed code execution | Same as Runtime |
| **Observability** | OpenTelemetry monitoring | Data ingestion + storage + queries |

### Vector Database Layer
| Technology | Use Case | Pricing Model | Best For |
|------------|----------|---------------|----------|
| **S3 Vectors** | Cost-effective vector storage | $0.012/GB-month + $0.01/1K queries | Large-scale, cost-sensitive deployments |
| **OpenSearch Serverless** | Hybrid text + vector search | $0.24/OCU-hour + $0.024/GB-month | Multi-modal search requirements |
| **Pinecone** | Pure vector search | $70/month starter + $0.096/pod-hour | High-performance vector workloads |

### Graph Database Layer
| Technology | Use Case | Pricing Model | Best For |
|------------|----------|---------------|----------|
| **Neptune Serverless** | GraphRAG, knowledge graphs | $0.18/NCU-hour + $0.10/GB-month | Serverless graph workloads |
| **Neptune ML** | Graph embeddings | $1.44/hour training + $0.48/hour inference | Graph machine learning |
| **Neo4j on EC2** | Custom graph requirements | EC2 instance costs + license | Self-managed graph databases |
| **Neo4j AuraDB** | Managed graph database | $0.50/hour professional | Fully managed graph service |

### Foundation Models (Bedrock)
| Model | Input Pricing | Output Pricing | Use Case |
|-------|---------------|----------------|----------|
| **Claude 3.5 Sonnet** | $3.00/1K tokens | $15.00/1K tokens | Primary reasoning and generation |
| **Claude 3.5 Haiku** | $0.25/1K tokens | $1.25/1K tokens | Fast, lightweight tasks |
| **Llama 3.1 70B** | $0.99/1K tokens | $0.99/1K tokens | Open source alternative |
| **Llama 3.1 8B** | $0.22/1K tokens | $0.22/1K tokens | Cost-effective option |

## 💰 Cost Analysis Summary

### Monthly Cost Breakdown (Baseline Scenario)
- **AgentCore Services**: Runtime, Gateway, Memory, Identity components
- **Foundation Models**: Bedrock model inference costs
- **Vector Database Services**: S3 Vectors, OpenSearch, Pinecone costs
- **Graph Database Services**: Neptune, Neo4j, GraphRAG costs
- **Supporting AWS Services**: EC2, Lambda, S3, DynamoDB
- **Infrastructure**: VPC, monitoring, security

### Usage Scenarios
1. **Baseline**: Standard sandbox usage (10 users, 3 sessions/day)
2. **Light Usage**: Minimal experimentation (5 users, 2 sessions/day)
3. **Heavy Usage**: Active development (15 users, 5 sessions/day)
4. **Training Event**: Intensive workshop (25 users, 8 sessions/day)
5. **Vector Search Heavy**: High vector workload (3x vector usage)
6. **Graph Analytics**: Graph ML training focus (3x graph usage)
7. **RAG + GraphRAG**: Combined approach (2.5x vector, 2x graph)
8. **Production Pilot**: Pre-production testing

## 🎯 Key Integration Patterns

### Vector Database Integration
- **Semantic Search**: Vector embeddings for document and code search
- **RAG (Retrieval Augmented Generation)**: Context-aware responses
- **Multi-modal Search**: Text + vector hybrid search capabilities
- **Cost Optimization**: S3 Vectors for cold storage, OpenSearch for hot queries

### Graph Database Integration
- **GraphRAG**: Knowledge graph enhanced retrieval
- **Entity Relationships**: Domain knowledge modeling
- **Graph ML**: Advanced graph analytics and predictions
- **Knowledge Graphs**: Structured domain expertise

### AgentCore Integration Frameworks
- **LangChain**: Vector store and graph database connectors
- **LangGraph**: Graph-based agent workflows
- **LlamaIndex**: Vector and graph RAG integration
- **Strands AI**: Knowledge graph integration
- **AutoGen/CrewAI**: Multi-agent coordination

## 📋 Usage Instructions

### Architecture Diagram
1. Open `AWS-AgentCore-Architecture.drawio` in draw.io or VS Code with draw.io extension
2. Use for architecture discussions, documentation, and planning
3. Customize environments and components as needed

### Cost Model
1. Open `AWS-AgentCore-Cost-Model-Enhanced.xlsx` in Excel
2. Review and update assumptions in the Assumptions worksheet
3. Modify scenarios in the Scenarios worksheet
4. Use Summary worksheet for executive reporting
5. Regenerate using Python script if major changes needed

### Script Execution
```bash
# Install dependencies
pip install pandas openpyxl

# Generate new cost model
python create_enhanced_cost_model.py
```

## 🔄 Maintenance

### Monthly Tasks
- Review actual costs vs. estimates
- Update usage assumptions based on real data
- Monitor vector and graph database utilization

### Quarterly Tasks
- Update AWS pricing data
- Adjust growth projections
- Review database technology choices

### Annual Tasks
- Comprehensive architecture review
- Budget planning and forecasting
- Technology stack optimization

## 📚 References

### AWS Documentation
- [AWS AgentCore](https://aws.amazon.com/agentcore/) - Core platform documentation
- [Amazon Neptune](https://aws.amazon.com/neptune/) - Graph database service
- [Amazon OpenSearch](https://aws.amazon.com/opensearch-service/) - Search and analytics
- [Amazon Bedrock](https://aws.amazon.com/bedrock/) - Foundation models

### Vector Database Documentation
- [S3 Vectors](https://aws.amazon.com/s3/features/vectors/) - AWS vector storage
- [Pinecone](https://www.pinecone.io/) - Vector database platform

### Graph Database Documentation
- [Neo4j](https://neo4j.com/) - Graph database platform
- [GraphRAG](https://microsoft.github.io/graphrag/) - Graph-based RAG

### Integration Frameworks
- [LangChain](https://langchain.com/) - LLM application framework
- [LlamaIndex](https://llamaindex.ai/) - Data framework for LLMs

## 🏷️ Tags
`aws` `agentcore` `vector-database` `graph-database` `cost-model` `architecture` `ai` `rag` `graphrag` `knowledge-graph` `bedrock` `neptune` `opensearch` `pinecone` `neo4j`

---
*Generated: December 2024*  
*Team: BNZ Strategy & Architecture*  
*Contact: Architecture Team*