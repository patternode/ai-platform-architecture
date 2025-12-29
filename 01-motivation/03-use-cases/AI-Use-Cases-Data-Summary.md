# BNZ AI Use Cases - Data Inputs and Outputs Summary

**Date:** December 4, 2025  
**Status:** Completed

## Overview

Successfully researched and documented data inputs and outputs for all 24 banking AI use cases at BNZ. This analysis provides a comprehensive view of data flows required for each AI solution, supporting architecture planning, integration design, and knowledge management capabilities.

## Use Cases Covered

### 1. Customer & Relationship Management (4 use cases)
- **FrontLine - Partnership Banking**: RM solutions for retail banking
- **FrontLine - CIB**: RM solutions for corporate/institutional banking  
- **HyperPersonalization**: Marketing, sales, service personalization
- **Front-end App Personalisation**: Mobile app personalization with GenAI

### 2. Risk Management (5 use cases)
- **Credit Risk**: Credit decisioning and portfolio management
- **Risk Functions**: Operational, market, liquidity, model, compliance, tech risk
- **Fincrime**: AML/CTF name screening, OCDD, ECDD, TM narratives
- **Fraud Ops**: Fraud investigation and case management
- **Wholesale Underwriting Transformation**: CIB risk underwriting process

### 3. Operations & Process Automation (8 use cases)
- **Lending Ops**: Document processing for loans and compliance
- **Onboarding**: ID verification, KYC, risk assessment
- **Payment Disputes**: Card payment dispute lifecycle automation
- **Collection Management**: Collections optimization and recovery
- **Procurement**: End-to-end procurement process optimization
- **IT Ops**: Ticketing, incident/service/problem management
- **Controls Testing**: IT and business controls testing
- **Contact Centre**: Customer service and support optimization

### 4. Data & Analytics (4 use cases)
- **Finance**: Financial reporting and analysis
- **Analytics and Reporting**: Predictive analytics and optimization
- **Data Products**: Data product creation acceleration
- **QA/QC**: Data validation and quality assurance

### 5. Platform & Development (3 use cases)
- **SDLC**: Software development lifecycle automation
- **Security AI**: Threat detection and security operations
- **Learning Content Production**: Training content generation

## Key Data Input Categories

### Structured Data Sources
- Customer profiles and demographics
- Transaction records and history
- Financial statements and metrics
- Product holdings and usage
- System logs and operational data
- Regulatory and reference data

### Unstructured Content
- Documents (PDFs, scans, contracts)
- Communications (emails, chat, calls)
- Knowledge base articles
- Policy and procedure documentation
- External sources (news, adverse media)

### Real-time Streams
- Transaction events
- Monitoring alerts
- User behavior patterns
- Network and security telemetry
- Market data feeds

### External Data
- Credit bureau reports
- Sanctions and PEP lists
- Industry benchmarks
- Regulatory requirements
- Threat intelligence feeds
- Market intelligence

## Key Data Output Categories

### Decisions & Recommendations
- Risk scores and ratings
- Approval/rejection decisions
- Next best actions
- Prioritization and routing
- Optimization recommendations

### Processed Documents
- Extracted data fields
- Automated summaries
- Formatted reports
- Documentation and narratives
- Audit trails

### Alerts & Notifications
- Risk alerts and warnings
- Anomaly detection
- Compliance violations
- Security threats
- Quality issues

### Analytics & Insights
- Predictions and forecasts
- Pattern analysis
- Trend identification
- Performance metrics
- What-if scenarios

### API Outputs
- Enriched data
- Metadata and tags
- Workflow triggers
- Integration payloads
- Real-time responses

## Architecture Implications

### Knowledge Capabilities Required
Based on the [knowledge capabilities framework](../../../02-capabilities/knowledge/knowledge-capabilities.md):

- **KN.1 Ingestion**: Multi-modal data ingestion (structured, unstructured, streaming)
- **KN.2 Organization**: Entity resolution, classification, semantic enrichment
- **KN.3 Storage & Retrieval**: Vector databases, knowledge graphs, search
- **KN.4 Access & Delivery**: APIs, real-time delivery, caching
- **KN.5 Governance**: Data quality, lineage, privacy, compliance

### Integration Patterns
- Core banking system integration
- Document processing pipelines
- Real-time event streaming
- API-based data exchange
- Batch data synchronization

### Data Quality Requirements
- Validation and verification
- Deduplication and resolution
- Completeness checks
- Timeliness monitoring
- Accuracy assessment

## Next Steps

1. **Map to Architecture Building Blocks**: Align data flows with ABBs in application, data, integration, and security layers
2. **Identify Integration Points**: Document specific systems and APIs for each data input/output
3. **Define Data Contracts**: Establish schemas and SLAs for data exchange
4. **Assess Data Governance**: Review privacy, security, and compliance requirements per use case
5. **Prioritize Implementation**: Sequence use cases based on data readiness and dependencies

## References

- [BNZ List of AI Use Cases Dec 25.csv](./BNZ%20List%20of%20AI%20use%20cases%20Dec%2025.csv)
- [Knowledge Capabilities](../../../02-capabilities/knowledge/knowledge-capabilities.md)
- [Architecture Building Blocks](../../../03-building-blocks/architecture-building-blocks/)
- [Integration Patterns](../../../03-building-blocks/patterns/integration/)

