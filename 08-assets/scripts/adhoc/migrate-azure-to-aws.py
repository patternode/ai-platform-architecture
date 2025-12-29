#!/usr/bin/env python3
"""
Script: migrate-azure-to-aws.py
Purpose: Replace Azure components with AWS equivalents and use Snowflake for data warehouse/lakes
Author: BNZ Enterprise Architecture
Date: 2025-12-06
"""

import os
import re
from pathlib import Path

# Configuration
USE_CASES_DIR = Path(r"D:\Work\BNZ\ai-platform-architecture\01-motivation\03-use-cases\use-cases")
PATTERNS_DIR = Path(r"D:\Work\BNZ\ai-platform-architecture\03-building-blocks\patterns")

# Component mappings: Azure -> AWS/Snowflake
REPLACEMENTS = [
    # LLM and AI Services
    ("Azure OpenAI Service", "AWS Bedrock"),
    ("Azure OpenAI API", "AWS Bedrock API"),
    ("Azure OpenAI", "AWS Bedrock"),
    ("Azure ML", "AWS SageMaker"),
    ("Azure AutoML", "AWS SageMaker AutoML"),
    ("Azure Anomaly Detector", "AWS Lookout for Metrics"),
    ("Azure Form Recognizer", "AWS Textract"),
    ("Azure Cognitive Services", "AWS AI Services"),
    ("Azure Speech Services", "AWS Transcribe"),
    ("Azure Text Analytics", "AWS Comprehend"),
    ("Azure Translator", "AWS Translate"),
    ("Azure Computer Vision", "AWS Rekognition"),

    # Data Storage and Databases
    ("Azure Data Lake", "Snowflake (Data Lake)"),
    ("Azure Synapse Analytics", "Snowflake"),
    ("Azure Synapse", "Snowflake"),
    ("Cosmos DB", "Amazon DynamoDB"),
    ("Azure Cosmos DB Gremlin", "Amazon Neptune"),
    ("Azure Cosmos DB", "Amazon DynamoDB"),
    ("Azure Blob Storage", "Amazon S3"),
    ("Azure SQL Database", "Amazon RDS"),
    ("Azure SQL", "Amazon RDS"),

    # Data Integration and ETL
    ("Azure Data Factory", "AWS Glue"),
    ("Azure Purview", "AWS Glue Data Catalog"),
    ("Azure Purview Glossary", "AWS Glue Data Catalog"),

    # Messaging and Events
    ("Azure Event Hubs", "Amazon Kinesis"),
    ("Azure Service Bus", "Amazon SQS"),
    ("Event Hubs", "Amazon Kinesis"),

    # Compute and Containers
    ("Azure Kubernetes Service", "Amazon EKS"),
    ("Azure Container Instances", "AWS Fargate"),
    ("Azure Functions", "AWS Lambda"),
    ("Azure App Service", "AWS Elastic Beanstalk"),

    # API and Integration
    ("Azure API Management", "Amazon API Gateway"),
    ("Azure Logic Apps", "AWS Step Functions"),

    # Monitoring and DevOps
    ("Azure Monitor", "Amazon CloudWatch"),
    ("Azure Monitor Alerts", "Amazon CloudWatch Alarms"),
    ("Azure DevOps", "AWS CodePipeline"),
    ("Azure Application Insights", "AWS X-Ray"),
    ("Application Insights", "AWS X-Ray"),

    # Security and Identity
    ("Azure Active Directory", "AWS IAM Identity Center"),
    ("Azure AD", "AWS IAM"),
    ("Azure Key Vault", "AWS Secrets Manager"),

    # General Cloud Platform
    ("Azure Cloud Services", "AWS Cloud Services"),
    ("Cloud (Azure)", "Cloud (AWS)"),
    ("on Azure", "on AWS"),
    ("Feast on Azure", "Feast on AWS"),

    # Inherited compliance
    ("inherited from Azure", "inherited from AWS"),

    # Documentation links
    ("https://learn.microsoft.com/azure/ai-services/openai/", "https://docs.aws.amazon.com/bedrock/"),
    ("https://azure.microsoft.com", "https://aws.amazon.com"),

    # Additional Azure references in comparisons
    ("Azure Document Intelligence", "AWS Textract"),
    ("Azure Blob Archive", "Amazon S3 Glacier"),
    ("S3/Azure Blob", "Amazon S3"),
    ("Azure Blob", "Amazon S3"),
    ("Azure Cost Management", "AWS Cost Explorer"),
    ("Azure Cost API", "AWS Cost Explorer API"),
    ("Azure-native strategy", "AWS-native strategy"),
    ("Azure-native", "AWS-native"),
    ("if Azure-native", "if AWS-native"),
    ("Azure Gov Cloud", "AWS GovCloud"),
    ("Azure Machine Learning", "AWS SageMaker"),
    ("Azure regions", "AWS regions"),
    ("Azure solution accelerator", "AWS solution accelerator"),
    ("Microsoft Semantic Kernel", "AWS Agents SDK"),
    ("Microsoft Agent 365", "AWS Bedrock Agents"),
    ("Azure AI Foundry", "AWS Bedrock"),
    ("Evaluate Azure", "Evaluate GCP"),

    # Documentation URLs
    ("https://learn.microsoft.com/en-us/azure/machine-learning/how-to-machine-learning-interpretability", "https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-explainability.html"),
    ("https://learn.microsoft.com/en-us/azure/ai-services/openai/", "https://docs.aws.amazon.com/bedrock/"),
    ("https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/", "https://docs.aws.amazon.com/textract/"),
    ("https://learn.microsoft.com/en-us/azure/machine-learning/how-to-safely-rollout-online-endpoints", "https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails.html"),
    ("https://docs.microsoft.com/azure/machine-learning/how-to-use-batch-endpoint", "https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html"),
    ("https://learn.microsoft.com/en-us/azure/bot-service/", "https://docs.aws.amazon.com/lex/"),
    ("https://docs.microsoft.com/azure/sentinel/", "https://docs.aws.amazon.com/securityhub/"),
    ("https://docs.microsoft.com/azure/stream-analytics/", "https://docs.aws.amazon.com/kinesisanalytics/"),

    # Security and SIEM
    ("Azure Sentinel", "AWS Security Hub"),
    ("Azure Confidential Ledger", "AWS QLDB"),
    ("Azure Storage Encryption", "AWS S3 Encryption"),
    ("Azure RBAC", "AWS IAM"),
    ("Microsoft Purview", "AWS Macie"),
    ("Azure Defender for Cloud", "AWS GuardDuty"),
    ("Azure Firewall", "AWS Network Firewall"),
    ("Azure E5 licenses", "AWS Enterprise Support"),
    ("Network Security Groups (NSG)", "AWS Security Groups"),

    # Bot and conversational
    ("Microsoft Bot Framework", "Amazon Lex"),
    ("Office 365", "AWS WorkSpaces"),
    ("Azure Bot Service", "Amazon Lex"),

    # Stream Analytics
    ("Azure Stream Analytics", "Amazon Kinesis Analytics"),
    ("Azure DI", "AWS Textract"),

    # Remaining Azure patterns
    ("Azure Batch", "AWS Batch"),
    ("Azure cloud resources", "AWS cloud resources"),
    ("Azure Cloud Environment", "AWS Cloud Environment"),
    ("Azure Amazon DynamoDB", "Amazon DynamoDB"),
    ("integrated with Azure services", "integrated with AWS services"),
    ("Azure integration", "AWS integration"),
    ("Azure ecosystem", "AWS ecosystem"),
    ("integrated with Azure", "integrated with AWS"),
    ("Azure Schema Registry", "AWS Glue Schema Registry"),
    ("Native Azure logging", "Native AWS logging"),
    ("Native Azure cost", "Native AWS cost"),
    ("Microsoft Azure", "AWS"),
    ("primary cloud is Azure", "primary cloud is AWS"),
    ("Azure-first organizations", "AWS-first organizations"),
    ("AWS/GCP/Azure", "AWS/GCP"),
    ("[AWS, Azure, GCP", "[AWS, GCP"),
]

def update_file(filepath):
    """Update Azure references in a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # Skip binary files or files with encoding issues
        return []

    original_content = content
    changes = []

    for azure_term, aws_term in REPLACEMENTS:
        if azure_term in content:
            count = content.count(azure_term)
            content = content.replace(azure_term, aws_term)
            changes.append(f"  {azure_term} -> {aws_term} ({count}x)")

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return changes
    return []

def main():
    print("=" * 70)
    print("Azure to AWS Migration Script")
    print("=" * 70)
    print()
    print("Replacements include:")
    print("  - Azure OpenAI -> AWS Bedrock")
    print("  - Azure Synapse/Data Lake -> Snowflake")
    print("  - Azure Event Hubs -> Amazon Kinesis")
    print("  - Cosmos DB -> Amazon DynamoDB")
    print("  - And 50+ other component mappings")
    print()

    total_files = 0
    total_changes = 0

    # Process all files in use-cases directory (markdown and drawio)
    for root, dirs, files in os.walk(USE_CASES_DIR):
        for filename in files:
            if filename.endswith(('.md', '.drawio')):
                filepath = Path(root) / filename
                changes = update_file(filepath)
                if changes:
                    total_files += 1
                    total_changes += len(changes)
                    print(f"{filepath.name}:")
                    for change in changes:
                        print(change)
                    print()

    # Process all files in patterns directory (markdown and drawio)
    print("\n--- Processing Patterns ---\n")
    for root, dirs, files in os.walk(PATTERNS_DIR):
        for filename in files:
            if filename.endswith(('.md', '.drawio')):
                filepath = Path(root) / filename
                changes = update_file(filepath)
                if changes:
                    total_files += 1
                    total_changes += len(changes)
                    print(f"{filepath.name}:")
                    for change in changes:
                        print(change)
                    print()

    print("=" * 70)
    print(f"Summary: Made {total_changes} replacements in {total_files} files")
    print("=" * 70)

if __name__ == "__main__":
    main()
