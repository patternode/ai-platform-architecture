#!/usr/bin/env python3
"""
Extract BIAN Service Landscape V13.0 Value Chain View elements to CSV
"""

import csv
import re
from collections import defaultdict

def parse_value_chain_elements():
    """
    Parse and organize the BIAN Value Chain View elements based on the extracted text
    """
    
    # All service domains extracted from the Value Chain View
    value_chain_elements = [
        # Business Management
        "Business Management", "Business Direction", "Organization Direction", 
        "Products and Services Direction", "Corporate Strategy", "Corporate Policies",
        "Human Resources Direction", "IT Systems Direction", "Asset And Liability Management",
        "Property Portfolio",
        
        # Corporate Relations
        "Corporate Relations", "Investor Relations", "Corporate Relationship", 
        "Corporate Alliance and Stake Holder", "Corporate Communications",
        
        # Corporate Services
        "Corporate Services", "Legal Compliance", "Internal Audit", "Security Advisory",
        "Security Assurance", "Continuity Planning",
        
        # Unit Management
        "Unit Management", "Business Unit Direction", "Business Unit Financial Operations",
        "Business Unit Management", "Business Unit Accounting", "Business Unit Financial Analysis",
        
        # Buildings And Equipment
        "Buildings And Equipment", "Fixed Asset Register", "Procurement", 
        "Equipment Administration", "Equipment Maintenance", "Utilities Administration",
        "Site Operations", "Site Administration", "Building Maintenance",
        
        # Human Resources
        "Human Resources", "Recruitment", "Employee Assignment", "Employee Evaluation",
        "Employee Certification", "Employee and Contractor Contract", "Employee Data Management",
        "Employee Payroll And Incentives", "Employee Benefits", "Workforce Training",
        "Travel and Expenses", "Employee Access",
        
        # Platform Operations
        "Platform Operations", "Systems Assurance", "System Deployment", "Systems Operations",
        "Internal Network Operation", "Systems Help Desk", "Platform Operations",
        "Operational Gateway",
        
        # Risk Management
        "Resource Management", "Market Risk", "Credit and Margin Management", "Gap Analysis",
        "Limit and Exposure Management", "Position Management", "Economic Capital",
        
        # Compliance
        "Compliance", "Regulatory And Legal Authority", "Regulatory Compliance",
        "Regulatory Reporting", "Guideline Compliance", "Compliance Reporting",
        
        # Financial Control
        "Financial Control", "Financial Statements", "Company Billing and Payments",
        "Approved Supplier Directory", "Enterprise Tax Administration", "Financial Compliance",
        
        # Credit Risk
        "Credit Risk", "Credit Management", "Counterparty Risk", "Fraud Resolution",
        "Operational Risk", "Business Risk Models", "Operational Risk Models",
        "Production Risk Models",
        
        # Group Treasury
        "Group Treasury", "Corporate Treasury", "Corporate Treasury Analysis",
        "Bank Portfolio Administration", "Bank Portfolio Analysis", "Asset Securitization",
        
        # Finance And Risk Management
        "Finance And Risk Management",
        
        # External Agency
        "External Agency", "Interbank Relationship Management", "Correspondent Bank Relationship",
        "Management", "Syndicate Management", "Product Service Agency", "Product Broker Agreement",
        "Sub Custodian Agreement", "Commission Agreement", "Contractor and Supplier Agreement",
        "Service Provider Operations",
        
        # Operational Services
        "Operational Services", "Customer Billing", "Disbursement", "Open Item Management",
        "Delinquent Account Handling", "Card Collections", "Product Combination",
        "Reward Points Awards And Redemption", "Issued Device Administration",
        "Issued Device Tracking", "Card Transaction Switch", "Internal Bank Account",
        "Term Deposit Framework Agreement",
        
        # Custody, Collateral And Documents
        "Custody, Collateral And Documents", "Account Recovery", "Archive Services",
        "Custody Administration", "Collateral Allocation Management", "Collections",
        "Document Directory", "Investment Account", "Document Services", "Party Asset Directory",
        "Collateral Asset Administration",
        
        # Clearing And Settlement
        "Clearing And Settlement", "Counterparty Administration", "Payment Order",
        "Cheque Processing", "Card Financial Settlement", "Order Allocation",
        "Payment Execution", "Card Clearing", "Transaction Engine", "ACH Operations",
        "Correspondent Bank Directory", "Correspondent Bank Operations", "Card eCommerce Gateway",
        "Payment Instruction", "Payment Rail Operations",
        
        # Accounting Services
        "Accounting Services", "Position Keeping", "Customer Position", "Accounts Receivable",
        "Financial Accounting", "Customer Tax Handling", "Commissions", "Fraud Evaluation",
        "Account Reconciliation", "Securities Position Keeping", "Fraud Diagnosis",
        "Reward Points Account", "Financial Statement Assessment",
        
        # Market Operations
        "Market Operations", "Trading Book Oversight", "Trade Confirmation Matching",
        "Trade and Price Reporting", "Credit Risk Operations", "Securities Fails Processing",
        "Financial Instrument Valuation", "Corporate Action", "Trade Clearing", "Trade Settlement",
        
        # Consumer Banking
        "Consumer Banking", "Current Account", "Brokered Product", "Sales Product",
        "Trust Services", "Payment Initiation", "Currency Exchange", "Advisory Services",
        "Mergers and Acquisitions Advisory", "Corporate Finance", "Corporate Tax Advisory",
        "Consumer Advisory Services", "Legal Advisory",
        
        # Market Trading
        "Market Trading", "Trader Position Operations", "Market Order", "Market Order Execution",
        "Dealer Desk", "Suitability Checking", "Quote Management", "Market Making",
        "Program Trading", "Stock Lending and Repos",
        
        # Corporate Banking
        "Corporate Banking", "Corporate Current Account", "Direct Debit Mandate",
        "Cash Management And Account Services", "Corporate Trust Services", "Credit Facility",
        "Direct Debit", "Cheque Lock Box", "Factoring", "Cash Concentration",
        "Corporate Payroll Services", "Project Finance", "Notional Pooling", "Virtual Account",
        
        # Cards
        "Cards", "Credit Card", "Card Authorization", "Card Transaction Capture",
        "Merchant Relations", "Card Network Participant Facility", "Merchant Acquiring Facility",
        "Credit Card Position Keeping",
        
        # Trade Banking
        "Trade Banking", "Letter of Credit", "Bank Guarantee", "Bank Drafts",
        "Corporate Finance", "ECM And DCM", "Private Placement", "Public Offering",
        "Unit Trust Administration", "Hedge Fund Administration", "Mutual Fund Administration",
        
        # Loans and Deposits
        "Loans and Deposits", "Loan", "Consumer Loan", "Mortgage Loan", "Corporate Loan",
        "Corporate Lease", "Merchandising Loan", "Leasing Item Administration",
        "Syndicated Loan", "Fiduciary Agreement", "Underwriting", "Leasing", "Savings Account",
        "Term Deposit", "Standing Order",
        
        # Products
        "Products",
        
        # Sales
        "Sales", "Customer Campaign Execution", "Product Expert Sales Support", "Product Matching",
        "Customer Offer", "Special Pricing Conditions", "Party Lifecycle Management",
        "Prospect Campaign Execution", "Lead and Opportunity Management", "Product Sales Support",
        
        # Relationship Management
        "Relationship Management", "Customer Relationship Management", "Customer Behavior Insights",
        "Customer Credit Rating", "Customer Agreement", "Sales Product Agreement",
        "Customer Product And Service Eligibility", "Customer Proposition", "Customer Event History",
        "Customer Product and Service Directory", "Loan Syndication", "Customer Financial Insights",
        
        # Customer Care
        "Customer Care", "Servicing Mandate", "Servicing Order", "Customer Case Management",
        "Card Case", "Customer Case",
        
        # Party Reference
        "Party Reference", "Legal Entity Directory", "Location Data Management",
        "Party Reference Data Directory",
        
        # Customers
        "Customers",
        
        # Investment Services
        "Investment Services", "Consumer Investments", "Investment Portfolio Management",
        "Investment Portfolio Analysis", "Investment Portfolio Planning", "eTrading Workbench",
        
        # Information Providers
        "Information Providers", "Public Reference Data Management",
        "Financial Instrument Reference Data Management", "Financial Market Research",
        "Financial Market Analysis", "Market Information Management", "Market Data Switch Operation",
        "Information Provider Operation",
        
        # Cross Channel
        "Cross Channel", "Customer Workbench", "Contact Handler", "Contact Routing",
        "Session Dialogue", "Party Routing Profile", "Transaction Authorization",
        "Customer Access Entitlement", "Channel Activity History", "Processing Order",
        "Party Authentication",
        
        # Channel Specific
        "Channel Specific", "ATM Network Operations", "Branch Location Operations",
        "Advanced Voice Services Operations", "eBranch Operations", "Financial Gateway",
        "Card Terminal Administration", "Card Terminal Operation",
        
        # Distribution
        "Distribution", "Product Inventory Distribution", "Branch Currency Distribution",
        "Correspondence",
        
        # Channels
        "Channels",
        
        # Servicing
        "Servicing", "Contact Center Operations", "Point of Service", "Interactive Help",
        "Servicing Issue", "Servicing Event History", "Service Directory",
        
        # Marketing And Development
        "Marketing And Development", "Business Development", "Market Research", "Market Analysis",
        "Competitor Analysis", "Customer Campaign Management", "Customer Campaign Design",
        "Customer Portfolio", "Advertising", "Promotional Events", "Sales Planning",
        "Contribution Analysis", "Brand Management", "Segment Direction",
        "Prospect Campaign Design", "Customer Surveys", "Prospect Campaign Management",
        
        # Product Management
        "Product Management", "Product Portfolio", "Product Design", "Production Release",
        "Product Deployment", "Product Quality Assurance", "Product Training",
        "Case Root Cause Analysis", "Product Directory", "Discount Pricing",
        
        # Solution Development
        "Solution Development", "IT Standards And Guidelines", "Systems Administration",
        "Development Environment", "System Development",
        
        # Channel Management
        "Channel Management", "Channel Portfolio", "Branch Portfolio", "Contact Center Management",
        "Servicing Activity Analysis", "Financial Message Analysis", "Channel Activity Analysis",
        "Information Provider Administration", "Market Data Switch Administration",
        "Branch Location Management", "ATM Network Management", "Branch Network Management",
        "Advanced Voice Services Management", "eBranch Management", "Product Inventory Item Management",
        "Central Cash Handling", "Branch Currency Management",
        
        # Intellectual Property And Knowledge
        "Intellectual Property And Knowledge", "Intellectual Property Portfolio",
        "Management Manual", "Enterprise Architecture", "Knowledge Exchange",
        
        # Models And Analytics
        "Models And Analytics", "Contribution Models", "Customer Behavior Models",
        "Credit Risk Models", "Fraud Model", "Quant Model", "Trading Models",
        "Financial Instrument Valuation Models", "Liquidity Risk Models", "Market Risk Models",
        
        # Business Development (appears again)
        "Business Development"
    ]
    
    # Define the value chain structure based on the visual layout
    value_chain_structure = {
        "Business Management": [
            "Business Direction", "Organization Direction", "Products and Services Direction", 
            "Corporate Strategy", "Corporate Policies", "Human Resources Direction", 
            "IT Systems Direction", "Asset And Liability Management", "Property Portfolio"
        ],
        "Corporate Relations": [
            "Investor Relations", "Corporate Relationship", "Corporate Alliance and Stake Holder", 
            "Corporate Communications"
        ],
        "Corporate Services": [
            "Legal Compliance", "Internal Audit", "Security Advisory", "Security Assurance", 
            "Continuity Planning"
        ],
        "Unit Management": [
            "Business Unit Direction", "Business Unit Financial Operations", "Business Unit Management",
            "Business Unit Accounting", "Business Unit Financial Analysis"
        ],
        "Buildings And Equipment": [
            "Fixed Asset Register", "Procurement", "Equipment Administration", "Equipment Maintenance",
            "Utilities Administration", "Site Operations", "Site Administration", "Building Maintenance"
        ],
        "Human Resources": [
            "Recruitment", "Employee Assignment", "Employee Evaluation", "Employee Certification",
            "Employee and Contractor Contract", "Employee Data Management", "Employee Payroll And Incentives",
            "Employee Benefits", "Workforce Training", "Travel and Expenses", "Employee Access"
        ],
        "Platform Operations": [
            "Systems Assurance", "System Deployment", "Systems Operations", "Internal Network Operation",
            "Systems Help Desk", "Operational Gateway"
        ],
        "Finance And Risk Management": [
            "Market Risk", "Credit and Margin Management", "Gap Analysis", "Limit and Exposure Management",
            "Position Management", "Economic Capital", "Regulatory And Legal Authority", "Regulatory Compliance",
            "Regulatory Reporting", "Guideline Compliance", "Compliance Reporting", "Financial Control",
            "Financial Statements", "Company Billing and Payments", "Approved Supplier Directory",
            "Enterprise Tax Administration", "Financial Compliance", "Credit Management", "Counterparty Risk",
            "Fraud Resolution", "Business Risk Models", "Operational Risk Models", "Production Risk Models",
            "Corporate Treasury", "Corporate Treasury Analysis", "Bank Portfolio Administration",
            "Bank Portfolio Analysis", "Asset Securitization"
        ],
        "External Agency": [
            "Interbank Relationship Management", "Correspondent Bank Relationship", "Syndicate Management",
            "Product Service Agency", "Product Broker Agreement", "Sub Custodian Agreement",
            "Commission Agreement", "Contractor and Supplier Agreement", "Service Provider Operations"
        ],
        "Operational Services": [
            "Customer Billing", "Disbursement", "Open Item Management", "Delinquent Account Handling",
            "Card Collections", "Product Combination", "Reward Points Awards And Redemption",
            "Issued Device Administration", "Issued Device Tracking", "Card Transaction Switch",
            "Internal Bank Account", "Term Deposit Framework Agreement", "Account Recovery",
            "Archive Services", "Custody Administration", "Collateral Allocation Management",
            "Collections", "Document Directory", "Investment Account", "Document Services",
            "Party Asset Directory", "Collateral Asset Administration", "Counterparty Administration",
            "Payment Order", "Cheque Processing", "Card Financial Settlement", "Order Allocation",
            "Payment Execution", "Card Clearing", "Transaction Engine", "ACH Operations",
            "Correspondent Bank Directory", "Correspondent Bank Operations", "Card eCommerce Gateway",
            "Payment Instruction", "Payment Rail Operations", "Position Keeping", "Customer Position",
            "Accounts Receivable", "Financial Accounting", "Customer Tax Handling", "Commissions",
            "Fraud Evaluation", "Account Reconciliation", "Securities Position Keeping",
            "Fraud Diagnosis", "Reward Points Account", "Financial Statement Assessment",
            "Trading Book Oversight", "Trade Confirmation Matching", "Trade and Price Reporting",
            "Credit Risk Operations", "Securities Fails Processing", "Financial Instrument Valuation",
            "Corporate Action", "Trade Clearing", "Trade Settlement"
        ],
        "Products": [
            "Current Account", "Brokered Product", "Sales Product", "Trust Services", "Payment Initiation",
            "Currency Exchange", "Mergers and Acquisitions Advisory", "Corporate Finance",
            "Corporate Tax Advisory", "Consumer Advisory Services", "Legal Advisory",
            "Trader Position Operations", "Market Order", "Market Order Execution", "Dealer Desk",
            "Suitability Checking", "Quote Management", "Market Making", "Program Trading",
            "Stock Lending and Repos", "Corporate Current Account", "Direct Debit Mandate",
            "Cash Management And Account Services", "Corporate Trust Services", "Credit Facility",
            "Direct Debit", "Cheque Lock Box", "Factoring", "Cash Concentration",
            "Corporate Payroll Services", "Project Finance", "Notional Pooling", "Virtual Account",
            "Credit Card", "Card Authorization", "Card Transaction Capture", "Merchant Relations",
            "Card Network Participant Facility", "Merchant Acquiring Facility", "Credit Card Position Keeping",
            "Letter of Credit", "Bank Guarantee", "Bank Drafts", "ECM And DCM", "Private Placement",
            "Public Offering", "Unit Trust Administration", "Hedge Fund Administration",
            "Mutual Fund Administration", "Loan", "Consumer Loan", "Mortgage Loan", "Corporate Loan",
            "Corporate Lease", "Merchandising Loan", "Leasing Item Administration", "Syndicated Loan",
            "Fiduciary Agreement", "Underwriting", "Leasing", "Savings Account", "Term Deposit",
            "Standing Order", "Consumer Investments", "Investment Portfolio Management",
            "Investment Portfolio Analysis", "Investment Portfolio Planning", "eTrading Workbench"
        ],
        "Customers": [
            "Customer Campaign Execution", "Product Expert Sales Support", "Product Matching",
            "Customer Offer", "Special Pricing Conditions", "Party Lifecycle Management",
            "Prospect Campaign Execution", "Lead and Opportunity Management", "Product Sales Support",
            "Customer Relationship Management", "Customer Behavior Insights", "Customer Credit Rating",
            "Customer Agreement", "Sales Product Agreement", "Customer Product And Service Eligibility",
            "Customer Proposition", "Customer Event History", "Customer Product and Service Directory",
            "Loan Syndication", "Customer Financial Insights", "Servicing Mandate", "Servicing Order",
            "Customer Case Management", "Card Case", "Customer Case", "Legal Entity Directory",
            "Location Data Management", "Party Reference Data Directory"
        ],
        "Information Providers": [
            "Public Reference Data Management", "Financial Instrument Reference Data Management",
            "Financial Market Research", "Financial Market Analysis", "Market Information Management",
            "Market Data Switch Operation", "Information Provider Operation"
        ],
        "Channels": [
            "Customer Workbench", "Contact Handler", "Contact Routing", "Session Dialogue",
            "Party Routing Profile", "Transaction Authorization", "Customer Access Entitlement",
            "Channel Activity History", "Processing Order", "Party Authentication",
            "ATM Network Operations", "Branch Location Operations", "Advanced Voice Services Operations",
            "eBranch Operations", "Financial Gateway", "Card Terminal Administration",
            "Card Terminal Operation", "Product Inventory Distribution", "Branch Currency Distribution",
            "Correspondence", "Contact Center Operations", "Point of Service", "Interactive Help",
            "Servicing Issue", "Servicing Event History", "Service Directory"
        ],
        "Marketing And Development": [
            "Business Development", "Market Research", "Market Analysis", "Competitor Analysis",
            "Customer Campaign Management", "Customer Campaign Design", "Customer Portfolio",
            "Advertising", "Promotional Events", "Sales Planning", "Contribution Analysis",
            "Brand Management", "Segment Direction", "Prospect Campaign Design", "Customer Surveys",
            "Prospect Campaign Management", "Product Portfolio", "Product Design", "Production Release",
            "Product Deployment", "Product Quality Assurance", "Product Training",
            "Case Root Cause Analysis", "Product Directory", "Discount Pricing", "IT Standards And Guidelines",
            "Systems Administration", "Development Environment", "System Development", "Channel Portfolio",
            "Branch Portfolio", "Contact Center Management", "Servicing Activity Analysis",
            "Financial Message Analysis", "Channel Activity Analysis", "Information Provider Administration",
            "Market Data Switch Administration", "Branch Location Management", "ATM Network Management",
            "Branch Network Management", "Advanced Voice Services Management", "eBranch Management",
            "Product Inventory Item Management", "Central Cash Handling", "Branch Currency Management",
            "Intellectual Property Portfolio", "Management Manual", "Enterprise Architecture",
            "Knowledge Exchange", "Contribution Models", "Customer Behavior Models", "Credit Risk Models",
            "Fraud Model", "Quant Model", "Trading Models", "Financial Instrument Valuation Models",
            "Liquidity Risk Models", "Market Risk Models"
        ]
    }
    
    # Create CSV data
    csv_data = []
    
    # Add header categories and their service domains
    for category, service_domains in value_chain_structure.items():
        # Add the category itself
        csv_data.append({
            'Element_Type': 'Value Chain Category',
            'Element_Name': category,
            'Parent_Category': '',
            'Level': 1,
            'Description': f'{category} value chain category'
        })
        
        # Add service domains under this category
        for service_domain in service_domains:
            csv_data.append({
                'Element_Type': 'Service Domain',
                'Element_Name': service_domain,
                'Parent_Category': category,
                'Level': 2,
                'Description': f'Service Domain within {category}'
            })
    
    return csv_data

def main():
    """Main function to create the CSV file"""
    print("Extracting BIAN Service Landscape V13.0 Value Chain View elements...")
    
    elements = parse_value_chain_elements()
    
    # Write to CSV
    csv_filename = 'bian_v13_value_chain_elements.csv'
    
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Element_Type', 'Element_Name', 'Parent_Category', 'Level', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(elements)
    
    print(f"✅ Successfully created {csv_filename}")
    print(f"📊 Total elements extracted: {len(elements)}")
    
    # Print summary
    categories = len([e for e in elements if e['Element_Type'] == 'Value Chain Category'])
    service_domains = len([e for e in elements if e['Element_Type'] == 'Service Domain'])
    
    print(f"   - Value Chain Categories: {categories}")
    print(f"   - Service Domains: {service_domains}")

if __name__ == "__main__":
    main()