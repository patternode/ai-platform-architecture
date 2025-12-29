import pandas as pd
from datetime import datetime

# Create the updated Excel writer object
excel_path = r'd:\Work\BNZ\work-bnz\02-architecture\03-agentic-ai\06-community\AWS-AgentCore-Cost-Model-Enhanced.xlsx'

with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    
    # 1. SUMMARY WORKSHEET (Updated with new categories)
    summary_data = {
        'Cost Category': [
            'AgentCore Services',
            'Foundation Models (Bedrock)',
            'Supporting AWS Services',
            'Data Transfer & Storage',
            'Monitoring & Logging',
            'Network Infrastructure',
            'Security & Compliance',
            'Vector Database Services',
            'Graph Database Services',
            'TOTAL MONTHLY COST'
        ],
        'Monthly Cost (USD)': [
            '=Calculations!B2',
            '=Calculations!B3', 
            '=Calculations!B4',
            '=Calculations!B5',
            '=Calculations!B6',
            '=Calculations!B7',
            '=Calculations!B8',
            '=Calculations!B9',
            '=Calculations!B10',
            '=SUM(B1:B9)'
        ],
        'Percentage': [
            '=B1/$B$10*100',
            '=B2/$B$10*100',
            '=B3/$B$10*100',
            '=B4/$B$10*100',
            '=B5/$B$10*100',
            '=B6/$B$10*100',
            '=B7/$B$10*100',
            '=B8/$B$10*100',
            '=B9/$B$10*100',
            '100%'
        ],
        'Notes': [
            'Runtime, Browser, Code Interpreter, Gateway, Observability',
            'Claude 3.5, Haiku, Llama models',
            'EC2, Lambda, S3, DynamoDB',
            'Inter-AZ, Internet egress, S3 storage',
            'CloudWatch metrics, logs, dashboards',
            'VPC, NAT Gateway, Load Balancer',
            'KMS, IAM, SSL certificates',
            'S3 Vectors, OpenSearch, Pinecone vector search',
            'Neptune, Neo4j knowledge graphs, GraphRAG',
            'Total estimated monthly cost'
        ]
    }
    summary_df = pd.DataFrame(summary_data)
    summary_df.to_excel(writer, sheet_name='Summary', index=False)
    
    # 2. ASSUMPTIONS WORKSHEET (Enhanced with vector/graph database assumptions)
    assumptions_data = {
        'Category': [
            'PROJECT ASSUMPTIONS', '', '', '',
            'Team Size', 'Active Hours per Day', 'Working Days per Month', 'Sessions per User per Day',
            'Average Session Duration', 'Peak Concurrent Users', 'Data Storage Growth', '',
            'MODEL USAGE DISTRIBUTION', '', '', '',
            'Claude 3.5 Sonnet', 'Claude 3.5 Haiku', 'Llama 3.1 70B', 'Llama 3.1 8B',
            'Average Input Tokens per Session', 'Average Output Tokens per Session', '',
            'VECTOR DATABASE ASSUMPTIONS', '', '', '',
            'Vector Dimensions', 'Vectors per User', 'Vector Storage Growth', 'Vector Queries per Session',
            'Vector Search Precision', 'Embedding Model', '',
            'GRAPH DATABASE ASSUMPTIONS', '', '', '',
            'Entities per User', 'Relationships per Entity', 'Graph Queries per Session', 'Knowledge Graph Depth',
            'GraphRAG Integration', 'Graph ML Training Frequency', '',
            'TECHNICAL SPECIFICATIONS', '', '', '',
            'CPU Usage per Session', 'Memory Usage per Session', 'Storage per User', 'Log Retention Period',
            'AWS Region', 'Availability Zones', 'VPC CIDR', 'Environment Type'
        ],
        'Value': [
            '', '', '', '',
            10, 8, 22, 3,
            120, 5, 10, '',
            '', '', '', '',
            40, 30, 20, 10,
            500, 300, '',
            '', '', '', '',
            1536, 1000, 20, 2,
            '95%', 'text-embedding-ada-002', '',
            '', '', '', '',
            50, 3, 1, 4,
            'Enabled', 'Weekly', '',
            '', '', '', '',
            0.5, 1, 5, 30,
            'us-east-1', 2, '10.0.0.0/16', 'Sandbox'
        ],
        'Unit': [
            '', '', '', '',
            'People', 'Hours', 'Days', 'Sessions',
            'Seconds', 'Users', 'GB/Month', '',
            '', '', '', '',
            '%', '%', '%', '%',
            'Tokens', 'Tokens', '',
            '', '', '', '',
            'Dimensions', 'Vectors', 'Percent Growth/Month', 'Queries',
            'Accuracy', 'Model', '',
            '', '', '', '',
            'Entities', 'Relationships', 'Queries', 'Levels',
            'Boolean', 'Frequency', '',
            '', '', '', '',
            'vCPU', 'GB', 'GB', 'Days',
            'Region', 'Count', 'CIDR', 'Type'
        ],
        'Description': [
            '', '', '', '',
            'Number of sandbox users in community', 'Daily active usage hours', 'Business days per month', 'AgentCore sessions per user daily',
            'Typical session length', 'Maximum simultaneous users', 'Monthly data accumulation', '',
            '', '', '', '',
            'Percentage of model usage', 'Percentage of model usage', 'Percentage of model usage', 'Percentage of model usage',
            'Typical prompt size', 'Typical response size', '',
            '', '', '', '',
            'Vector embedding dimensions', 'Number of vectors per user', 'Monthly vector storage growth', 'Vector searches per session',
            'Target search accuracy', 'Embedding model for vectors', '',
            '', '', '', '',
            'Knowledge graph entities per user', 'Average relationships per entity', 'Graph queries per session', 'Knowledge graph traversal depth',
            'GraphRAG integration enabled', 'Graph ML model training frequency', '',
            '', '', '', '',
            'Processing requirement', 'RAM requirement', 'Individual storage allocation', 'CloudWatch log retention',
            'Primary deployment region', 'Multi-AZ deployment', 'Network address space', 'Development/learning environment'
        ]
    }
    assumptions_df = pd.DataFrame(assumptions_data)
    assumptions_df.to_excel(writer, sheet_name='Assumptions', index=False)
    
    # 3. AWS PRICING WORKSHEET (Enhanced with vector and graph database pricing)
    pricing_data = {
        'Category': [
            # AgentCore Services (12 items)
            'AgentCore Runtime', 'AgentCore Runtime', 'AgentCore Browser', 'AgentCore Browser',
            'AgentCore Code Interpreter', 'AgentCore Code Interpreter', 'AgentCore Gateway', 'AgentCore Gateway',
            'AgentCore Gateway', 'AgentCore Observability', 'AgentCore Observability', 'AgentCore Observability',
            # Bedrock Models (10 items) 
            'Bedrock Claude 3.5 Sonnet', 'Bedrock Claude 3.5 Sonnet', 'Bedrock Claude 3.5 Haiku', 'Bedrock Claude 3.5 Haiku',
            'Bedrock Claude 3 Opus', 'Bedrock Claude 3 Opus', 'Bedrock Llama 3.1 70B', 'Bedrock Llama 3.1 70B',
            'Bedrock Llama 3.1 8B', 'Bedrock Llama 3.1 8B',
            # Compute Services (8 items)
            'EC2 t3.micro', 'EC2 t3.small', 'EC2 t3.medium', 'EC2 t3.large', 'EC2 t4g.micro', 'EC2 t4g.small',
            'Lambda Requests', 'Lambda Duration x86',
            # Storage & Database (8 items)
            'S3 Standard Storage', 'S3 Standard-IA Storage', 'S3 GET Requests', 'S3 PUT Requests', 
            'DynamoDB On-Demand RRU', 'DynamoDB On-Demand WRU', 'DynamoDB Storage', 'CloudWatch Custom Metrics',
            # Monitoring & Network (6 items)
            'CloudWatch Log Ingestion', 'CloudWatch Log Storage', 'VPC NAT Gateway Hours', 'VPC NAT Gateway Data',
            'Data Transfer Inter-AZ', 'Data Transfer Internet 1GB-10TB',
            # Vector Database Services (6 items)
            'S3 Vectors Storage', 'S3 Vectors Query', 'OpenSearch Serverless Search OCU', 'OpenSearch Serverless Storage',
            'Pinecone Starter', 'Pinecone Standard',
            # Graph Database Services (8 items)
            'Neptune Serverless Capacity', 'Neptune Serverless Storage', 'Neptune Serverless I/O', 'Neptune ML Training',
            'Neptune ML Inference', 'Neo4j on EC2 m5.large', 'Neo4j on EC2 m5.xlarge', 'Neo4j AuraDB Professional'
        ],
        'Component': [
            # AgentCore
            'CPU Usage', 'Memory Usage', 'CPU Usage', 'Memory Usage',
            'CPU Usage', 'Memory Usage', 'MCP Operations', 'Search Queries',
            'Tool Indexing', 'Data Ingestion', 'Data Storage', 'Queries',
            # Bedrock
            'Input Tokens', 'Output Tokens', 'Input Tokens', 'Output Tokens',
            'Input Tokens', 'Output Tokens', 'Input Tokens', 'Output Tokens',
            'Input Tokens', 'Output Tokens',
            # Compute
            'Instance Hour', 'Instance Hour', 'Instance Hour', 'Instance Hour', 'Instance Hour', 'Instance Hour',
            'Requests', 'GB-seconds',
            # Storage & Database
            'Storage', 'Storage', 'Requests', 'Requests',
            'Read Request Units', 'Write Request Units', 'Storage', 'Metrics',
            # Monitoring & Network
            'Data Ingestion', 'Data Storage', 'Instance Hours', 'Data Processing',
            'Data Transfer', 'Data Transfer',
            # Vector Database
            'Vector Storage', 'Vector Queries', 'Search Compute', 'Storage',
            'Vector Database', 'Vector Database',
            # Graph Database
            'Capacity Units', 'Storage', 'I/O Operations', 'Training',
            'Inference', 'Instance Hour', 'Instance Hour', 'Managed Service'
        ],
        'Unit': [
            # AgentCore
            'per vCPU-second', 'per GB-second', 'per vCPU-second', 'per GB-second',
            'per vCPU-second', 'per GB-second', 'per operation', 'per query',
            'per tool indexed', 'per GB', 'per GB-month', 'per 1000 queries',
            # Bedrock
            'per 1K tokens', 'per 1K tokens', 'per 1K tokens', 'per 1K tokens',
            'per 1K tokens', 'per 1K tokens', 'per 1K tokens', 'per 1K tokens',
            'per 1K tokens', 'per 1K tokens',
            # Compute
            'per hour', 'per hour', 'per hour', 'per hour', 'per hour', 'per hour',
            'per 1M requests', 'per GB-second',
            # Storage & Database
            'per GB-month', 'per GB-month', 'per 1K requests', 'per 1K requests',
            'per 1M RRUs', 'per 1M WRUs', 'per GB-month', 'per metric-month',
            # Monitoring & Network
            'per GB', 'per GB-month', 'per hour', 'per GB',
            'per GB', 'per GB',
            # Vector Database
            'per GB-month', 'per 1K queries', 'per OCU-hour', 'per GB-month',
            'per month', 'per pod-hour',
            # Graph Database
            'per NCU-hour', 'per GB-month', 'per 1M I/Os', 'per hour',
            'per hour', 'per hour', 'per hour', 'per hour'
        ],
        'Current Price (USD)': [
            # AgentCore (12 prices)
            0.0000248611, 0.00000262500, 0.0000248611, 0.00000262500,
            0.0000248611, 0.00000262500, 0.001000, 0.001000,
            0.001000, 0.50, 0.03, 0.005,
            # Bedrock (10 prices)
            0.003000, 0.015000, 0.000250, 0.001250,
            0.015000, 0.075000, 0.00099, 0.00099,
            0.00022, 0.00022,
            # Compute (8 prices)
            0.0104, 0.0208, 0.0416, 0.0832, 0.0084, 0.0168,
            0.20, 0.0000166667,
            # Storage & Database (8 prices)
            0.023, 0.0125, 0.0004, 0.005,
            0.25, 1.25, 0.25, 0.30,
            # Monitoring & Network (6 prices)
            0.50, 0.03, 0.045, 0.045,
            0.01, 0.09,
            # Vector Database (6 prices)
            0.012, 0.01, 0.24, 0.024,
            70, 0.096,
            # Graph Database (8 prices)
            0.18, 0.10, 0.20, 1.44,
            0.48, 0.096, 0.192, 0.50
        ],
        'Region': ['us-east-1'] * 58,
        'Last Updated': ['2024-12-01'] * 58,
        'Notes': [
            # AgentCore notes
            'Consumption-based billing', 'Peak memory consumed', 'Same as Runtime pricing', 'Same as Runtime pricing',
            'Same as Runtime pricing', 'Same as Runtime pricing', 'ListTools CallTool operations', 'Semantic search functionality',
            'One-time indexing cost', 'CloudWatch Logs ingestion', 'CloudWatch Logs storage', 'Log analysis queries',
            # Bedrock notes
            'Text generation input', 'Text generation output', 'Lightweight model', 'Lightweight model',
            'Most capable model', 'Most capable model', 'Open source model', 'Open source model',
            'Smaller open source', 'Smaller open source',
            # Compute notes
            'Burstable performance', 'Burstable performance', 'Burstable performance', 'Burstable performance', 
            'ARM-based Graviton2', 'ARM-based Graviton2', 'First 1M free monthly', 'First 400K GB-s free',
            # Storage & Database notes
            'First 50TB pricing tier', 'Infrequent access', 'Data retrieval', 'Data upload',
            'Pay per request', 'Pay per request', 'Data storage', 'First 10K free',
            # Monitoring & Network notes
            'First 5GB free monthly', 'Compressed storage', 'Highly available NAT', 'Data processed',
            'Between AZs same region', 'Next 9.999TB',
            # Vector Database notes
            'Vector storage in S3', 'Vector search operations', 'Search compute units', 'Managed storage',
            'Up to 5M vectors 768d', 's1.x1 pod pricing',
            # Graph Database notes
            'Neptune Compute Units', 'Graph database storage', 'Database I/O operations', 'Graph ML model training',
            'Graph ML inference', 'Self-managed Neo4j', 'Self-managed Neo4j', 'Managed Neo4j service'
        ]
    }
    pricing_df = pd.DataFrame(pricing_data)
    pricing_df.to_excel(writer, sheet_name='AWS Pricing', index=False)
    
    # 4. BILL OF MATERIALS WORKSHEET (Enhanced)
    bom_data = {
        'Service Category': [
            'AgentCore Services', 'AgentCore Services', 'AgentCore Services', 'AgentCore Services',
            'Foundation Models', 'Foundation Models', 'Foundation Models', 'Foundation Models',
            'Compute Services', 'Compute Services', 'Compute Services', 'Storage Services',
            'Storage Services', 'Database Services', 'Database Services', 'Database Services',
            'Monitoring Services', 'Monitoring Services', 'Network Services', 'Network Services',
            'Security Services', 'Vector Database Services', 'Vector Database Services', 'Vector Database Services',
            'Graph Database Services', 'Graph Database Services'
        ],
        'Component': [
            'AgentCore Runtime', 'AgentCore Browser', 'AgentCore Code Interpreter', 'AgentCore Gateway',
            'Claude 3.5 Sonnet', 'Claude 3.5 Haiku', 'Llama 3.1 70B', 'Llama 3.1 8B',
            'EC2 t3.medium', 'Lambda Functions', 'Lambda ARM Functions', 'S3 Standard Storage',
            'S3 API Operations', 'DynamoDB Tables', 'DynamoDB Read Units', 'DynamoDB Write Units',
            'CloudWatch Metrics', 'CloudWatch Logs', 'VPC NAT Gateway', 'Data Transfer',
            'KMS Keys', 'S3 Vectors Storage', 'OpenSearch Serverless', 'Pinecone Vector DB',
            'Neptune Serverless', 'Neo4j on EC2'
        ],
        'Quantity': [
            '=Assumptions!B5*Assumptions!B6*Assumptions!B7*Assumptions!B8', 
            '=B1*0.3', '=B1*0.2', '=B1*100',
            '=Assumptions!B17/100', '=Assumptions!B18/100', '=Assumptions!B19/100', '=Assumptions!B20/100',
            2, '=B1', '=B1*0.5', '=Assumptions!B11*Assumptions!B5',
            '=B1*1000', 3, '=B1*10000', '=B1*1000',
            '=Assumptions!B5*5', '=B1*0.1', 1, '=B1*0.001',
            2, '=Assumptions!B26*Assumptions!B5/1000', '=C22*24*22', 0.5,
            '=C24*24*22', 1
        ],
        'Unit': [
            'Sessions/Month', 'Sessions/Month', 'Sessions/Month', 'Operations/Month',
            'Usage %', 'Usage %', 'Usage %', 'Usage %',
            'Instances', 'Invocations/Month', 'Invocations/Month', 'GB',
            'API Calls/Month', 'Tables', 'RRUs/Month', 'WRUs/Month',
            'Metrics', 'GB/Month', 'Hours/Month', 'GB/Month',
            'Keys', 'GB', 'Search OCU Hours/Month', 'Pods',
            'NCU Hours/Month', 'Instance Hours/Month'
        ],
        'Monthly Usage': [
            '=C1', '=C2', '=C3', '=C4',
            '=C5', '=C6', '=C7', '=C8',
            '=C9*24*Assumptions!B7', '=C10', '=C11', '=C12',
            '=C13', '=C14', '=C15', '=C16',
            '=C17', '=C18', '=C19*24*Assumptions!B7', '=C20',
            '=C21', '=C22', '=C23', '=C24',
            '=C25', '=C26*24*Assumptions!B7'
        ],
        'Unit Cost (USD)': [
            '=(AWS_Pricing!E1*Assumptions!B41+AWS_Pricing!E2*Assumptions!B42)*Assumptions!B9',
            '=(AWS_Pricing!E3*Assumptions!B41+AWS_Pricing!E4*Assumptions!B42)*Assumptions!B9',
            '=(AWS_Pricing!E5*Assumptions!B41+AWS_Pricing!E6*Assumptions!B42)*Assumptions!B9',
            'AWS_Pricing!E7',
            '=(AWS_Pricing!E13*Assumptions!B21+AWS_Pricing!E14*Assumptions!B22)*C1/1000',
            '=(AWS_Pricing!E15*Assumptions!B21+AWS_Pricing!E16*Assumptions!B22)*C1/1000',
            '=(AWS_Pricing!E19*Assumptions!B21+AWS_Pricing!E20*Assumptions!B22)*C1/1000',
            '=(AWS_Pricing!E21*Assumptions!B21+AWS_Pricing!E22*Assumptions!B22)*C1/1000',
            'AWS_Pricing!E25', 'AWS_Pricing!E30*1', 'AWS_Pricing!E31*1', 'AWS_Pricing!E32',
            'AWS_Pricing!E34', 'AWS_Pricing!E38', 'AWS_Pricing!E36', 'AWS_Pricing!E37',
            'AWS_Pricing!E39', 'AWS_Pricing!E40', 'AWS_Pricing!E43', 'AWS_Pricing!E46',
            50, 'AWS_Pricing!E49', 'AWS_Pricing!E51', 'AWS_Pricing!E54',
            'AWS_Pricing!E55', 'AWS_Pricing!E58'
        ],
        'Monthly Cost (USD)': [
            '=D1*E1', '=D2*E2', '=D3*E3', '=D4*E4',
            '=D5*E5', '=D6*E6', '=D7*E7', '=D8*E8',
            '=D9*E9', '=D10*E10', '=D11*E11', '=D12*E12',
            '=D13*E13', '=D14*E14', '=D15*E15/1000000', '=D16*E16/1000000',
            '=D17*E17', '=D18*E18', '=D19*E19', '=D20*E20',
            '=D21*E21', '=D22*E22', '=D23*E23', '=D24*E24',
            '=D25*E25', '=D26*E26'
        ]
    }
    bom_df = pd.DataFrame(bom_data)
    bom_df.to_excel(writer, sheet_name='Bill of Materials', index=False)
    
    # 5. CALCULATIONS WORKSHEET (Enhanced)
    calculations_data = {
        'Cost Category': [
            'AgentCore Services Total',
            'Foundation Models Total',
            'Supporting AWS Services Total',
            'Data Transfer & Storage Total',
            'Monitoring & Logging Total',
            'Network Infrastructure Total',
            'Security & Compliance Total',
            'Vector Database Services Total',
            'Graph Database Services Total',
            'TOTAL MONTHLY COST',
            '',
            'BREAKDOWN BY USAGE PATTERN',
            'Peak Hours Cost (70%)',
            'Off-Peak Hours Cost (20%)',
            'Weekend Cost (10%)',
            '',
            'COST PER USER',
            'Monthly Cost per User',
            'Daily Cost per User',
            'Cost per Session',
            '',
            'QUARTERLY PROJECTIONS',
            'Q1 Estimate',
            'Q2 Estimate (15% growth)',
            'Q3 Estimate (cumulative)',
            'Q4 Estimate (cumulative)',
            '',
            'DATABASE COST BREAKDOWN',
            'Vector Database Cost Ratio',
            'Graph Database Cost Ratio',
            'Traditional Database Cost Ratio'
        ],
        'Formula/Value': [
            '=SUM(BOM!F1:F4)',
            '=SUM(BOM!F5:F8)',
            '=SUM(BOM!F9:F13)',
            '=SUM(BOM!F12:F13,BOM!F20)',
            '=SUM(BOM!F17:F18)',
            '=SUM(BOM!F19:F20)',
            '=SUM(BOM!F21)',
            '=SUM(BOM!F22:F24)',
            '=SUM(BOM!F25:F26)',
            '=B1+B2+B3+B4+B5+B6+B7+B8+B9',
            '',
            '',
            '=B10*0.7',
            '=B10*0.2',
            '=B10*0.1',
            '',
            '',
            '=B10/Assumptions!B5',
            '=B18/Assumptions!B7',
            '=B18/(Assumptions!B5*Assumptions!B7*Assumptions!B8)',
            '',
            '',
            '=B10*3',
            '=B23*1.15',
            '=B24*1.15',
            '=B25*1.15',
            '',
            '',
            '=B8/B10*100',
            '=B9/B10*100',
            '=(B3+B4)/B10*100'
        ],
        'Result (USD)': [
            '', '', '', '', '', '', '', '', '', '',
            '', '', '', '', '',
            '', '', '', '', '',
            '', '', '', '', '', '',
            '', '', '', '', ''
        ],
        'Notes': [
            'Runtime, Browser, Code Interpreter, Gateway costs',
            'All Bedrock model inference costs',
            'EC2, Lambda, S3 costs',
            'Storage and data transfer costs',
            'CloudWatch metrics and logs',
            'VPC and NAT Gateway costs',
            'KMS keys and security',
            'S3 Vectors, OpenSearch, Pinecone costs',
            'Neptune, Neo4j, and graph ML costs',
            'Complete monthly cost estimate',
            '',
            'Cost distribution by usage pattern',
            'Business hours (9-5) usage cost',
            'After hours usage cost',
            'Weekend usage cost',
            '',
            'Per-user cost metrics',
            'Total cost divided by team size',
            'Monthly cost per working day',
            'Cost per individual session',
            '',
            'Growth projections',
            'Current quarter estimate',
            'Next quarter with growth',
            'Third quarter projection',
            'Fourth quarter projection',
            '',
            'Database technology cost analysis',
            'Vector database cost percentage',
            'Graph database cost percentage',
            'Traditional database cost percentage'
        ]
    }
    calculations_df = pd.DataFrame(calculations_data)
    calculations_df.to_excel(writer, sheet_name='Calculations', index=False)
    
    # 6. SCENARIOS WORKSHEET (Enhanced with vector/graph scenarios)
    scenarios_data = {
        'Scenario': [
            'Baseline (Current)', 'Light Usage', 'Heavy Usage', 'Training Event',
            'Vector Search Heavy', 'Graph Analytics', 'RAG + GraphRAG', 'Production Pilot'
        ],
        'Team Size': [10, 5, 15, 25, 10, 8, 12, 10],
        'Sessions/User/Day': [3, 2, 5, 8, 6, 4, 5, 3],
        'Vector Usage Multiplier': [1.0, 0.5, 1.5, 2.0, 3.0, 1.0, 2.5, 1.2],
        'Graph Usage Multiplier': [1.0, 0.3, 1.2, 1.5, 0.8, 3.0, 2.0, 1.0],
        'Monthly Cost': [
            '=Calculations!B10',
            '=Calculations!B10*0.4',
            '=Calculations!B10*1.8',
            '=Calculations!B10*4.2',
            '=Calculations!B10*2.1',
            '=Calculations!B10*1.9',
            '=Calculations!B10*2.8',
            '=Calculations!B10*1.0'
        ],
        'Cost/User/Month': [
            '=F1/B1',
            '=F2/B2',
            '=F3/B3',
            '=F4/B4',
            '=F5/B5',
            '=F6/B6',
            '=F7/B7',
            '=F8/B8'
        ],
        'Notes': [
            'Standard sandbox usage pattern',
            'Minimal experimentation',
            'Active development phase',
            'Intensive training workshop',
            'Heavy vector search workload',
            'Graph analytics and ML training',
            'Combined RAG and GraphRAG',
            'Pre-production testing'
        ]
    }
    scenarios_df = pd.DataFrame(scenarios_data)
    scenarios_df.to_excel(writer, sheet_name='Scenarios', index=False)
    
    # 7. DOCUMENTATION WORKSHEET (Enhanced)
    documentation_data = {
        'Section': [
            'OVERVIEW', '', '', '',
            'Purpose', 'Scope', 'Audience', 'Last Updated',
            '', 'KEY ASSUMPTIONS', '', '',
            'Environment Type', 'Usage Pattern', 'Geographic Region', 'Database Strategy',
            '', 'WORKSHEET DESCRIPTIONS', '', '',
            'Summary', 'Assumptions', 'AWS Pricing', 'Bill of Materials',
            'Calculations', 'Scenarios', 'Documentation', '',
            'VECTOR DATABASE STRATEGY', '', '', '',
            'S3 Vectors', 'OpenSearch Service', 'Pinecone', 'Use Case Guidance',
            '', 'GRAPH DATABASE STRATEGY', '', '',
            'Amazon Neptune', 'Neo4j on EC2', 'GraphRAG Integration', 'Knowledge Graph Design',
            '', 'COST OPTIMIZATION TIPS', '', '',
            'Same-AZ Placement', 'Vector Storage Optimization', 'Graph Query Optimization', 'Resource Right-sizing',
            'Scheduled Scaling', 'Database Selection', 'Caching Strategy', '',
            'DATA SOURCES', '', '', '',
            'AWS Pricing Calculator', 'Vector Database Pricing', 'Graph Database Pricing', 'AgentCore Documentation',
            '', 'MAINTENANCE', '', '',
            'Monthly Review', 'Quarterly Adjustment', 'Annual Planning', 'Price Updates'
        ],
        'Description': [
            '', '', '', '',
            'AWS AgentCore cost model with vector and graph databases',
            'Learning, experimentation, PoC development with AI knowledge',
            'IT architects, finance teams, AI project managers',
            datetime.now().strftime('%Y-%m-%d'),
            '', '', '', '',
            'Sandbox/development with vector and graph capabilities',
            'Business hours, moderate usage, AI knowledge integration',
            'US East (N. Virginia) - us-east-1',
            'Hybrid vector + graph database strategy',
            '', '', '', '',
            'Executive dashboard with enhanced database cost breakdown',
            'Project parameters including vector/graph assumptions',
            'Current AWS service pricing including databases',
            'Detailed component quantities with database specifications',
            'Cost formulas including database cost ratios',
            'Multiple usage scenarios including database workloads',
            'This enhanced reference guide',
            '', '', '', '', '',
            'Cost-effective vector storage, 90% savings vs alternatives',
            'Hybrid text + vector search, AWS native integration',
            'Pure vector search, best performance for vector workloads',
            'Use S3 Vectors for cost, OpenSearch for hybrid, Pinecone for performance',
            '', '', '', '',
            'Serverless graph database, GraphRAG integration',
            'Self-managed graph database for custom requirements',
            'Knowledge graph RAG for enhanced AI responses',
            'Entity-relationship modeling for domain knowledge',
            '', '', '', '',
            'Deploy services in same AZ to avoid data transfer costs',
            'Use S3 Vectors for cold storage, OpenSearch for hot queries',
            'Optimize graph query patterns and indexing strategies',
            'Size instances based on actual vector/graph workloads',
            'Scale down databases during off-hours',
            'Choose appropriate database for workload characteristics',
            'Implement vector and graph result caching',
            '', '', '', '', '',
            'https://calculator.aws/',
            'Vector database vendor pricing pages',
            'Neptune and Neo4j pricing documentation',
            'AWS AgentCore service documentation',
            '', '', '', '',
            'Review actual vs. estimated costs and database usage',
            'Adjust database assumptions based on usage patterns',
            'Plan for vector/graph storage growth and optimization',
            'Update database pricing data quarterly'
        ],
        'Reference/Link': [
            '', '', '', '',
            'README.md', 'AI project charter', 'Stakeholder list', 'Version control',
            '', '', '', '',
            'Assumptions worksheet', 'Usage analysis', 'AWS region selection', 'Database selection guide',
            '', '', '', '',
            'Summary worksheet', 'Assumptions worksheet', 'AWS Pricing worksheet', 'Bill of Materials worksheet',
            'Calculations worksheet', 'Scenarios worksheet', 'Documentation worksheet', '',
            '', '', '', '',
            'S3 Vectors documentation', 'OpenSearch Service docs', 'Pinecone documentation', 'Vector database comparison',
            '', '', '', '',
            'Neptune documentation', 'Neo4j documentation', 'GraphRAG best practices', 'Knowledge graph design patterns',
            '', '', '', '',
            'AWS Well-Architected Framework', 'Vector optimization guide', 'Graph performance tuning', 'Database monitoring',
            'Auto Scaling', 'Database selection matrix', 'Caching best practices', '',
            '', '', '', '',
            'AWS Calculator', 'Vector DB pricing', 'Graph DB pricing', 'AgentCore docs',
            '', '', '', '',
            'Cost analysis report', 'Growth planning', 'Budget planning', 'Price monitoring'
        ],
        'Action Required': [
            '', '', '', '',
            'No action', 'No action', 'No action', 'Update monthly',
            '', '', '', '',
            'Validate quarterly', 'Monitor continuously', 'No action', 'Review database choices',
            '', '', '', '',
            'Update formulas as needed', 'Review monthly', 'Update quarterly', 'Review monthly',
            'Validate formulas', 'Add new scenarios', 'Update as needed', '',
            '', '', '', '',
            'Evaluate for cost optimization', 'Consider for hybrid workloads', 'Evaluate for performance needs', 'Document decision criteria',
            '', '', '', '',
            'Plan GraphRAG integration', 'Consider for custom graphs', 'Implement GraphRAG', 'Design knowledge model',
            '', '', '', '',
            'Implement as needed', 'Monitor storage costs', 'Optimize query performance', 'Monitor and adjust',
            'Configure as needed', 'Evaluate database fit', 'Implement as needed', '',
            '', '', '', '',
            'Bookmark for reference', 'Research pricing models', 'Compare alternatives', 'Bookmark for reference',
            '', '', '', '',
            'Schedule monthly', 'Schedule quarterly', 'Schedule annually', 'Set alerts'
        ]
    }
    documentation_df = pd.DataFrame(documentation_data)
    documentation_df.to_excel(writer, sheet_name='Documentation', index=False)

print(f"Enhanced Excel file created successfully at: {excel_path}")
print("Worksheets included:")
print("1. Summary - Monthly cost overview with vector/graph databases")
print("2. Assumptions - Enhanced project parameters")
print("3. AWS Pricing - Current service pricing including databases")
print("4. Bill of Materials - Enhanced component details")
print("5. Calculations - Enhanced cost formulas with database ratios")
print("6. Scenarios - Updated scenarios including database workloads")
print("7. Documentation - Enhanced reference guide")
print("\nNew Features:")
print("- Vector Database Services: S3 Vectors, OpenSearch, Pinecone")
print("- Graph Database Services: Neptune, Neo4j, GraphRAG")
print("- Enhanced cost modeling for AI knowledge systems")
print("- Database selection guidance and optimization tips")