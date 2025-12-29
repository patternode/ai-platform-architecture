import pandas as pd
import numpy as np
from datetime import datetime
import os

# Create the Excel writer object
excel_path = r'd:\Work\BNZ\work-bnz\02-architecture\03-agentic-ai\06-community\AWS-AgentCore-Cost-Model.xlsx'

with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
    
    # 1. SUMMARY WORKSHEET
    summary_data = {
        'Cost Category': [
            'AgentCore Services',
            'Foundation Models (Bedrock)',
            'Supporting AWS Services',
            'Data Transfer & Storage',
            'Monitoring & Logging',
            'Network Infrastructure',
            'Security & Compliance',
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
            '=SUM(B1:B7)'
        ],
        'Percentage': [
            '=B1/$B$8*100',
            '=B2/$B$8*100',
            '=B3/$B$8*100',
            '=B4/$B$8*100',
            '=B5/$B$8*100',
            '=B6/$B$8*100',
            '=B7/$B$8*100',
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
            'Total estimated monthly cost'
        ]
    }
    summary_df = pd.DataFrame(summary_data)
    summary_df.to_excel(writer, sheet_name='Summary', index=False)
    
    # 2. ASSUMPTIONS WORKSHEET
    assumptions_data = {
        'Category': [
            'PROJECT ASSUMPTIONS', '', '', '',
            'Team Size', 'Active Hours per Day', 'Working Days per Month', 'Sessions per User per Day',
            'Average Session Duration', 'Peak Concurrent Users', 'Data Storage Growth', '',
            'MODEL USAGE DISTRIBUTION', '', '', '',
            'Claude 3.5 Sonnet', 'Claude 3.5 Haiku', 'Llama 3.1 70B', 'Llama 3.1 8B',
            'Average Input Tokens per Session', 'Average Output Tokens per Session', '',
            'TECHNICAL SPECIFICATIONS', '', '', '',
            'CPU Usage per Session', 'Memory Usage per Session', 'Storage per User', 'Log Retention Period',
            'AWS Region', 'Availability Zones', 'VPC CIDR', 'Environment Type',
            '', 'USAGE PATTERNS', '', '',
            'Peak Usage Hours', 'Off-Peak Multiplier', 'Weekend Multiplier', 'Growth Rate per Quarter',
            'Experiment Frequency', 'Training Session Frequency'
        ],
        'Value': [
            '', '', '', '',
            10, 8, 22, 3,
            120, 5, 10, '',
            '', '', '', '',
            40, 30, 20, 10,
            500, 300, '',
            '', '', '', '',
            0.5, 1, 5, 30,
            'us-east-1', 2, '10.0.0.0/16', 'Sandbox',
            '', '', '', '',
            '9:00-17:00', 0.3, 0.1, 15,
            2, 1
        ],
        'Unit': [
            '', '', '', '',
            'People', 'Hours', 'Days', 'Sessions',
            'Seconds', 'Users', 'GB/Month', '',
            '', '', '', '',
            '%', '%', '%', '%',
            'Tokens', 'Tokens', '',
            '', '', '', '',
            'vCPU', 'GB', 'GB', 'Days',
            'Region', 'Count', 'CIDR', 'Type',
            '', '', '', '',
            'Time', 'Factor', 'Factor', '%',
            'per Week', 'per Month'
        ],
        'Description': [
            '', '', '', '',
            'Number of sandbox users in community', 'Daily active usage hours', 'Business days per month', 'AgentCore sessions per user daily',
            'Typical session length', 'Maximum simultaneous users', 'Monthly data accumulation', '',
            '', '', '', '',
            'Percentage of model usage', 'Percentage of model usage', 'Percentage of model usage', 'Percentage of model usage',
            'Typical prompt size', 'Typical response size', '',
            '', '', '', '',
            'Processing requirement', 'RAM requirement', 'Individual storage allocation', 'CloudWatch log retention',
            'Primary deployment region', 'Multi-AZ deployment', 'Network address space', 'Development/learning environment',
            '', '', '', '',
            'Daily peak period', 'Usage reduction factor', 'Weekend usage reduction', 'Quarterly usage growth',
            'PoC/PoV experiments per user', 'Formal training sessions'
        ]
    }
    assumptions_df = pd.DataFrame(assumptions_data)
    assumptions_df.to_excel(writer, sheet_name='Assumptions', index=False)
    
    # 3. AWS PRICING WORKSHEET
    pricing_data = {
        'Category': [
            'AgentCore Runtime', 'AgentCore Runtime', 'AgentCore Browser', 'AgentCore Browser',
            'AgentCore Code Interpreter', 'AgentCore Code Interpreter', 'AgentCore Gateway', 'AgentCore Gateway',
            'AgentCore Gateway', 'AgentCore Observability', 'AgentCore Observability', 'AgentCore Observability',
            'Bedrock Claude 3.5 Sonnet', 'Bedrock Claude 3.5 Sonnet', 'Bedrock Claude 3.5 Haiku', 'Bedrock Claude 3.5 Haiku',
            'Bedrock Claude 3 Opus', 'Bedrock Claude 3 Opus', 'Bedrock Llama 3.1 70B', 'Bedrock Llama 3.1 70B',
            'Bedrock Llama 3.1 8B', 'Bedrock Llama 3.1 8B', 'EC2 t3.micro', 'EC2 t3.small',
            'EC2 t3.medium', 'EC2 t3.large', 'EC2 t4g.micro', 'EC2 t4g.small',
            'Lambda Requests', 'Lambda Duration x86', 'Lambda Duration ARM', 'S3 Standard Storage',
            'S3 Standard-IA Storage', 'S3 GET Requests', 'S3 PUT Requests', 'DynamoDB On-Demand RRU',
            'DynamoDB On-Demand WRU', 'DynamoDB Storage', 'CloudWatch Custom Metrics', 'CloudWatch Log Ingestion',
            'CloudWatch Log Storage', 'CloudWatch Dashboards', 'VPC NAT Gateway Hours', 'VPC NAT Gateway Data',
            'Data Transfer Same AZ', 'Data Transfer Inter-AZ', 'Data Transfer Inter-Region', 'Data Transfer Internet 1GB-10TB'
        ],
        'Component': [
            'CPU Usage', 'Memory Usage', 'CPU Usage', 'Memory Usage',
            'CPU Usage', 'Memory Usage', 'MCP Operations', 'Search Queries',
            'Tool Indexing', 'Data Ingestion', 'Data Storage', 'Queries',
            'Input Tokens', 'Output Tokens', 'Input Tokens', 'Output Tokens',
            'Input Tokens', 'Output Tokens', 'Input Tokens', 'Output Tokens',
            'Input Tokens', 'Output Tokens', 'Instance Hour', 'Instance Hour',
            'Instance Hour', 'Instance Hour', 'Instance Hour', 'Instance Hour',
            'Requests', 'GB-seconds', 'GB-seconds', 'Storage',
            'Storage', 'Requests', 'Requests', 'Read Request Units',
            'Write Request Units', 'Storage', 'Metrics', 'Data Ingestion',
            'Data Storage', 'Dashboard', 'Instance Hours', 'Data Processing',
            'Data Transfer', 'Data Transfer', 'Data Transfer', 'Data Transfer'
        ],
        'Unit': [
            'per vCPU-second', 'per GB-second', 'per vCPU-second', 'per GB-second',
            'per vCPU-second', 'per GB-second', 'per operation', 'per query',
            'per tool indexed', 'per GB', 'per GB-month', 'per 1000 queries',
            'per 1K tokens', 'per 1K tokens', 'per 1K tokens', 'per 1K tokens',
            'per 1K tokens', 'per 1K tokens', 'per 1K tokens', 'per 1K tokens',
            'per 1K tokens', 'per 1K tokens', 'per hour', 'per hour',
            'per hour', 'per hour', 'per hour', 'per hour',
            'per 1M requests', 'per GB-second', 'per GB-second', 'per GB-month',
            'per GB-month', 'per 1K requests', 'per 1K requests', 'per 1M RRUs',
            'per 1M WRUs', 'per GB-month', 'per metric-month', 'per GB',
            'per GB-month', 'per dashboard-month', 'per hour', 'per GB',
            'per GB', 'per GB', 'per GB', 'per GB'
        ],
        'Current Price (USD)': [
            0.0000248611, 0.00000262500, 0.0000248611, 0.00000262500,
            0.0000248611, 0.00000262500, 0.001000, 0.001000,
            0.001000, 0.50, 0.03, 0.005,
            0.003000, 0.015000, 0.000250, 0.001250,
            0.015000, 0.075000, 0.00099, 0.00099,
            0.00022, 0.00022, 0.0104, 0.0208,
            0.0416, 0.0832, 0.0084, 0.0168,
            0.20, 0.0000166667, 0.0000133334, 0.023,
            0.0125, 0.0004, 0.005, 0.25,
            1.25, 0.25, 0.30, 0.50,
            0.03, 3.00, 0.045, 0.045,
            0.00, 0.01, 0.02, 0.09
        ],
        'Region': ['us-east-1'] * 48,
        'Last Updated': ['2024-12-01'] * 48,
        'Notes': [
            'Consumption-based billing', 'Peak memory consumed', 'Same as Runtime pricing', 'Same as Runtime pricing',
            'Same as Runtime pricing', 'Same as Runtime pricing', 'ListTools CallTool operations', 'Semantic search functionality',
            'One-time indexing cost', 'CloudWatch Logs ingestion', 'CloudWatch Logs storage', 'Log analysis queries',
            'Text generation input', 'Text generation output', 'Lightweight model', 'Lightweight model',
            'Most capable model', 'Most capable model', 'Open source model', 'Open source model',
            'Smaller open source', 'Smaller open source', 'Burstable performance', 'Burstable performance',
            'Burstable performance', 'Burstable performance', 'ARM-based Graviton2', 'ARM-based Graviton2',
            'First 1M free monthly', 'First 400K GB-s free', 'Graviton2 ARM processors', 'First 50TB pricing tier',
            'Infrequent access', 'Data retrieval', 'Data upload', 'Pay per request',
            'Pay per request', 'Data storage', 'First 10K free', 'First 5GB free monthly',
            'Compressed storage', 'Up to 50 metrics', 'Highly available NAT', 'Data processed',
            'Free within same AZ', 'Between AZs same region', 'US East to US West', 'Next 9.999TB'
        ]
    }
    pricing_df = pd.DataFrame(pricing_data)
    pricing_df.to_excel(writer, sheet_name='AWS Pricing', index=False)
    
    # 4. BILL OF MATERIALS WORKSHEET
    bom_data = {
        'Service Category': [
            'AgentCore Services', 'AgentCore Services', 'AgentCore Services', 'AgentCore Services',
            'Foundation Models', 'Foundation Models', 'Foundation Models', 'Foundation Models',
            'Compute Services', 'Compute Services', 'Compute Services', 'Compute Services',
            'Storage Services', 'Storage Services', 'Storage Services', 'Database Services',
            'Database Services', 'Database Services', 'Monitoring Services', 'Monitoring Services',
            'Monitoring Services', 'Network Services', 'Network Services', 'Network Services',
            'Security Services', 'Security Services', 'Vector Database Services', 'Vector Database Services',
        'Vector Database Services', 'Graph Database Services', 'Graph Database Services', 'Graph Database Services',
        'Graph Database Services', 'Graph Database Services'
        ],
        'Component': [
            'AgentCore Runtime', 'AgentCore Browser', 'AgentCore Code Interpreter', 'AgentCore Gateway',
            'Claude 3.5 Sonnet', 'Claude 3.5 Haiku', 'Llama 3.1 70B', 'Llama 3.1 8B',
            'EC2 t3.medium', 'EC2 t4g.small', 'Lambda Functions', 'Lambda ARM Functions',
            'S3 Standard Storage', 'S3 Standard-IA Storage', 'S3 API Operations', 'DynamoDB Tables',
            'DynamoDB Read Units', 'DynamoDB Write Units', 'CloudWatch Metrics', 'CloudWatch Logs',
            'CloudWatch Dashboards', 'VPC NAT Gateway', 'Application Load Balancer', 'Data Transfer',
            'KMS Keys', 'SSL Certificates', 'S3 Vectors Storage', 'OpenSearch Serverless',
            'Pinecone Vector DB', 'Neptune Serverless', 'Neptune ML', 'Neptune Storage',
            'Neptune I/O Operations', 'Neo4j on EC2'
        ],
        'Quantity': [
            '=Assumptions!B5*Assumptions!B6*Assumptions!B7*Assumptions!B8', 
            '=B1*0.3', '=B1*0.2', '=B1*100',
            '=Assumptions!B17/100', '=Assumptions!B18/100', '=Assumptions!B19/100', '=Assumptions!B20/100',
            2, 1, '=B1', '=B1*0.5',
            '=Assumptions!B11*Assumptions!B5', '=B13*0.3', '=B1*1000', 3,
            '=B1*10000', '=B1*1000', '=Assumptions!B5*5', '=B1*0.1',
            1, 1, 1, '=B1*0.001',
            2, 1, '=Assumptions!B11*2', '=C27*24*22', 0.5, '=C29*24*22', '=C29*0.5', '=C29*5',
            '=C29*100000', 1
        ],
        'Unit': [
            'Sessions/Month', 'Sessions/Month', 'Sessions/Month', 'Operations/Month',
            'Usage %', 'Usage %', 'Usage %', 'Usage %',
            'Instances', 'Instances', 'Invocations/Month', 'Invocations/Month',
            'GB', 'GB', 'API Calls/Month', 'Tables',
            'RRUs/Month', 'WRUs/Month', 'Metrics', 'GB/Month',
            'Dashboards', 'Hours/Month', 'Hours/Month', 'GB/Month',
            'Keys', 'Certificates', 'GB', 'Search OCU Hours/Month',
            'Pods', 'NCU Hours/Month', 'Training Hours/Month', 'GB',
            'Million I/Os/Month', 'Instance Hours/Month'
        ],
        'Monthly Usage': [
            '=C1', '=C2', '=C3', '=C4',
            '=C5', '=C6', '=C7', '=C8',
            '=C9*24*Assumptions!B7', '=C10*24*Assumptions!B7', '=C11', '=C12',
            '=C13', '=C14', '=C15', '=C16',
            '=C17', '=C18', '=C19', '=C20',
            '=C21', '=C22*24*Assumptions!B7', '=C23*24*Assumptions!B7', '=C24',
            '=C25', '=C26', '=C27', '=C28*24*Assumptions!B7', '=C29',
            '=C30*24*Assumptions!B7', '=C31', '=C32', '=C33', '=C34*24*Assumptions!B7'
        ],
        'Unit Cost (USD)': [
            '=(AWS_Pricing!E1*Assumptions!B25+AWS_Pricing!E2*Assumptions!B26)*Assumptions!B9',
            '=(AWS_Pricing!E3*Assumptions!B25+AWS_Pricing!E4*Assumptions!B26)*Assumptions!B9',
            '=(AWS_Pricing!E5*Assumptions!B25+AWS_Pricing!E6*Assumptions!B26)*Assumptions!B9',
            'AWS_Pricing!E7',
            '=(AWS_Pricing!E13*Assumptions!B21+AWS_Pricing!E14*Assumptions!B22)*C1/1000',
            '=(AWS_Pricing!E15*Assumptions!B21+AWS_Pricing!E16*Assumptions!B22)*C1/1000',
            '=(AWS_Pricing!E19*Assumptions!B21+AWS_Pricing!E20*Assumptions!B22)*C1/1000',
            '=(AWS_Pricing!E21*Assumptions!B21+AWS_Pricing!E22*Assumptions!B22)*C1/1000',
            'AWS_Pricing!E25', 'AWS_Pricing!E28', 'AWS_Pricing!E30*1', 'AWS_Pricing!E31*1',
            'AWS_Pricing!E32', 'AWS_Pricing!E33', 'AWS_Pricing!E34', 'AWS_Pricing!E38',
            'AWS_Pricing!E36', 'AWS_Pricing!E37', 'AWS_Pricing!E39', 'AWS_Pricing!E40',
            'AWS_Pricing!E42', 'AWS_Pricing!E43', 100, 'AWS_Pricing!E48',
            50, 0, 'AWS_Pricing!E59', 'AWS_Pricing!E61', 'AWS_Pricing!E64', 'AWS_Pricing!E66',
            'AWS_Pricing!E70', 'AWS_Pricing!E67', 'AWS_Pricing!E68', 'AWS_Pricing!E74'
        ],
        'Monthly Cost (USD)': [
            '=D1*E1', '=D2*E2', '=D3*E3', '=D4*E4',
            '=D5*E5', '=D6*E6', '=D7*E7', '=D8*E8',
            '=D9*E9', '=D10*E10', '=D11*E11', '=D12*E12',
            '=D13*E13', '=D14*E14', '=D15*E15', '=D16*E16',
            '=D17*E17/1000000', '=D18*E18/1000000', '=D19*E19', '=D20*E20',
            '=D21*E21', '=D22*E22', '=D23*E23', '=D24*E24',
            '=D25*E25', '=D26*E26', '=D27*E27', '=D28*E28', '=D29*E29',
            '=D30*E30', '=D31*E31', '=D32*E32', '=D33*E33', '=D34*E34'
        ]
    }
    bom_df = pd.DataFrame(bom_data)
    bom_df.to_excel(writer, sheet_name='Bill of Materials', index=False)
    
    # 5. CALCULATIONS WORKSHEET
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
            'Q4 Estimate (cumulative)'
        ],
        'Formula/Value': [
            '=SUM(BOM!F1:F4)',
            '=SUM(BOM!F5:F8)',
            '=SUM(BOM!F9:F16)',
            '=SUM(BOM!F13:F15,BOM!F24)',
            '=SUM(BOM!F19:F21)',
            '=SUM(BOM!F22:F23)',
            '=SUM(BOM!F25:F26)',
            '=SUM(BOM!F27:F29)',
            '=SUM(BOM!F30:F34)',
            '=B1+B2+B3+B4+B5+B6+B7+B8+B9',
            '',
            '',
            '=B8*0.7',
            '=B8*0.2',
            '=B8*0.1',
            '',
            '',
            '=B8/Assumptions!B5',
            '=B16/Assumptions!B7',
            '=B16/(Assumptions!B5*Assumptions!B7*Assumptions!B8)',
            '',
            '',
            '=B8*3',
            '=B21*1.15',
            '=B22*1.15',
            '=B23*1.15'
        ],
        'Result (USD)': [
            '', '', '', '', '', '', '', '',
            '', '', '', '', '',
            '', '', '', '', '',
            '', '', '', '', '', ''
        ],
        'Notes': [
            'Runtime, Browser, Code Interpreter, Gateway costs',
            'All Bedrock model inference costs',
            'EC2, Lambda, S3, DynamoDB costs',
            'Storage and data transfer costs',
            'CloudWatch metrics, logs, dashboards',
            'VPC, NAT Gateway, ALB costs',
            'KMS keys and SSL certificates',
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
            'Fourth quarter projection'
        ]
    }
    calculations_df = pd.DataFrame(calculations_data)
    calculations_df.to_excel(writer, sheet_name='Calculations', index=False)
    
    # 6. SCENARIOS WORKSHEET
    scenarios_data = {
        'Scenario': [
            'Baseline (Current)', 'Light Usage', 'Heavy Usage', 'Training Event',
            'Quarter End', 'Experiment Phase', 'Production Pilot', 'Full Rollout'
        ],
        'Team Size': [10, 5, 15, 25, 10, 20, 10, 50],
        'Sessions/User/Day': [3, 2, 5, 8, 4, 6, 3, 4],
        'Session Duration (sec)': [120, 90, 180, 300, 150, 240, 120, 180],
        'Model Mix - Claude %': [40, 30, 50, 60, 45, 40, 40, 35],
        'Monthly Cost': [
            '=Calculations!B8',
            '=Calculations!B8*0.4',
            '=Calculations!B8*1.8',
            '=Calculations!B8*4.2',
            '=Calculations!B8*1.3',
            '=Calculations!B8*2.4',
            '=Calculations!B8*1.0',
            '=Calculations!B8*6.5'
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
            'Month-end reporting spike',
            'Multiple PoCs running',
            'Pre-production testing',
            'Full community deployment'
        ]
    }
    scenarios_df = pd.DataFrame(scenarios_data)
    scenarios_df.to_excel(writer, sheet_name='Scenarios', index=False)
    
    # 7. DOCUMENTATION WORKSHEET
    documentation_data = {
        'Section': [
            'OVERVIEW', '', '', '',
            'Purpose', 'Scope', 'Audience', 'Last Updated',
            '', 'KEY ASSUMPTIONS', '', '',
            'Environment Type', 'Usage Pattern', 'Geographic Region', 'Cost Optimization',
            '', 'WORKSHEET DESCRIPTIONS', '', '',
            'Summary', 'Assumptions', 'AWS Pricing', 'Bill of Materials',
            'Calculations', 'Scenarios', 'Documentation', '',
            'COST OPTIMIZATION TIPS', '', '', '',
            'Same-AZ Placement', 'Model Selection', 'Caching Strategy', 'Resource Right-sizing',
            'Scheduled Scaling', 'Reserved Instances', 'Spot Instances', '',
            'DATA SOURCES', '', '', '',
            'AWS Pricing Calculator', 'Bedrock Pricing', 'AgentCore Documentation', 'CloudWatch Pricing',
            '', 'MAINTENANCE', '', '',
            'Monthly Review', 'Quarterly Adjustment', 'Annual Planning', 'Price Updates'
        ],
        'Description': [
            '', '', '', '',
            'AWS AgentCore cost model for community sandbox environments',
            'Learning, experimentation, PoC development',
            'IT architects, finance teams, project managers',
            datetime.now().strftime('%Y-%m-%d'),
            '', '', '', '',
            'Sandbox/development, not production',
            'Business hours, moderate usage, learning focus',
            'US East (N. Virginia) - us-east-1',
            'Basic level, standard configurations',
            '', '', '', '',
            'Executive dashboard with monthly cost breakdown',
            'Project parameters and usage assumptions',
            'Current AWS service pricing (updatable)',
            'Detailed component quantities and specifications',
            'Cost formulas and calculations',
            'Multiple usage scenarios for comparison',
            'This reference guide and maintenance notes',
            '', '', '', '', '',
            'Deploy services in same AZ to avoid data transfer costs',
            'Use appropriate model for task complexity (Haiku vs Sonnet)',
            'Implement response caching to reduce model calls',
            'Size EC2 instances based on actual usage patterns',
            'Scale down during off-hours and weekends',
            'Consider RIs for predictable baseline workloads',
            'Use Spot for non-critical development workloads',
            '', '', '', '', '',
            'https://calculator.aws/',
            'https://aws.amazon.com/bedrock/pricing/',
            'AWS AgentCore service documentation',
            'https://aws.amazon.com/cloudwatch/pricing/',
            '', '', '', '',
            'Review actual vs. estimated costs monthly',
            'Adjust assumptions based on usage patterns',
            'Plan for growth and new use cases',
            'Update pricing data quarterly or as needed'
        ],
        'Reference/Link': [
            '', '', '', '',
            'README.md', 'Project charter', 'Stakeholder list', 'Version control',
            '', '', '', '',
            'Assumptions worksheet', 'Usage analysis', 'AWS region selection', 'Cost optimization guide',
            '', '', '', '',
            'Summary worksheet', 'Assumptions worksheet', 'AWS Pricing worksheet', 'Bill of Materials worksheet',
            'Calculations worksheet', 'Scenarios worksheet', 'Documentation worksheet', '',
            '', '', '', '',
            'AWS Well-Architected Framework', 'Bedrock model comparison', 'CloudFront caching', 'CloudWatch metrics',
            'Auto Scaling', 'RI recommendations', 'EC2 Spot pricing', '',
            '', '', '', '',
            'AWS Calculator', 'Bedrock docs', 'AgentCore docs', 'CloudWatch docs',
            '', '', '', '',
            'Cost analysis report', 'Growth planning', 'Budget planning', 'Price monitoring'
        ],
        'Action Required': [
            '', '', '', '',
            'No action', 'No action', 'No action', 'Update monthly',
            '', '', '', '',
            'Validate quarterly', 'Monitor continuously', 'No action', 'Review quarterly',
            '', '', '', '',
            'Update formulas as needed', 'Review monthly', 'Update quarterly', 'Review monthly',
            'Validate formulas', 'Add new scenarios', 'Update as needed', '',
            '', '', '', '',
            'Implement as needed', 'Optimize based on usage', 'Implement as needed', 'Monitor and adjust',
            'Configure as needed', 'Evaluate annually', 'Consider for dev/test', '',
            '', '', '', '',
            'Bookmark for reference', 'Bookmark for reference', 'Bookmark for reference', 'Bookmark for reference',
            '', '', '', '',
            'Schedule monthly', 'Schedule quarterly', 'Schedule annually', 'Set alerts'
        ]
    }
    documentation_df = pd.DataFrame(documentation_data)
    documentation_df.to_excel(writer, sheet_name='Documentation', index=False)

print(f"Excel file created successfully at: {excel_path}")
print("Worksheets included:")
print("1. Summary - Monthly cost overview")
print("2. Assumptions - Project parameters")
print("3. AWS Pricing - Current service pricing")
print("4. Bill of Materials - Component details")
print("5. Calculations - Cost formulas")
print("6. Scenarios - Usage scenarios")
print("7. Documentation - Reference guide")