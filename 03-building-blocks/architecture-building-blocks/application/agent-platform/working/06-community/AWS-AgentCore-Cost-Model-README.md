# AWS AgentCore Cost Model for Community Sandbox Environments

## Overview

This comprehensive Excel-based cost model helps estimate monthly AWS costs for community learning environments focused on AWS AgentCore and agentic AI technologies. The model is specifically designed for sandbox environments where teams experiment with proof-of-concept and proof-of-value projects.

## Files Included

- **AWS-AgentCore-Cost-Model.xlsx** - Main cost model with 7 worksheets
- **AWS-Pricing-Table.csv** - Detailed pricing reference (Dec 2024)
- **create_cost_model.py** - Python script for regenerating the Excel file
- **AWS-AgentCore-Cost-Model-README.md** - This documentation

## Worksheets Structure

### 1. **Summary**
- Executive dashboard showing monthly cost breakdown by category
- High-level cost distribution and percentages
- Quick reference for budget planning
- Automatic calculations from other worksheets

### 2. **Assumptions** 
- Project parameters (team size, usage patterns, session characteristics)
- Model usage distribution (Claude vs Llama variants)
- Technical specifications (CPU, memory, storage requirements)
- Configurable variables that drive all cost calculations
- **Key Variables to Customize:**
  - Team Size (default: 10 people)
  - Sessions per User per Day (default: 3)
  - Session Duration (default: 120 seconds)
  - Model Mix percentages

### 3. **AWS Pricing**
- Current pricing for all AWS services (as of December 2024)
- AgentCore consumption-based pricing (CPU-seconds, GB-seconds)
- Bedrock foundation model token pricing
- Supporting service costs (EC2, Lambda, S3, DynamoDB, CloudWatch)
- **Update quarterly** or when AWS announces price changes

### 4. **Bill of Materials**
- Detailed component specifications and quantities
- Monthly usage calculations based on assumptions
- Unit costs and total monthly costs per component
- Formulas link to Assumptions and Pricing worksheets

### 5. **Calculations**
- Cost formulas and aggregations
- Usage pattern breakdowns (peak/off-peak/weekend)
- Per-user cost metrics
- Quarterly growth projections with 15% quarterly growth factor

### 6. **Scenarios**
- Multiple usage scenarios (baseline, light, heavy, training events)
- Scenario-specific cost estimates
- Comparison matrix for planning different phases
- **8 Pre-configured Scenarios:**
  - Baseline (Current)
  - Light Usage  
  - Heavy Usage
  - Training Event
  - Quarter End
  - Experiment Phase
  - Production Pilot
  - Full Rollout

### 7. **Documentation**
- Reference guide and maintenance instructions
- Cost optimization recommendations
- Data sources and update procedures
- Maintenance schedule and action items

## Key Cost Components

### AgentCore Services ($0.0000248611/vCPU-second, $0.00000262500/GB-second)
- **Runtime**: CPU and memory consumption per second
- **Browser Tool**: Same pricing model as Runtime  
- **Code Interpreter**: Sandbox execution pricing
- **Gateway**: MCP operations ($0.001/operation), search queries, tool indexing
- **Observability**: CloudWatch integration for telemetry

### Bedrock Foundation Models (Token-based pricing)
- **Claude 3.5 Sonnet**: $0.003 input, $0.015 output per 1K tokens
- **Claude 3.5 Haiku**: $0.00025 input, $0.00125 output per 1K tokens  
- **Llama 3.1 70B**: $0.00099 input/output per 1K tokens
- **Llama 3.1 8B**: $0.00022 input/output per 1K tokens

### Supporting AWS Services
- **Compute**: EC2 instances (t3.medium $0.0416/hour), Lambda functions
- **Storage**: S3 buckets ($0.023/GB-month), DynamoDB tables
- **Monitoring**: CloudWatch metrics, logs ($0.50/GB ingestion), dashboards
- **Networking**: VPC, NAT Gateway ($0.045/hour), data transfer

## Usage Patterns for Sandbox Environments

- **Learning & Experimentation**: Moderate usage during business hours
- **Proof of Concept Development**: Burst usage during active development
- **Training Events**: High usage during scheduled workshops
- **Knowledge Sharing**: Regular but predictable usage patterns

### Default Assumptions
- 10-person team
- 3 sessions per user per day
- 120-second average session duration
- 22 working days per month
- 8 active hours per day
- Mixed model usage (40% Sonnet, 30% Haiku, 20% Llama 70B, 10% Llama 8B)

## Cost Optimization Recommendations

The model assumes non-production workloads with cost optimization opportunities:

1. **Same-AZ Placement**: Deploy services in same AZ to avoid $0.01/GB data transfer costs
2. **Model Selection**: Use Haiku for simple tasks, Sonnet for complex reasoning
3. **Caching Strategy**: Implement response caching to reduce model inference calls
4. **Resource Right-sizing**: Size EC2 instances based on actual usage patterns
5. **Scheduled Scaling**: Scale down during off-hours and weekends (70% peak, 20% off-peak, 10% weekend)
6. **Reserved Instances**: Consider RIs for predictable baseline workloads
7. **Spot Instances**: Use Spot for non-critical development workloads

## How to Use This Model

### Initial Setup
1. Open `AWS-AgentCore-Cost-Model.xlsx`
2. Review and customize the **Assumptions** worksheet for your specific environment
3. Verify pricing in **AWS Pricing** worksheet (update if needed)
4. Check the **Summary** worksheet for total monthly cost estimate

### Scenario Planning
1. Use the **Scenarios** worksheet to compare different usage patterns
2. Create custom scenarios by copying and modifying existing ones
3. Adjust team size, session frequency, and model mix for each scenario

### Monthly Updates
1. Update actual usage data in **Assumptions** worksheet
2. Compare actual costs with estimates
3. Adjust assumptions based on real usage patterns
4. Review **Calculations** worksheet for cost trends

### Quarterly Reviews
1. Update **AWS Pricing** worksheet with current rates
2. Adjust growth projections in **Calculations** worksheet
3. Add new scenarios for upcoming initiatives
4. Review cost optimization opportunities

## Estimated Costs (Baseline Scenario)

Based on default assumptions (10-person team, moderate usage):
- **AgentCore Services**: Primary cost driver due to session volume
- **Foundation Models**: Significant cost, varies by model mix
- **Supporting Services**: Baseline infrastructure costs
- **Total Monthly Estimate**: Review Summary worksheet for current calculation

Cost per user scales approximately linearly with team size, with some fixed costs for infrastructure.

## Maintenance Schedule

- **Weekly**: Monitor actual usage vs. assumptions
- **Monthly**: Update Assumptions worksheet with real data
- **Quarterly**: Update AWS Pricing worksheet and review scenarios
- **Annually**: Comprehensive model review and optimization planning

## Support and Updates

- Pricing data source: AWS Pricing Calculator and service documentation
- Model maintained by: Strategy & Architecture Team
- Update frequency: Quarterly or when significant price changes occur
- Version control: Track in git with change log

For questions or assistance with the cost model, contact the AI Platform Architecture team.