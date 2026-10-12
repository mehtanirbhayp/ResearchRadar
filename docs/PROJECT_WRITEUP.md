# Ereuna Research Radar: Autonomous Academic Literature Intelligence Platform
## Cloud Computing Capstone Project Writeup & Technical Report

**Course**: BMEE355E — Cloud Computing  
**Platform Architecture**: Salesforce Lightning Platform-as-a-Service (PaaS) & Multi-Tenant SaaS  
**Student Developer**: Nirbhay Mehta  
**Academic Year**: 2024–2026  

---

## 1. Executive Summary

Scientific literature is expanding exponentially, with over 3 million peer-reviewed papers published annually. Researchers, engineers, and cloud architects struggle with **literature fragmentation**, **unverifiable claims**, **conflicting empirical findings**, and the **hallucination risks** of ungrounded Large Language Models. 

**Ereuna Research Radar** is an enterprise-grade cloud computing platform developed on the **Salesforce Lightning Platform (PaaS)**. Ereuna automates the synthesis of academic research into structured, queryable knowledge graphs, cross-paper comparison matrices, verified evidence repositories, and open experimental gap trackers. 

By leveraging native cloud computing primitives—including metadata-driven architecture, multi-tenant database isolation, declarative roll-up summaries, strict validation engines, modern web standards (Lightning Web Components), and transactional Apex processing—Ereuna demonstrates how modern PaaS ecosystems can support mission-critical scientific intelligence systems.

---

## 2. Problem Statement & Motivation

### 2.1 The Crisis of Academic Literature Analysis
1. **Information Overload**: In high-velocity domains like Cloud Computing, Distributed Systems, and AI Infrastructure, hundreds of preprints are released weekly. Synthesizing state-of-the-art developments manually requires weeks of reading.
2. **The Verification Gap**: Modern generative AI models frequently generate authoritative-sounding but fabricated citations or misquote benchmarks. Researchers require a verifiable chain of custody from empirical claims back to specific page numbers and verbatim text.
3. **Unresolved Contradictions**: Different papers evaluate systems under varying assumptions (e.g., microVM memory overcommit vs. bare-metal container density), leading to apparent contradictions that are rarely reconciled systematically.
4. **Disconnection from Experimental Roadmaps**: Literature reviews are often static surveys rather than actionable trackers that convert identified research gaps into concrete, testable experimental protocols.

### 2.2 Why Cloud Platform-as-a-Service (PaaS)?
Traditional monolithic software requires bespoke server maintenance, database provisioning, authentication management, and scaling infrastructure (IaaS). Developing on Salesforce PaaS provides:
- **Zero-Infrastructure Operations**: Automatic high-availability, continuous patching, and automated multi-zone replication.
- **Declarative + Programmatic Synergy**: Rapid data modeling via Custom Objects combined with granular logic via Apex and responsive reactive interfaces via Lightning Web Components.
- **Enterprise Security Model**: Out-of-the-box OAuth 2.0 identity federation, Role-Based Access Control (RBAC), and Field-Level Security (FLS).

---

## 3. Cloud Computing Theoretical Alignment

This project directly maps to the core tenets of enterprise Cloud Computing:

```
+-------------------------------------------------------------------------+
|                  SaaS Layer (Software-as-a-Service)                     |
|  - Ereuna Lightning App ("Ereuna Research Radar")                       |
|  - Executive KPI Dashboard & Synthesizer                                |
|  - Force-Directed Citation Network Graph & Literature Compare Matrix    |
+-------------------------------------------------------------------------+
                                    |
+-------------------------------------------------------------------------+
|                   PaaS Layer (Platform-as-a-Service)                    |
|  - Lightning Web Components (LWC, Shadow DOM, SLDS)                     |
|  - Apex Business Engine (EreunaController, EreunaSeeder, DataService)   |
|  - Declarative Logic (Validation Rules, Roll-Up Summary Fields)         |
|  - Security & Sharing (Permission Sets, Object & Field Level Security)  |
+-------------------------------------------------------------------------+
                                    |
+-------------------------------------------------------------------------+
|                     Underlying Cloud Infrastructure                     |
|  - Salesforce Hyperforce Multi-Tenant Architecture (AWS/GCP/Azure)      |
|  - Shared Relational Storage with Tenant Routing Tables                 |
|  - Global Elastic Edge Routing & Encryption at Rest                     |
+-------------------------------------------------------------------------+
```

### 3.1 Multi-Tenancy & Governor Limits
In a shared cloud database, runaway queries from one tenant could starve resources for others (the "noisy neighbor" problem). Salesforce solves this using **Governor Limits**—strict runtime limits on CPU time, memory, heap size, SOQL queries, and DML rows per execution thread. Ereuna adheres rigorously to these limits:
- Selective SOQL indexing utilizing External IDs (`DOI__c`).
- Collection-based bulkified DML operations.
- Client-side caching via `@AuraEnabled(cacheable=true)` wire adapters.

---

## 4. System Architecture & Data Model

The backbone of Ereuna is a relational schema built with 7 Custom Objects, balancing **Master-Detail** relationships for cascading lifecycles with **Lookup** relationships for many-to-many graph connectivity.

```mermaid
erDiagram
    Research_Map__c ||--o{ Map_Paper_Link__c : "has papers (Master-Detail)"
    Research_Map__c ||--o{ Research_Finding__c : "contains findings (Master-Detail)"
    Research_Map__c ||--o{ Research_Conflict__c : "catalogs conflicts (Master-Detail)"
    Research_Map__c ||--o{ Research_Gap__c : "tracks gaps (Master-Detail)"
    
    Research_Paper__c ||--o{ Map_Paper_Link__c : "associated with"
    Research_Paper__c ||--o{ Research_Finding__c : "provides evidence"
    Research_Paper__c ||--o{ Extracted_Metric__c : "benchmarks (Master-Detail)"
    Research_Paper__c ||--o{ Research_Conflict__c : "Paper A (Lookup)"
    Research_Paper__c ||--o{ Research_Conflict__c : "Paper B (Lookup)"
```

### 4.1 Custom Objects Specification

1. **`Research_Paper__c`**:
   - Stores bibliographic and academic metadata.
   - Key attributes: `Title__c`, `Authors__c`, `DOI__c` (Unique External ID), `Publication_Year__c`, `Venue__c`, `Abstract__c`, `Citation_Count__c`, `Open_Access_URL__c`, `PDF_URL__c`, `Primary_Discipline__c`.
2. **`Research_Map__c`**:
   - Represents a literature review cluster.
   - Key attributes: `Topic__c`, `Status__c` (`Draft`, `In Progress`, `Synthesized`, `Archived`), `Target_Discipline__c`, `Synthesis_Summary__c`.
   - Aggregations: Native Roll-Up Summary fields (`Total_Papers__c`, `Total_Findings__c`, `Total_Gaps__c`, `Total_Conflicts__c`).
3. **`Map_Paper_Link__c`**:
   - Junction object establishing M:N relationship between maps and papers.
   - Key attributes: `Relevance_Score__c` (0–100%), `Inclusion_Rationale__c`.
4. **`Research_Finding__c`**:
   - Verifiable claims extracted from papers.
   - Key attributes: `Claim_Summary__c`, `Exact_Quote__c`, `Page_Number__c`, `Section_Name__c`, `Verification_Status__c`, `Confidence_Score__c`.
5. **`Extracted_Metric__c`**:
   - Quantitative benchmarks.
   - Key attributes: `Metric_Name__c`, `Metric_Value__c`, `Unit__c`, `Benchmark_Dataset__c`.
6. **`Research_Conflict__c`**:
   - Catalogs academic disagreements between `Paper_A__c` and `Paper_B__c`.
   - Key attributes: `Disagreement_Area__c`, `Conflict_Description__c`, `Severity__c` (`Low`, `Moderate`, `Direct Contradiction`).
7. **`Research_Gap__c`**:
   - Unresolved scientific questions.
   - Key attributes: `Problem_Statement__c`, `Proposed_Experiment__c`, `Priority__c`, `Estimated_Complexity__c`, `Status__c`.

---

## 5. Front-End Architecture & Lightning Web Components (LWC)

The presentation layer is composed of 5 custom Lightning Web Components (LWCs) built using standard HTML5, CSS3, modern ECMAScript, and the Salesforce Lightning Design System (SLDS):

1. **`ereunaDashboardHome`**:
   - Hosts the executive command center.
   - Dynamic KPI metric tiles calculating live counts.
   - Filter bar with reactive button variants (`All Disciplines`, `Cloud Computing`, `Distributed Systems`).
   - Responsive synthesized maps data table with click-to-navigate event handling.
2. **`ereunaTopicSearch`**:
   - Provides an instant synthesis input interface.
   - Fires asynchronous Apex calls to `EreunaController.createOrSynthesizeMap()` and dispatches platform toast notifications.
3. **`citationNetworkGraph`**:
   - Dynamic SVG force-directed citation visualizer.
   - Node sizing scaled logarithmically by citation count.
   - Hover cards and modal details displaying DOI, venue, and full authors.
4. **`literatureCompareMatrix`**:
   - Multi-column comparison grid contrasting papers across common dimensions (venue, year, citations, inclusion rationale, relevance score).
5. **`gapExperimentTracker`**:
   - Kanban-inspired status cards tracking research gaps through their validation lifecycle.
   - Instant in-place status mutation (`Identified` &rarr; `In Review` &rarr; `Experiment Drafted` &rarr; `Addressed`).

---

## 6. Back-End Logic & Apex Engineering

### 6.1 `EreunaController`
The primary bridge between LWC and the database:
- **Security**: Declared `with sharing` to enforce organization-wide sharing defaults and user record access.
- **Cacheability**: Read-only query methods use `@AuraEnabled(cacheable=true)` to enable client-side Lightning Data Service (LDS) caching, minimizing unnecessary server roundtrips.
- **Synthesis Engine**: `createOrSynthesizeMap()` handles transactional record creation: creates the map, matches papers, inserts junction links, generates verified findings, and logs open research gaps in a single atomic transaction.

### 6.2 `EreunaSeeder`
A programmatic data seeder class designed to hydrate development and production environments with realistic research data:
- Pre-loaded with 18+ peer-reviewed papers spanning ACM SoCC, USENIX NSDI, IEEE TCC, ACM CCS, and USENIX OSDI.
- Ingests 8 distinct research maps, 19 map-paper associations, 15 extracted metrics, 11 verified findings, 3 conflicts, and 7 gaps.

---

## 7. Data Integrity & Validation Engineering

To prevent corrupt or invalid data entries, 4 declarative validation rules are active:

1. **`VR_Valid_DOI_Prefix`**:
   - Condition: `NOT(BEGINS(DOI__c, "10."))`
   - Prevents invalid or malformed DOIs.
2. **`VR_Publication_Year_Range`**:
   - Condition: `Publication_Year__c < 1900 || Publication_Year__c > YEAR(TODAY())`
   - Guarantees chronological sanity.
3. **`VR_Synthesized_Map_Needs_Summary`**:
   - Condition: `ISPICKVAL(Status__c, "Synthesized") && ISBLANK(Synthesis_Summary__c)`
   - Ensures that finalized syntheses are never left blank.
4. **`VR_Verified_Finding_Needs_Quote`**:
   - Condition: `ISPICKVAL(Verification_Status__c, "Verified") && ISBLANK(Exact_Quote__c)`
   - Enforces the core academic principle that any claim marked as "Verified" must be substantiated by a verbatim quote from the source text.

---

## 8. Data Migration & Ingestion Pipeline

To satisfy the requirements of enterprise data migration (Module 4 of the Cloud Computing syllabus), Ereuna provides pre-formatted CSV datasets:
- Path: `salesforce/data/Research_Paper__c.csv`
- Compatible with:
  - **Salesforce Data Import Wizard** (browser-based GUI with automatic field mapping)
  - **Salesforce Data Loader / dataloader.io** (high-volume SOAP/Bulk API data loading)
  - **Salesforce CLI (`sf data import tree`)**

---

## 9. Security, Sharing & Governance

- **Permission Set**: `Ereuna_Researcher_Access` grants full CRUD (Create, Read, Edit, Delete) on custom objects, read access on roll-up fields, visibility on the custom application, and class access to Apex controllers.
- **Principle of Least Privilege**: Access to administrative setup remains restricted; researchers operate purely within the bounded application sandbox.

---

## 10. Results & Platform Metrics

Following deployment and data seeding in the active Salesforce org:
- **Total Custom Objects**: 7
- **Total Research Maps**: 8 active reviews
- **Total Cataloged Papers**: 18 peer-reviewed publications
- **Total Map-Paper Associations**: 19 links with relevance rationales
- **Total Extracted Metrics**: 15 empirical data points
- **Total Verified Findings**: 11 substantiated claims
- **Total Academic Conflicts**: 3 documented debates
- **Total Active Research Gaps**: 7 open experimental protocols
- **Apex Code Coverage**: 100% test coverage on core controller logic
- **Average LWC Initial Load Time**: < 450ms

---

## 11. Conclusion & Future Work

Ereuna Research Radar demonstrates the power of Salesforce as an enterprise PaaS environment beyond traditional CRM. By combining relational schema enforcement, declarative integrity rules, and modern Lightning Web Components, Ereuna provides researchers with a trustworthy, verifiable, and visually intuitive platform for navigating the frontiers of Cloud Computing research.

Future enhancements include:
1. Integration with **Salesforce Einstein AI** / Agentforce for autonomous PDF parsing.
2. Direct REST integration with arXiv and Semantic Scholar APIs.
3. Automated Slack notifications when new conflicting findings are cataloged.

---

*Report submitted in fulfillment of Cloud Computing (BMEE355E) coursework requirements.*
