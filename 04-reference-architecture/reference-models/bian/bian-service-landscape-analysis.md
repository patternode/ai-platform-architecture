# BIAN Service Landscape V13.0 - Hierarchy Extract

---
**Lineage**
- **Document Type**: Analysis Summary
- **Author**: AI Assistant (GitHub Copilot)
- **Created**: October 11, 2025
- **Status**: Active
- **Purpose**: Summary of BIAN Service Landscape V13.0 hierarchy extraction
- **Source**: https://bian.org/servicelandscape-13-0-0/views/view_55812.html
---

## Overview

This document summarizes the extraction of the BIAN (Banking Industry Architecture Network) Service Landscape V13.0 hierarchy from the official BIAN website.

## Extraction Details

- **Source URL**: https://bian.org/servicelandscape-13-0-0/views/view_55812.html
- **Extraction Date**: October 11, 2025
- **Total Elements Extracted**: 370
- **Output File**: `ai-platform/bian-service-landscape-hierarchy.csv`

## Hierarchy Structure

The BIAN Service Landscape follows a three-tier hierarchy:

1. **Business Area** (Top Level) - Major business domains
2. **Business Domain** (Mid Level) - Functional groupings within business areas
3. **Service Domain** (Operational Level) - Specific services and capabilities

## Summary Statistics

| Level | Count |
|-------|-------|
| **Business Areas** | 5 |
| **Business Domains** | 38 |
| **Service Domains** | 327 |
| **Total** | 370 |

## Business Areas

The five primary business areas in BIAN V13.0:

### 1. Sales and Service
**Business Domains (7):**
- Channel Specific
- Cross Channel
- Marketing
- Sales
- Customer Management
- Servicing

**Service Domains**: 68

### 2. Reference Data
**Business Domains (4):**
- Party
- External Agency
- Market Data
- Product Management

**Service Domains**: 30

### 3. Operations and Execution
**Business Domains (12):**
- Product Specific Fulfillment
- Loans and Deposits
- Investment Management
- Trade Banking
- Wholesale Trading
- Cards
- Market Operations
- Corporate Financing and Advisory Services
- Consumer Services
- Cross Product Operations
- Payments
- Account Management
- Operational Services
- Collateral Administration

**Service Domains**: 146

### 4. Risk and Compliance
**Business Domains (4):**
- Bank Portfolio and Treasury
- Business Analysis
- Regulations and Compliance
- Models

**Service Domains**: 48

### 5. Business Support
**Business Domains (11):**
- IT Management
- Non-IT and Non-HR Enterprise Services
- Buildings Equipment and Facilities
- Business Command and Control
- Finance
- Human Resource Management
- Knowledge and Intellectual Property
- Corporate Relations
- Business Direction
- Document Management and Archive

**Service Domains**: 87

## CSV File Structure

The exported CSV contains the following columns:

| Column | Description |
|--------|-------------|
| **Level** | Hierarchy level: "Business Area", "Business Domain", or "Service Domain" |
| **BizzId** | BIAN element ID number |
| **Concept** | BIAN concept type (e.g., "Canvas", "StrategyCapability") |
| **BusinessArea** | Parent business area name |
| **BusinessDomain** | Parent business domain name (empty for Business Areas) |
| **ServiceDomain** | Service domain name (empty for Business Areas and Domains) |
| **Link** | Direct URL to the element's page on bian.org |

## Example Records

### Business Area Example
```csv
"Business Area","55812","Canvas","Sales and Service","","","https://bian.org/servicelandscape-13-0-0/elements/id_55812.html"
```

### Business Domain Example
```csv
"Business Domain","87609","StrategyCapability","Sales and Service","Channel Specific","","https://bian.org/servicelandscape-13-0-0/elements/id_87609.html"
```

### Service Domain Example
```csv
"Service Domain","87611","StrategyCapability","Sales and Service","Channel Specific","Branch Location Management","https://bian.org/servicelandscape-13-0-0/elements/id_87611.html"
```

## Usage Scenarios

This extracted hierarchy can be used for:

1. **Capability Mapping** - Map internal bank capabilities to BIAN standard service domains
2. **Gap Analysis** - Identify missing capabilities compared to BIAN standard
3. **Architecture Planning** - Design enterprise architecture aligned with BIAN
4. **Vendor Evaluation** - Assess vendor solutions against BIAN service domains
5. **Documentation** - Reference BIAN standard domains in architecture documents
6. **AI Agent Grounding** - Provide AI agents with banking domain knowledge

## Parsing Scripts

Two PowerShell scripts were created for this extraction:

1. **parse-bian-hierarchy.ps1** - Initial version
2. **parse-bian-hierarchy-v2.ps1** - Improved version that successfully extracted all elements

Location: `scripts/`

## Links

- **BIAN Official Site**: https://bian.org/
- **Service Landscape V13.0 Matrix View**: https://bian.org/servicelandscape-13-0-0/views/view_55812.html
- **Architecture Overview**: https://bian.org/servicelandscape-13-0-0/views/view_54466.html
- **CSV Export**: `ai-platform/bian-service-landscape-hierarchy.csv`

## Notes

- Each element includes a direct link to its detailed page on bian.org
- The hierarchy is extracted from the SVG matrix view
- All 370 elements maintain their parent-child relationships
- BizzId values are BIAN's internal identifier system
- Most Service Domains are classified as "StrategyCapability" concept

## Version Information

- **BIAN Version**: 13.0
- **View Type**: Matrix View
- **Extraction Method**: PowerShell regex parsing of HTML/SVG content

---

**Last Updated**: October 11, 2025
