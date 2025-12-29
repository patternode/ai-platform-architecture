# AI Platform Roadmap - PowerPoint Presentation Specification

> This document provides detailed specifications for creating a PowerPoint presentation for the AI Platform Roadmap, following BNZ Visual Design Standards

---

## Presentation Metadata

| Attribute | Value |
|-----------|-------|
| **Title** | AI Platform Implementation Roadmap |
| **Subtitle** | Q4 FY25 - Q4 FY26 Strategic Plan |
| **Classification** | Confidential |
| **Status** | Draft |
| **Template** | BNZ Corporate Template |
| **Aspect Ratio** | 16:9 (1920x1080px) |
| **Total Slides** | 18 slides |

---

## Visual Design Standards Reference

**All slides MUST follow**: [05-governance/standards/visual-design/visual-design-standard.md](../05-governance/standards/visual-design/visual-design-standard.md)

**Key Standards**:
- **Primary Colors**: BNZ Navy Blue (#003087), BNZ Orange (#FF6B35), BNZ Light Blue (#50E6FF), BNZ Teal (#00A651)
- **Font**: Calibri throughout
- **Slide Title**: 32-36pt Bold, BNZ Navy Blue
- **Body Text**: 18-20pt Regular, Dark Gray (#333333)
- **Bullet Points**: 16-18pt Regular, Dark Gray

---

## Slide-by-Slide Specification

### Slide 1: Title Slide

**Layout**: Title slide with logo

**Content**:
```
Title: AI Platform Implementation Roadmap
Subtitle: Q4 FY25 - Q4 FY26 Strategic Plan
Footer: CONFIDENTIAL | DRAFT | [Date]
```

**Visual Elements**:
- BNZ logo (top right)
- Title: 44pt Bold, BNZ Navy Blue (#003087)
- Subtitle: 28pt Regular, Dark Gray (#333333)
- Background: White with subtle BNZ Navy Blue accent bar at bottom
- "DRAFT" watermark: BNZ Orange (#FF6B35), rotated 45°, semi-transparent

---

### Slide 2: Executive Summary

**Layout**: Title + 2-column content

**Title**: Executive Summary

**Left Column - Key Facts**:
```
Duration: 14 months (Aug 2025 - Sept 2026)

Capability Domains:
• Agents
• Models
• Knowledge

Supporting Platforms:
• Integration | Security | Data
• Infrastructure | Engineering
```

**Right Column - Strategic Outcomes**:
```
Phase 1: Foundation (Q4-Q1)
✓ Target states defined
✓ Technology decisions made

Phase 2: Production Ready (Q2)
✓ Core platforms operational
✓ Foundation models available

Phase 3: Enterprise Scale (Q3-Q4)
✓ Agents use enterprise data
✓ Custom models integrated
```

**Visual Elements**:
- Use BNZ Navy Blue (#003087) for section headers
- Use BNZ Teal (#00A651) for checkmarks
- Icons for each capability domain (agent, model, knowledge)

---

### Slide 3: Roadmap Overview - Timeline

**Layout**: Title + full-width visual

**Title**: Roadmap at a Glance

**Content**: Timeline visualization

```
Q4 FY25        Q1 FY26         Q2 FY26         Q3 FY26         Q4 FY26
Aug-Sep        Oct-Dec         Jan-Mar         Apr-Jun         Jul-Sep
─────────────────────────────────────────────────────────────────────
PHASE 1: FOUNDATION    |  PHASE 2: PRODUCTION  |  PHASE 3: ENTERPRISE
                       |      READINESS        |      SCALE
```

**Below Timeline - Key Milestones**:
- Q4 FY25: Define target states, make technology decisions
- Q1 FY26: MVP platforms ready
- Q2 FY26: Production ready, architectures endorsed
- Q3 FY26: Enterprise data access, graph RAG deployed
- Q4 FY26: Custom models integrated, full platform operational

**Visual Elements**:
- Use gradient bar from BNZ Navy Blue → BNZ Light Blue → BNZ Teal
- Milestone markers in BNZ Orange (#FF6B35)
- Phase labels in white text on colored background

---

### Slide 4: Roadmap Phases Overview

**Layout**: Title + 3-column comparison

**Title**: Three-Phase Delivery Approach

**Columns** (Equal width):

**Phase 1: Foundation**
```
Timeline: Q4 FY25 - Q1 FY26

Focus:
• Define target states
• Technology decisions
• Workbench deployment
• Governance setup

Key Deliverables:
✓ Agent architecture
✓ Model platform design
✓ Knowledge framework
✓ SageMaker workbench
✓ Technology selections
```

**Phase 2: Production Readiness**
```
Timeline: Q2 FY26

Focus:
• Production hardening
• Foundation models
• Vector RAG deployment
• Integration patterns

Key Deliverables:
✓ AgentCore production
✓ LLMs available
✓ Vector search
✓ API gateways
✓ Security controls
```

**Phase 3: Enterprise Scale**
```
Timeline: Q3-Q4 FY26

Focus:
• Enterprise integration
• Custom models
• Graph RAG
• Scale infrastructure

Key Deliverables:
✓ Enterprise data access
✓ Custom model serving
✓ Graph database
✓ PEGA integration
✓ Full platform ops
```

**Visual Elements**:
- Each column header: BNZ Navy Blue background, white text
- Use BNZ Teal (#00A651) for checkmarks
- Light gray (#F5F5F5) background for each column

---

### Slide 5: Capability Domains Overview

**Layout**: Title + 3-row content

**Title**: Three Core Capability Domains

**Row 1 - Agents** (BNZ Navy Blue accent):
```
🤖 AGENTS
Enable autonomous AI systems that can perform tasks, make decisions, and interact with users

Key Components: AgentCore | Copilot Studio | Agent UI | Orchestration
Timeline: Q4 FY25 → Q4 FY26 (Full roadmap period)
```

**Row 2 - Models** (BNZ Light Blue accent):
```
🧠 MODELS
Manage ML/AI model lifecycle from development through production serving

Key Components: SageMaker | Model Registry | Foundation Models | Custom Models
Timeline: Q4 FY25 → Q4 FY26 (Multiple workstreams)
```

**Row 3 - Knowledge** (BNZ Teal accent):
```
📚 KNOWLEDGE
Data and knowledge management enabling AI to leverage enterprise information

Key Components: Vector DB | Graph DB | Semantic Layer | RAG Patterns
Timeline: Q4 FY25 → Q4 FY26 (Parallel initiatives)
```

**Visual Elements**:
- Large emoji icons on left
- Colored left border for each row (matching accent color)
- Timeline bar on right showing duration

---

### Slide 6: Agents Capability - Detailed Timeline

**Layout**: Title + timeline diagram

**Title**: Agents Capability Roadmap

**Content**: Horizontal timeline with milestones

```
Q4 FY25          Q1 FY26              Q2 FY26              Q3 FY26              Q4 FY26
────────────────────────────────────────────────────────────────────────────────────

Agent            Agents target        AgentCore and        Agents can use       Agents can use
capabilities     state definition     Copilot Studio       enterprise data      custom models
& UI foundation  complete             PRODUCTION READY     & foundation
                                                           models
High/Low code    AgentCore and
direction ⚠      Copilot Studio                           Agents target
                 MVP                                       state endorsed
```

**Legend**:
- ⚠ = Decision point
- 🎯 = Key milestone
- ✓ = Deliverable

**Visual Elements**:
- Main timeline: BNZ Navy Blue (#003087)
- Milestones: BNZ Orange (#FF6B35) diamonds
- Decision points: BNZ Orange triangles
- Completion boxes: BNZ Teal (#00A651)

---

### Slide 7: Models Capability - Detailed Timeline

**Layout**: Title + dual-track timeline

**Title**: Models Capability Roadmap

**Content**: Two parallel workstreams

**Track 1 - Foundation Models**:
```
Q4 FY25          Q1 FY26              Q2 FY26              Q3 FY26              Q4 FY26
────────────────────────────────────────────────────────────────────────────────────
Models target    Models target        Foundation models    R2: Publishing       R3-R4:
state defined    state complete       available (R1)       into BDH             Agent integration
(draft)                                                    (no AI)
```

**Track 2 - BNZ-Specific Models**:
```
Q4 FY25          Q1 FY26              Q2 FY26              Q3 FY26              Q4 FY26
────────────────────────────────────────────────────────────────────────────────────
SageMaker        Uplift for limited   Continued uplift     Uplift for use       Uplift for agent
Workbench        production use /                          outside analytics    integration
(DD&A only)      Scoping for AI                            (e.g., PEGA)         (custom models)
```

**Continuous Activities** (bottom banner):
- Model Serving | Model Hosting | Model Observability

**Visual Elements**:
- Track 1: BNZ Light Blue (#50E6FF) timeline
- Track 2: BNZ Navy Blue (#003087) timeline
- Release markers (R1, R2, R3, R4): BNZ Orange (#FF6B35) badges
- Continuous activities: Dark Gray (#333333) banner at bottom

---

### Slide 8: Knowledge Capability - Detailed Timeline

**Layout**: Title + three-track timeline

**Title**: Knowledge Capability Roadmap

**Content**: Three parallel workstreams

**Track 1 - Semantic & Data Access**:
```
Q4 FY25          Q1 FY26              Q2 FY26              Q3 FY26              Q4 FY26
────────────────────────────────────────────────────────────────────────────────────
Knowledge        Knowledge target     Knowledge target     [Ongoing refinement and
capabilities     state complete       state ENDORSED       implementation]
defined (draft)  (safe data access)
```

**Track 2 - Vector Database**:
```
Q4 FY25          Q1 FY26              Q2 FY26              Q3 FY26              Q4 FY26
────────────────────────────────────────────────────────────────────────────────────
Vector DB        MongoDb              Uplift for vector    [Operational]
confirmation ⚠   implementation       embeddings
                                      Vector RAG
                                      available to agents
```

**Track 3 - Graph Database**:
```
Q4 FY25          Q1 FY26              Q2 FY26              Q3 FY26              Q4 FY26
────────────────────────────────────────────────────────────────────────────────────
Graph DB         Graph Database       Graph/RAG available  [Operational]
direction ⚠      options              to agents
                                      (NeoJ procurement
                                      & deployment)
```

**Visual Elements**:
- Track 1: BNZ Teal (#00A651)
- Track 2: BNZ Light Blue (#50E6FF)
- Track 3: BNZ Navy Blue (#003087)
- Decision points: Orange triangles

---

### Slide 9: Technology Platforms Overview

**Layout**: Title + layered architecture diagram

**Title**: Supporting Technology Platforms

**Content**: Horizontal layers (bottom to top)

```
┌─────────────────────────────────────────────────────────────────────┐
│  AGENTS | MODELS | KNOWLEDGE (Applications)                         │
│  BNZ Light Blue (#50E6FF)                                            │
├─────────────────────────────────────────────────────────────────────┤
│  INTEGRATION PLATFORM                                                │
│  APIs, Gateways, Service Bus | Q1-Q2 FY26                           │
│  BNZ Navy Blue (#003087)                                             │
├─────────────────────────────────────────────────────────────────────┤
│  SECURITY PLATFORM                                                   │
│  Identity, Access, Risk, Controls | Q1-Q4 FY26                      │
│  Dark Gray (#333333)                                                 │
├─────────────────────────────────────────────────────────────────────┤
│  DATA PLATFORM                                                       │
│  Data Sources, Targets, Semantic Management | Q4 FY25-Q4 FY26       │
│  BNZ Teal (#00A651)                                                  │
├─────────────────────────────────────────────────────────────────────┤
│  INFRASTRUCTURE PLATFORM                                             │
│  Compute, Storage, Networking, Observability | Q4 FY25-Q3 FY26      │
│  Medium Gray (#666666)                                               │
├─────────────────────────────────────────────────────────────────────┤
│  ENGINEERING PLATFORM                                                │
│  MLOps, AIOps, CI/CD, Governance | Q1-Q3 FY26                       │
│  Light Gray (#CCCCCC)                                                │
└─────────────────────────────────────────────────────────────────────┘
```

**Visual Elements**:
- Each layer: colored background with white text
- Layer height proportional to complexity
- Timeline indicators on right edge
- Arrows showing dependencies between layers

---

### Slide 10: Key Milestones - Q4 FY25

**Layout**: Title + milestone cards

**Title**: Q4 FY25 Key Milestones (Aug-Sep 2025)

**Content**: 6 milestone cards in 2 rows x 3 columns

**Row 1**:

**Card 1**:
```
🤖 AGENTS
Agent capabilities foundation
• Initial framework
• UI components
Status: Planned
```

**Card 2**:
```
⚠ DECISION
High/Low code direction
• Strategic choice
• Tooling impact
Status: Dependency
```

**Card 3**:
```
🧠 MODELS
SageMaker Workbench
• DD&A deployment
• Model development
Status: Planned
```

**Row 2**:

**Card 4**:
```
📚 KNOWLEDGE
Knowledge capabilities
• Draft architecture
• Framework design
Status: Planned
```

**Card 5**:
```
⚠ DECISION
Vector DB confirmed
• Technology selected
• Architecture designed
Status: Dependency
```

**Card 6**:
```
⚠ DECISION
Graph DB direction
• Evaluation decision
• Use case defined
Status: Dependency
```

**Visual Elements**:
- Cards: Light gray (#F5F5F5) background, 2px border
- Emoji icons at top of each card
- Status badge at bottom (color-coded):
  - Planned: BNZ Teal (#00A651)
  - Dependency: BNZ Orange (#FF6B35)

---

### Slide 11: Key Milestones - Q1 FY26

**Layout**: Title + milestone cards

**Title**: Q1 FY26 Key Milestones (Oct-Dec 2025)

**Content**: 4 milestone cards in 2x2 grid

**Card 1**:
```
🤖 AGENTS
Agents target state defined
• Complete architecture
• Reference patterns
• Governance framework

Status: Planned
```

**Card 2**:
```
🤖 AGENTS
AgentCore & Copilot Studio MVP
• Initial orchestration
• Microsoft integration
• Testing ready

Status: Planned
```

**Card 3**:
```
🧠 MODELS
Models target state defined
• Platform architecture
• Serving patterns
• Integration design

Status: Planned
```

**Card 4**:
```
📚 KNOWLEDGE
Knowledge target state defined
• Safe data leverage
• Semantic framework
• Governance established

Status: Planned
```

**Visual Elements**:
- Larger cards than Q4 slide (more content)
- Same styling as previous milestone slide
- Green status badges (all Planned)

---

### Slide 12: Key Milestones - Q2 FY26

**Layout**: Title + milestone cards

**Title**: Q2 FY26 Key Milestones (Jan-Mar 2026)

**Content**: 5 milestone cards

**Card 1**:
```
🤖 AGENTS - Production Ready
AgentCore Production Deployment
• Production-grade infrastructure
• SLAs defined and met
• Copilot Studio operational

Status: Planned
```

**Card 2**:
```
🤖 AGENTS - Architecture Approved
Agents target state endorsed
• Architecture review board approval
• Governance framework approved
• Standards established

Status: Planned
```

**Card 3**:
```
🧠 MODELS - Foundation Models
LLMs available to agents (R1)
• Foundation model access
• LLM orchestration
• Basic model serving

Status: Planned
```

**Card 4**:
```
📚 KNOWLEDGE - Vector RAG
Vector RAG available to agents
• Vector search operational
• Embedding pipeline
• Agent integration complete

Status: Planned
```

**Card 5**:
```
🏗️ PLATFORMS - Architecture Approved
Technology platform endorsed
• AI platform architecture approved
• Integration patterns defined
• Security controls established

Status: Planned
```

**Visual Elements**:
- 3 cards in top row, 2 in bottom row
- Green status badges
- Icons for each domain

---

### Slide 13: Key Milestones - Q3 FY26

**Layout**: Title + milestone cards

**Title**: Q3 FY26 Key Milestones (Apr-Jun 2026)

**Content**: 4 milestone cards

**Card 1**:
```
🤖 AGENTS - Enterprise Integration
Agents use enterprise data
• Secure data access
• Enterprise integration patterns
• Foundation models operational

Status: Planned
```

**Card 2**:
```
🧠 MODELS - BDH Integration
Models published to BDH (R2)
• Model metadata publishing
• Bank Data Hub integration
• Cross-platform access

Status: Planned
```

**Card 3**:
```
📚 KNOWLEDGE - Graph RAG
Graph/RAG available to agents
• NeoJ deployed
• Graph-based retrieval
• Advanced RAG patterns

Status: Planned
```

**Card 4**:
```
🧠 MODELS - PEGA Integration
PEGA model integration
• Fraud models in workflows
• Cross-platform serving
• Real-time inference

Status: Planned
```

---

### Slide 14: Key Milestones - Q4 FY26

**Layout**: Title + milestone cards

**Title**: Q4 FY26 Key Milestones (Jul-Sep 2026)

**Content**: 3 milestone cards (larger)

**Card 1**:
```
🤖 AGENTS - Custom Models
Agents use custom BNZ models
• Custom model integration
• Agent-to-model APIs
• Full orchestration operational

Key Outcome: Complete agent-model integration

Status: Planned
```

**Card 2**:
```
🧠 MODELS - Agent Platform
Custom models platform (R3/R4)
• Advanced agent integration
• Model versioning
• Performance optimization

Key Outcome: Full model platform operational

Status: Planned
```

**Card 3**:
```
📚 KNOWLEDGE - Platform Maturity
Knowledge platform mature
• Semantic layer complete
• Vector and Graph RAG operational
• Enterprise-wide knowledge access

Key Outcome: Complete knowledge platform

Status: Planned
```

**Visual Elements**:
- 3 large cards with expanded content
- All green status badges
- "Key Outcome" section in each card

---

### Slide 15: Dependencies and Risks

**Layout**: Title + 2-column content

**Title**: Critical Dependencies and Decision Points

**Left Column - Critical Decisions (Q4 FY25)**:

| Decision | Impact | Status |
|----------|--------|--------|
| High/Low code direction | Agent development tooling | ⚠ Required |
| Graph database selection | Knowledge graph architecture | ⚠ Required |
| Vector DB confirmation | Vector RAG implementation | ⚠ Required |

**Key Dependencies**:
```
Foundation → Production → Enterprise Scale

✓ Agent target state → Production deployment
✓ Knowledge platform → Enterprise data access
✓ Foundation models → LLM capabilities
✓ Model platform → Custom model integration
```

**Right Column - Risk Matrix**:

**HIGH IMPACT**:
- Technology decision delays
- Architecture approval delays
- Resource constraints

**MEDIUM IMPACT**:
- Integration complexity
- Vendor delivery delays
- Skill gaps

**Mitigation Strategies**:
✓ Early decision forcing functions
✓ Architecture review checkpoints
✓ Vendor engagement and contracts
✓ Training and enablement programs

**Visual Elements**:
- Warning triangles (BNZ Orange) for decisions
- Checkmarks (BNZ Teal) for dependencies
- Risk matrix: 2x2 grid with color coding
  - High: Red (#CC0000)
  - Medium: Orange (#FFA500)
  - Low: Green (#00A651)

---

### Slide 16: Success Metrics and KPIs

**Layout**: Title + 3-column metrics

**Title**: Success Metrics by Phase

**Column 1 - Phase 1 (Foundation)**:
```
TARGET COMPLETION: Q1 FY26

Key Metrics:
✓ All target states documented
✓ 3 critical decisions made
✓ SageMaker workbench operational
✓ Governance framework established

Success Criteria:
• 100% architecture documentation
• 3/3 technology decisions
• MVP platforms deployed
• Governance processes approved
```

**Column 2 - Phase 2 (Production Ready)**:
```
TARGET COMPLETION: Q2 FY26

Key Metrics:
✓ AgentCore production SLA: 99.5%
✓ Foundation models accessible
✓ Vector RAG operational
✓ Architecture endorsed

Success Criteria:
• Production SLAs met
• Security controls approved
• Integration patterns defined
• Board approval received
```

**Column 3 - Phase 3 (Enterprise Scale)**:
```
TARGET COMPLETION: Q4 FY26

Key Metrics:
✓ Agents accessing enterprise data
✓ Custom models integrated
✓ Graph RAG operational
✓ Full platform operational

Success Criteria:
• 10+ agents in production
• 20+ models deployed
• Enterprise-wide adoption
• Operational excellence
```

**Visual Elements**:
- Each column header: colored background matching phase
- Checkmarks in BNZ Teal
- Metrics boxes with light gray background
- Target completion in BNZ Orange

---

### Slide 17: Next Steps and Actions

**Layout**: Title + action items table

**Title**: Immediate Next Steps (Q4 FY25)

**Content**: Action items table

| Action | Owner | Due Date | Status |
|--------|-------|----------|--------|
| **Critical Decisions** | | | |
| Finalize high/low code direction | Architecture Team | Sep 2025 | 🔴 Not Started |
| Confirm vector database selection | Architecture Team | Sep 2025 | 🟡 In Progress |
| Decide graph database direction | Architecture Team | Sep 2025 | 🔴 Not Started |
| **Architecture Artifacts** | | | |
| Document agents target state | Platform Architects | Oct 2025 | 🔴 Not Started |
| Document models target state | ML Architects | Oct 2025 | 🔴 Not Started |
| Document knowledge target state | Data Architects | Oct 2025 | 🔴 Not Started |
| **Platform Deployment** | | | |
| Deploy SageMaker workbench | Engineering Team | Sep 2025 | 🟡 In Progress |
| Setup AgentCore dev environment | Platform Team | Oct 2025 | 🔴 Not Started |
| Configure MongoDB vector search | Data Team | Oct 2025 | 🔴 Not Started |
| **Governance** | | | |
| Establish ADR process | Architecture Team | Aug 2025 | 🟢 Complete |
| Create governance framework | Governance Team | Sep 2025 | 🟡 In Progress |

**Legend**:
- 🟢 Complete
- 🟡 In Progress
- 🔴 Not Started

**Visual Elements**:
- Table with BNZ Navy Blue header row (white text)
- Alternating row colors: white and light gray (#F5F5F5)
- Status indicators: colored circles
- Bold section headers in table

---

### Slide 18: Questions & Discussion

**Layout**: Title + contact information

**Title**: Questions & Discussion

**Content**:

**Key Discussion Points**:
```
1. Technology decision timeline and process
2. Resource allocation and team capacity
3. Dependency management and risk mitigation
4. Governance and approval processes
5. Quarterly planning and milestone tracking
```

**Contact Information**:
```
For questions or additional information:

BNZ Strategy & Architecture Team
📧 architecture@bnz.co.nz

Related Documentation:
📄 AI Platform Architecture Repository
📄 Capability Model
📄 Governance Framework
📄 Work Taxonomy Guide
```

**Footer**:
```
CONFIDENTIAL | DRAFT | Next Review: Q2 FY26 (QPS Planning)
```

**Visual Elements**:
- Large icons for discussion points
- Contact info in centered box with BNZ Navy Blue border
- Footer in small text, light gray

---

## Appendix Slides (Optional)

### Appendix A: Glossary

**Layout**: Title + 2-column table

**Title**: Glossary of Terms

| Term | Definition |
|------|------------|
| **ABB** | Architecture Building Block - Logical, vendor-agnostic component |
| **ADR** | Architecture Decision Record - Documented architectural decision |
| **AgentCore** | BNZ's agent orchestration platform |
| **BDH** | Bank Data Hub - BNZ's central data platform |
| **Copilot Studio** | Microsoft's agent development platform |
| **DD&A** | Data, Digital & Analytics team |
| **LLM** | Large Language Model |
| **MLOps** | Machine Learning Operations |
| **NeoJ** | Graph database technology |
| **PEGA** | BNZ's workflow and decisioning platform |
| **RAG** | Retrieval-Augmented Generation |
| **SageMaker** | AWS machine learning platform |
| **SBB** | Solution Building Block - Specific technology implementation |

---

### Appendix B: Related Documentation

**Layout**: Title + document links

**Title**: Related Documentation and Resources

**Architecture Repository**:
- AI Platform Architecture README
- Capability Model
- Building Blocks (ABBs and SBBs)
- Governance and Standards
- Visual Design Standards

**Roadmap Artifacts**:
- Theme Documents (Foundation, Production, Enterprise Scale)
- Epic Definitions (to be created)
- Feature Breakdowns (to be created)
- Spike Research Plans (to be created)

**Governance**:
- Architecture Decision Records (ADRs)
- Technology Radar
- Standards and Compliance Documentation

---

## Presentation Notes for Each Slide

### General Presentation Guidelines

**Delivery Approach**:
1. Start with executive summary (Slide 2) for leadership audiences
2. Deep-dive into capability domains (Slides 6-8) for technical audiences
3. Focus on milestones (Slides 10-14) for status reporting
4. Emphasize dependencies and risks (Slide 15) for planning discussions

**Customization for Audience**:
- **Executive Leadership**: Slides 1-4, 15-17 (high-level strategy and risks)
- **Architecture Review Board**: Slides 1-5, 6-8, 15-17 (complete technical view)
- **Delivery Teams**: Slides 5-8, 10-14, 17 (detailed milestones and actions)
- **Status Reporting**: Slides 2, 10-14, 17 (progress and next steps)

---

## How to Create the PowerPoint

### Step 1: Setup
1. Open PowerPoint
2. Set slide size to 16:9 (Design → Slide Size → Widescreen)
3. Apply BNZ corporate template (if available)

### Step 2: Create Master Slides
1. Go to View → Slide Master
2. Set up color theme with BNZ colors:
   - Accent 1: #003087 (Navy Blue)
   - Accent 2: #FF6B35 (Orange)
   - Accent 3: #50E6FF (Light Blue)
   - Accent 4: #00A651 (Teal)
3. Set default font to Calibri
4. Create text styles:
   - Title: 32-36pt Bold
   - Body: 18-20pt Regular
   - Caption: 12-14pt Regular

### Step 3: Create Slides
1. Follow each slide specification above
2. Use shapes and SmartArt for diagrams
3. Apply consistent spacing and alignment
4. Add transitions (subtle, professional - e.g., Fade)

### Step 4: Review
1. Check all text is readable (minimum 16pt)
2. Verify color contrast (WCAG AA compliance)
3. Test presentation in presentation mode
4. Proofread all content

---

## Version Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2025-12-03 | Claude Code | Initial presentation specification |

**Status**: Draft Specification
**Next Step**: Create PowerPoint file following this specification
