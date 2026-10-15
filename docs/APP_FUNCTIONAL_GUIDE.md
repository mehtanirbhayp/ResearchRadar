# Ereuna Research Radar: Complete Functional Guide & User Manual

Welcome to **Ereuna Research Radar**, an autonomous Cloud Computing & Academic Literature Intelligence Platform built natively on the Salesforce Lightning PaaS (Platform-as-a-Service) architecture.

This manual provides an exhaustive, step-by-step reference for **every single function, feature, custom object, Lightning Web Component (LWC), Apex service, and user workflow** in the application.

---

## Table of Contents
1. [Quick Start & Accessing the App](#1-quick-start--accessing-the-app)
2. [Executive Dashboard (`Radar Dashboard` Tab)](#2-executive-dashboard-radar-dashboard-tab)
3. [Research Maps Management (`Research Maps` Tab)](#3-research-maps-management-research-maps-tab)
4. [Research Papers Catalog (`Research Papers` Tab)](#4-research-papers-catalog-research-papers-tab)
5. [Evidence & Findings Engine (`Research Findings` Tab)](#5-evidence--findings-engine-research-findings-tab)
6. [Open Questions & Experiment Tracker (`Research Gaps` Tab)](#6-open-questions--experiment-tracker-research-gaps-tab)
7. [Conflict & Debate Resolution (`Research Conflicts` Tab)](#7-conflict--debate-resolution-research-conflicts-tab)
8. [Lightning Web Components (LWC) Deep Dive](#8-lightning-web-components-lwc-deep-dive)
9. [Apex Controllers & Data Services Reference](#9-apex-controllers--data-services-reference)
10. [Data Ingestion & Migration (Data Loader & Import Wizard)](#10-data-ingestion--migration-data-loader--import-wizard)
11. [Validation Rules & Data Integrity Controls](#11-validation-rules--data-integrity-controls)

---

## 1. Quick Start & Accessing the App

### Step 1: Open the App Launcher
1. Log in to your Salesforce Developer or Trailhead Org.
2. In the top-left corner of the Salesforce navigation bar, click the **App Launcher** (the 3x3 grid icon).
3. In the search box, type **`Ereuna`**.
4. Click on **`Ereuna Research Radar`**.

### Step 2: Verifying Your Navigation Tabs
Once opened, you will see the unified navigation bar featuring dedicated, 100% interactive Lightning Web Component experiences — zero plain tables:
- **Radar Dashboard**: Executive KPI command center & topic synthesizer (`Ereuna_Home`).
- **Research Maps**: Visual card hub for synthesized literature clusters with status badges, roll-up metrics, 1-click **Launch Workspace**, and **+ Synthesize New Topic** modal (`Research_Map_Hub`).
- **Research Papers**: Visual academic publication card catalog with fire citation badges (`🔥 485 Citations`), extracted benchmark metric pills, abstract accordions, and 1-click PDF / DOI / BibTeX modal (`Paper_Explorer`).
- **Research Gaps**: Interactive 4-stage Kanban board tracking research gaps through validation stages with live stage moves and "+ Propose New Experiment" modal (`Gap_Board`).
- **Research Findings**: Empirical evidence cards featuring verbatim literature quotations, confidence percentage badges, and source publication page/section citations (`Findings_Explorer`).
- **Reports & Dashboards**: Standard Salesforce operational analytics and custom report builders.

---

## 2. Executive Dashboard (`Radar Dashboard` Tab)

The **Radar Dashboard** (`Ereuna_Home`) is the default landing page. It provides real-time situational awareness across the entire academic knowledge base.

### 2.1 Live KPI Summary Cards
At the top of the dashboard are four dynamic KPI metric cards:
1. **Research Maps**: Displays the total count of synthesized research reviews (e.g., `8`).
2. **Cataloged Papers**: Displays the number of peer-reviewed papers indexed in the system (e.g., `18`).
3. **Verified Findings**: Displays the number of empirical claims verified with exact page quotes (e.g., `11`).
4. **Active Gaps**: Displays identified open research problems awaiting experimental validation (e.g., `7`).

### 2.2 Instant Topic Search & Automated Synthesizer
Directly below the KPIs is the **Ereuna Topic Synthesizer**:
- **Search Bar**: Type any topic keyword (e.g., `Serverless Cold Start`, `eBPF Service Mesh`, `Carbon-Aware Datacenters`, `Confidential Computing`).
- **Discipline Selector**: Choose the target research discipline (`Cloud Computing`, `Distributed Systems`, `Artificial Intelligence`, `Computer Science`).
- **"Synthesize Map" Button**:
  - Automatically queries related papers in the repository.
  - Automatically computes relevance scores and builds `Map_Paper_Link__c` records.
  - Automatically generates an executive `Synthesis_Summary__c`.
  - Automatically extracts key findings and identifies research gaps.
  - Instantly refreshes the dashboard with the newly created map.

### 2.3 Discipline Filtering Bar
Filter recent research syntheses by discipline with a single click:
- **All Disciplines**: Shows all active research maps.
- **Cloud Computing**: Shows maps focusing on serverless, Kubernetes, virtualization, FinOps, and green cloud.
- **Distributed Systems**: Shows maps focusing on edge computing, CXL disaggregated memory, and Borg orchestration.

### 2.4 Interactive Syntheses Table
Clicking any row in the recent syntheses table navigates directly to that Research Map record view.

---

## 3. Research Maps Management (`Research Maps` Tab)

A **Research Map** (`Research_Map__c`) represents a high-level literature review cluster around a core research question.

### Key Fields:
- **Map Name (`Name`)**: Auto-generated identifier (e.g., `MAP-0001`).
- **Research Topic (`Topic__c`)**: The title of the research synthesis (e.g., *Serverless Elasticity and Cold-Start Mitigation in Multi-Cloud Systems*).
- **Target Discipline (`Target_Discipline__c`)**: Picklist value (`Cloud Computing`, `Distributed Systems`, `Artificial Intelligence`, `Computer Science`, `Biomedicine`).
- **Status (`Status__c`)**: Picklist tracking lifecycle:
  - `Draft`: Initial topic formulation.
  - `In Progress`: Active paper aggregation and metric extraction.
  - `Synthesized`: Fully reviewed and validated.
  - `Archived`: Superseded by newer syntheses.
- **Synthesis Summary (`Synthesis_Summary__c`)**: Rich text/text area providing the consensus summary of literature findings.
- **Automated Roll-Up Summaries**:
  - `Total_Papers__c`: Number of linked papers.
  - `Total_Findings__c`: Number of verified claims.
  - `Total_Gaps__c`: Number of identified research gaps.
  - `Total_Conflicts__c`: Number of detected contradictions.

### How to Create a Research Map Manually:
1. Navigate to the **Research Maps** tab.
2. Click **New**.
3. Fill in **Research Topic**, select **Target Discipline**, and set **Status** to `Draft` or `Synthesized`.
4. If setting Status to `Synthesized`, provide a **Synthesis Summary** (enforced by validation rule `VR_Synthesized_Map_Needs_Summary`).
5. Click **Save**.

---

## 4. Research Papers Catalog (`Research Papers` Tab)

The **Research Paper** (`Research_Paper__c`) object stores individual academic literature items.

### Key Fields:
- **Title (`Title__c`)**: Full publication title.
- **Authors (`Authors__c`)**: Comma-separated list of authors.
- **DOI (`DOI__c`)**: Digital Object Identifier (Must begin with `10.`, enforced by `VR_Valid_DOI_Prefix`).
- **Publication Year (`Publication_Year__c`)**: Must be between 1900 and the current year (enforced by `VR_Publication_Year_Range`).
- **Venue (`Venue__c`)**: Conference or journal name (e.g., *ACM SoCC*, *USENIX NSDI*, *IEEE TCC*).
- **Abstract (`Abstract__c`)**: Full academic abstract.
- **Citation Count (`Citation_Count__c`)**: Integer citation metrics.
- **Open Access URL (`Open_Access_URL__c`)**: Direct URL to repository page (e.g., arXiv, USENIX).
- **PDF URL (`PDF_URL__c`)**: Direct link to the open access PDF document.
- **Primary Discipline (`Primary_Discipline__c`)**: Academic discipline.

### How to Add a New Paper:
1. Navigate to the **Research Papers** tab.
2. Click **New**.
3. Enter paper details. Ensure the **DOI** begins with `10.` and **Publication Year** is valid.
4. Click **Save**.

---

## 5. Evidence & Findings Engine (`Research Findings` Tab)

The **Research Finding** (`Research_Finding__c`) object holds specific empirical claims extracted from papers.

### Key Fields:
- **Claim Summary (`Claim_Summary__c`)**: Concise description of the claim (e.g., *Memory pre-warming cuts P99 cold-start latency from 580ms to 184ms*).
- **Exact Quote (`Exact_Quote__c`)**: Verbatim quote from the paper text. *(Mandatory if Verification Status is "Verified", enforced by `VR_Verified_Finding_Needs_Quote`)*.
- **Page Number (`Page_Number__c`)**: The exact publication page where the quote appears.
- **Section Name (`Section_Name__c`)**: Paper section (e.g., *4.2 Evaluation of Warm-Start Page Sharing*).
- **Verification Status (`Verification_Status__c`)**: `Extracted`, `Verified`, `Disputed`, or `Unverified`.
- **Confidence Score (`Confidence_Score__c`)**: Confidence percentage (0-100%).
- **Research Paper (`Research_Paper__c`)**: Lookup to parent paper.
- **Research Map (`Research_Map__c`)**: Master-detail to parent research map.

---

## 6. Open Questions & Experiment Tracker (`Research Gaps` Tab)

The **Research Gap** (`Research_Gap__c`) object tracks unsolved scientific questions and planned validation experiments.

### Key Fields:
- **Problem Statement (`Problem_Statement__c`)**: The identified limitation in current literature.
- **Proposed Experiment (`Proposed_Experiment__c`)**: Concrete experimental setup and benchmark protocol to resolve the gap.
- **Priority (`Priority__c`)**: `Low`, `Medium`, or `High`.
- **Estimated Complexity (`Estimated_Complexity__c`)**: `Low`, `Medium`, or `High`.
- **Status (`Status__c`)**: `Identified` &rarr; `In Review` &rarr; `Experiment Drafted` &rarr; `Addressed`.
- **Research Map (`Research_Map__c`)**: Master-detail link to the research map.

---

## 7. Conflict & Debate Resolution (`Research Conflicts` Tab)

The **Research Conflict** (`Research_Conflict__c`) object catalogs scientific disagreements between two papers.

### Key Fields:
- **Paper A (`Paper_A__c`)**: Lookup to first research paper.
- **Paper B (`Paper_B__c`)**: Lookup to second research paper.
- **Disagreement Area (`Disagreement_Area__c`)**: The core topic of contention (e.g., *MicroVM Memory Overcommit Scalability*).
- **Conflict Description (`Conflict_Description__c`)**: Detailed analysis explaining the differing conclusions or methodologies.
- **Severity (`Severity__c`)**: `Low`, `Moderate`, or `Direct Contradiction`.
- **Research Map (`Research_Map__c`)**: Master-detail link to the research map.

---

## 8. Lightning Web Components (LWC) Deep Dive

Ereuna includes 5 custom Lightning Web Components developed using modern ECMAScript and Salesforce Lightning Design System (SLDS):

### 1. `ereunaDashboardHome`
- **Location**: Default component on the `Radar Dashboard` tab (`Ereuna_Home` AppPage).
- **Functionality**:
  - Dynamically computes KPI totals using Apex wire adapters.
  - Embeds the `ereunaTopicSearch` synthesizer.
  - Provides quick discipline filtering buttons.
  - Lists recent syntheses and enables 1-click record navigation.

### 2. `ereunaTopicSearch`
- **Location**: Embedded in `ereunaDashboardHome`.
- **Functionality**:
  - Dispatches synthesis requests to `EreunaController.createOrSynthesizeMap()`.
  - Displays instant loading animations and status toasts (`lightning/platformShowToastEvent`).

### 3. `citationNetworkGraph`
- **Location**: Available on `Research_Map__c` Record Pages.
- **Functionality**:
  - Renders an interactive force-directed citation network graph using SVG.
  - Visualizes papers as nodes (sized by citation count) and citation relationships as directed edges.
  - Clicking any node opens the paper modal with title, authors, venue, and DOI.

### 4. `literatureCompareMatrix`
- **Location**: Available on `Research_Map__c` Record Pages.
- **Functionality**:
  - Renders a multi-column comparison table comparing all papers in a map.
  - Compares Venue, Publication Year, Citations, Discipline, Relevance Score, and Inclusion Rationale.

### 5. `gapExperimentTracker`
- **Location**: Available on `Research_Map__c` Record Pages.
- **Functionality**:
  - Renders interactive status cards for open research gaps.
  - Enables 1-click status transitions (`Identified` &rarr; `In Review` &rarr; `Experiment Drafted` &rarr; `Addressed`) updating Salesforce records in real-time.

---

## 9. Apex Controllers & Data Services Reference

### `EreunaController`
Primary controller for LWC components, enforcing `with sharing` security:
- `getRecentMaps(String discipline)`: Fetches up to 25 recent research maps filtered by discipline.
- `getMapDetails(Id mapId)`: Retrieves full details of a specific map.
- `getMapPapers(Id mapId)`: Retrieves linked papers with relevance scores.
- `getMapFindings(Id mapId)`: Retrieves verified findings for a map.
- `getMapConflicts(Id mapId)`: Retrieves detected conflicts for a map.
- `getMapGaps(Id mapId)`: Retrieves open research gaps.
- `getCitationNetwork(Id mapId)`: Generates GraphNode and GraphLink structures for SVG graph rendering.
- `createOrSynthesizeMap(String topic, String discipline)`: Automated synthesis engine.
- `updateGapStatus(Id gapId, String newStatus)`: Updates research gap lifecycle state.

### `EreunaSeeder`
Automated data generation engine for setting up a realistic research environment:
- `seedAll()`: Resets and populates the entire research knowledge base (8 maps, 18 papers, 19 links, 15 metrics, 11 findings, 3 conflicts, 7 gaps).
- `seedBatch2()`: Ingests an additional batch of papers, findings, and experiments.

---

## 10. Data Ingestion & Migration (Data Loader & Import Wizard)

To demonstrate enterprise data migration as covered in Cloud Computing curricula:

### Option A: Salesforce Data Import Wizard
1. In Salesforce Setup, type **Data Import Wizard** into Quick Find.
2. Click **Launch Wizard!**.
3. Under **Custom Objects**, select **Research Papers**.
4. Choose **Add new and update existing records**.
5. Match by **DOI**.
6. Select and upload `salesforce/data/Research_Paper__c.csv`.
7. Verify field mappings (`Title__c`, `Authors__c`, `DOI__c`, `Publication_Year__c`, etc.).
8. Click **Start Import**.

### Option B: Salesforce CLI Bulk Insert
```bash
sf data import tree --files salesforce/data/Research_Paper__c.csv --sobject Research_Paper__c
```

---

## 11. Validation Rules & Data Integrity Controls

Ereuna enforces 4 strict business rules to prevent data corruption:

| Rule Developer Name | Target Object | Business Logic Condition | Error Message |
| :--- | :--- | :--- | :--- |
| `VR_Valid_DOI_Prefix` | `Research_Paper__c` | `NOT(BEGINS(DOI__c, "10."))` | *"DOI must begin with the standard prefix '10.' (e.g., 10.1145/...)"* |
| `VR_Publication_Year_Range` | `Research_Paper__c` | `Publication_Year__c < 1900 \|\| Publication_Year__c > YEAR(TODAY())` | *"Publication Year must be between 1900 and the current year."* |
| `VR_Synthesized_Map_Needs_Summary` | `Research_Map__c` | `ISPICKVAL(Status__c, "Synthesized") && ISBLANK(Synthesis_Summary__c)` | *"Synthesized Research Maps must have a comprehensive Synthesis Summary."* |
| `VR_Verified_Finding_Needs_Quote` | `Research_Finding__c` | `ISPICKVAL(Verification_Status__c, "Verified") && ISBLANK(Exact_Quote__c)` | *"Verified findings must include the exact textual quote from the paper."* |

---

*Manual compiled for Ereuna Research Radar &bull; Cloud Computing Platform Architecture.*
