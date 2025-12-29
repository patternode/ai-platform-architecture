# Technology (Infrastructure) Foundations Platform TSA - Summary

## Document Information
- **Document**: Technology (Infrastructure) Foundations Platform – Target State
- **Authors**: John Marshall & Hrishi Hiremath
- **Date**: August 2025 Version 0.5
- **Responsible Head of Architecture**: Tanya Boelema
- **Executive Sponsor**: Paul Norman CIO
- **Primary Platform Stakeholder**: GM Approver Nic Olivier, GM Core

## Executive Summary

The Infrastructure Foundations Platform describes BNZ's core hosting platforms, compute, mainframe, storage and data centres/cloud and associated capabilities to provide strong foundations to the bank's engineering, data and application hosting platforms.

## Platform Scope and Context

### Overview
Aligning to the BNZ Platform of Platforms model, this target state provides scope and context for the Infrastructure Foundations, which includes:

- **Core hosting platforms**: compute, mainframe, storage and data centres/cloud
- **Main hosting providers/locations**:
  - Amazon AWS
  - Microsoft Azure
  - BNZ Managed On Premises Infrastructure (NZ and AU)

### Strategic Approach
Current agreed approach is to incrementally build strong foundations in AWS (finish one cloud well), followed by Azure – providing end-to-end capabilities.

## Strategic Intent

The Infrastructure Foundations Platform follows a three-pillar approach:

### 1. Perfect the Basics
- **Well Architected**: Secure, Reliable, Performant, Optimised, Sustainable platform services and operations
- **Reference**: Amazon Well-Architected, Azure Well-Architected frameworks

### 2. Build Strong Foundations
- **Robust foundation capability** across both cloud providers and on premises
- **Out of the box** Discovery, Compliance, Security & Monitoring (CAST, G2G, CHF, BCP)

### 3. Deliver Market Leading Experiences (Capabilities)
- **Market leading platform capabilities** for business leverage
- **Simple, Repeatable, and Complete** (Ready and Compliant) patterns and building blocks (Recipes)

## Current State Analysis

### Platforms at BNZ
BNZ operates across multiple platform layers:
- **Experience Platforms**: Channels, Customer Digital, Colleague Digital, Conversational Banking
- **Customer Serving Platforms**: Customer Management, Product Origination, Account Management, Payments
- **Business Enablement Platforms**: Enterprise Services, Enterprise Data & Analytics
- **Core Technology Platforms**: Infrastructure Foundations, Enterprise Security, Enabling Technologies

### Current Cloud Placement
- **Total Applications**: 369 (SaaS or Cloud)
- **AWS Applications**: 187 (Primary)
- **Azure Applications**: 45 (Primary)
- **AWS Primary Usage**: 142 applications
- **Current Cloud Maturity**: MCT-2 level
- **Target**: MCT-4 for Digital Channels

### Business Maturity Index (BMI)
- **High BMI assets**: Reflected in legacy foundation infrastructure components being modernised
- **Low BMI new assets**: Have transitioned towards target state
- Foundation Platforms links to significant BMI outside of platforms, enabling modernisation

## Current State Challenges

### Key Issues Identified
1. **Compliance**: Asking too much of teams to build, understand and maintain applications and cloud
2. **Skillsets**: Balance needed between full stack teams and those requiring support
3. **Capability Maturity/Hygiene**: Good at building, but need to focus on extracting complete value
4. **RACI**: Ownership and clear RACI holding back capability leverage
5. **Currency**: Maintaining standard platforms, recipes and patterns for currency, security and compliance
6. **FinOps**: Need skillset that understands and can affect cloud cost management
7. **Too many tools**: Inconsistency of Infrastructure as Code/automation tooling

### Strong Positives
1. **Embedded Security Consultants**: Enables fast, informed and agile decision making
2. **Strong Foundations**: Good foundation, clear ownership and roadmaps across platforms
3. **Structure and Skills**: Experienced cloud and platform teams
4. **Collaboration**: Platform, Engineering and Security working towards market leading experiences
5. **FinOps**: Dedicated team for optimised cloud deployments

## Target State Architecture

### Strategic Vision
The target state enables a **resilient, reusable, flexible architecture** that allows BNZ to provide the best customer experience and enable feature growth.

### Cloud Adoption Strategy
- **Primary Cloud**: AWS for differentiating services
- **Secondary Cloud**: Azure for productivity capability and non-differentiating workloads
- **Multi-Cloud Approach**: Committed to multi-cloud but focus on industrialising MCT-2 first
- **Engineering Flavours**: MiniApps, Spring Boot, Data Products, SaaS/COTs, Mainframe

### Target State Overview - Across Providers
The architecture spans:
- **Azure**: SYD 99% Mel 1%
- **AWS**: SYD 100%
- **On Premises NZ**: Trans Tasman connection
- **On Premises AU**: Mel/Syd location

## Technology Strategy Alignment

### Five Strategic Principles
1. **Modernise and Simplify**: Platforms domain produces building blocks for modernisation
2. **Agile and Adaptable**: Technology Foundations platforms meet current and future needs
3. **Platform Mindset**: Technology foundation as enabling platform with strong foundations
4. **Resilient, Secure and Safe**: Secure by Default mantra, embedded security practices
5. **Deeply Digital**: Automation capabilities for agility and industrialisation

## Technical Focus Areas

### 1. Cross Domain Focus Areas
- **Compliant and Mature Components**: Managed Recipes and Patterns – Full Stack
- **Focused Cloud Enablement**: Strong collaboration on build and priorities
- **Pragmatic Priorities**: Opinionated Cloud with realistic service placement

### 2. Industry Leading Kubernetes
- **Cross Cloud K8s capability**: Prioritise cloud adoption
- **Ingress and PCI DSS Ready Clusters**
- **Future capabilities**: OpenShift on Bare Metal, Caching/persistence, AKS Azure 2.0

### 3. Compliance, Reporting & Operational Excellence
- **Build compliance into design and delivery**
- **GIRP/Compliance/Critical Hygiene Framework**
- **Embedded monitoring and reporting standards**

### 4. Deepen Cloud Adoption
- **Leverage Strong Foundations** for Cloud AI and Data Capabilities
- **Finish one Cloud well** - complete AWS Platform Offerings
- **Enable key capabilities**: HSM for Payments, Backup compliance, Education/Guild

### 5. Easier Industrialisation (Recipe Adoption)
- **Consistency of Tooling and Onboarding**
- **Multi-Tenant Platform Capabilities**
- **Default configurations** for security, compliance, backup, log retention

## Current State Infrastructure Components

### Data Centres
**Current State (FY25)**:
- Wellington: Spark datacentre
- Auckland: Orbit Drive (ADC1), East Tamaki (ADC2)
- Melbourne: MEL11 (Deer Park), MEL10 (Deer Park)
- Sydney: Knox (Wantirna South), Eastern Creek

**Future State (>FY26)**:
- Consolidated to fewer locations with enhanced capabilities
- Both mainframe sites in highly available state
- Enhanced Auckland presence for cloud services

### Cloud Services
- **Amazon AWS**: Primary cloud for differentiating services
- **Microsoft Azure**: Secondary cloud for productivity and standard services
- **Google Cloud**: Limited use for specific managed services (BNZ ATM, Experience Analytics)

### Storage and Compute
**Current Storage**:
- HPE Alletra for general workloads
- HPE GreenLake for Files performance tier
- AWS Storage Gateway for cloud-backed storage

**Compute Platforms**:
- VMware (current primary)
- OpenShift containers
- Cloud-native containers (EKS, AKS)
- Mainframe systems

## Roadmap and Investment

### FY24-FY28 Modernisation Timeline
**FY24/FY25**:
- EKS capabilities (Ingress, Wiz, General Purpose clusters)
- Container orchestration improvements
- Network and security foundations

**FY25/FY26**:
- AKS capabilities and Azure 2.0 builds
- VMware replacement options exploration
- NextGen Network implementation

**FY26/FY27**:
- EKS PCI Cluster Certification
- Cloud-first strategy implementation
- Recipe and pattern maturation

**FY28+**:
- Market leading experiences delivery
- Full cloud-native operations
- Legacy system retirement

### Investment Requirements
**Financial Ask** (already in plan for Infrastructure BU Capex):
- **FY26**: $6.5M (depreciation funded)
- **FY27**: $6.5M (depreciation funded)
- **FY28**: $6.5M (depreciation funded)

**Investment Focus**:
1. C7000 & HPE gen9 & 10 decommission
2. Decommission Solaris and RHEV hypervisor
3. HPE blade compute refresh
4. Hypervisor choices (VMware alternatives)

## NAB Alignment

### Shared Strategy Elements
- **Cloud First Strategy**: Both organisations aligned
- **Consistent Cloud Platforms**: AWS and Azure focus
- **Shared Security**: CSAM guardrails and governance
- **Common Standards**: Cloud Adoption Standards and Techniques (CAST)

### Differences
- Component/supplier level variations
- Some tooling and platform implementation differences
- Adaptation of NAB frameworks to BNZ-specific requirements

## Risk Management

### Current State Business Risks
The platform addresses key GRACE risks:

1. **RSK-171 Cyber Compromise Risk**: System component inventory, continuity/DR, system monitoring
2. **RSK-166 Data Loss**: System monitoring, backup and recovery capabilities
3. **RSK-158 IT System Failure**: Component inventory, DR capabilities, monitoring

All risks show **improved risk profile** through platform implementations.

## Carbon and Environmental Considerations

### Data Centre Sustainability
**Auckland**:
- Orbit Drive: 100% certified renewable energy through Mercury (carbon net zero by 2030)
- East Tamaki: Energy efficiency and green technology focus

**Melbourne**:
- MEL11: NABERS 3.5 star rating, 19% renewable energy

**Sydney**:
- 53% renewable energy generation capacity across NSW
- Recommendations favour Auckland for high-energy workloads

### Digital Carbon Footprint
- **2024 Cloud Emissions**: 187.22 tonnes CO2 equivalent
- **Azure**: 40% decrease through cost savings
- **AWS**: 33% increase due to migrations
- **Recommendation**: Prioritise renewable energy regions for high-energy workloads

## Tipping Point Analysis

### Platform Renewal vs Legacy Decay
- **Positive trajectory**: Investment rate outpaces legacy asset decay
- **Focus shift timeline**: Beyond FY28, focus moves from legacy to contemporary systems
- **Success factor**: Continued investment in platforms currency and capability maturation

## Critical Success Factors

### Technology Foundation Enablers
1. **Well Architected Cloud Platforms**: Based on compliant recipes as predominant hosting
2. **Security by Default**: Embedded throughout design and delivery
3. **Operational Excellence**: Monitoring, compliance, and governance built-in
4. **Recipe-Driven Development**: Standardised, reusable patterns and components
5. **Multi-Cloud Capability**: Strategic flexibility across providers

### Key Performance Indicators
- Cloud platform maturity progression (MCT levels)
- Recipe adoption rates across development teams
- Security and compliance automation coverage
- Platform cost optimisation (FinOps metrics)
- Developer experience and time-to-value improvements

## APRA Technology Lifecycle Management

### Regulatory Compliance Requirements
**1.2 A)** BNZ will develop sustainable process and implementation plan for life-cycle management
**1.2 B)** Continue developing technology modernisation roadmaps for target state architectures
**1.2 C)** Provide periodic updates on improvements to life-cycle data and modernisation progress

### Key Deliverables
- Technology modernisation roadmaps by June 30, 2025
- Governance and reporting mechanism for progress monitoring
- Funding model communication for timely milestone delivery

## Conclusion

The Infrastructure Foundations Platform represents BNZ's commitment to building world-class technology foundations that enable business growth, innovation, and customer experience excellence. Through a phased approach focusing on cloud-first strategy, security by default, and operational excellence, the platform will provide the foundation for BNZ's digital transformation journey.

The success of this platform depends on continued investment in people, processes, and technology, with a clear focus on delivering market-leading capabilities while maintaining strong security, compliance, and operational standards.