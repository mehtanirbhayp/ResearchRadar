# Research Radar: Project State & AI Memory Storage

> **Notice for Future AI Models & Collaborators**:  
> This file is the primary context snapshot and memory storage for the **Research Radar** project. If you are a new AI model or engineer taking over this repository, reading this document provides 100% full context of the project architecture, deployed Salesforce components, database records, CLI credentials, and operational workflows.

---

## 1. Project Overview & Context

- **Project Name**: Research Radar
- **Primary Domain**: Chemical Engineering (Heterogeneous Catalysis, Continuous-Flow Microreactors, Carbon Capture Membranes, Green Hydrogen PEM Electrolysis, Kinetic Modeling)
- **Supported Engineering Branches**: Mechanical Engineering (Thermal Systems & CFD), Civil Engineering (Geopolymers & Bio-Concrete), Electrical & Electronics (GaN Power Systems), Electronics & Communication (Sub-THz 6G Networks)
- **Platform Architecture**: Implemented natively on **Salesforce Lightning Platform (PaaS / SaaS)**
- **Repository Root**: `/Users/nirbhaymehta/Desktop/Ereuna`
- **Salesforce Project Directory**: `/Users/nirbhaymehta/Desktop/Ereuna/salesforce`

---

## 2. Connected Salesforce Org Environment

- **Default Org Alias**: `trailheadOrg`
- **Connected Username**: `nirbhay.pmehta2024@brave-hawk-mv84a9.com`
- **Org ID**: `00DdM000012iG5pUAE`
- **API Version**: `v62.0` / `v67.0` (Spring '24 / Winter '25)
- **Status**: Connected & Active (Default DevHub / Org)
- **To test org connectivity**:
  ```bash
  cd salesforce
  sf org display --target-org trailheadOrg
  ```

---

## 3. Current Live Database State (In Org)

The Salesforce database is populated with realistic academic research data centered on Chemical Engineering and multi-branch engineering:

| Object API Name | Label | Role in System |
| :--- | :--- | :--- |
| `Research_Map__c` | Research Map | High-level synthesis topics with roll-up counters & summaries (CO2 hydrogenation, MOF membranes, PEM electrolysis, microchannels, geopolymer concrete) |
| `Research_Paper__c` | Research Paper | Peer-reviewed academic papers with DOIs, citations, venues (Journal of Catalysis, AIChE Journal, Chem. Eng. Science, Int. J. Hydrogen Energy) |
| `Map_Paper_Link__c` | Map Paper Link | Junction object connecting papers to maps with relevance scores and inclusion rationales |
| `Research_Finding__c` | Research Finding | Empirical claims verified with verbatim quotes, page numbers, and spectroscopy observations |
| `Extracted_Metric__c` | Extracted Metric | Quantitative benchmarks (Space-Time Yield, Selectivity %, Heat Transfer Coeff, Overpotential, Compressive Strength) |
| `Research_Conflict__c` | Research Conflict | Scientific debates between Paper A and Paper B with severity (Reaction Mechanisms: Formate vs Hydroxycarbonyl) |
| `Research_Gap__c` | Research Gap | Open research questions with proposed validation experiments and status tracking |

To re-seed or verify at any time:
```bash
cd salesforce
echo "EreunaSeeder.seedAll(); EreunaSeeder.seedBatch2();" | sf apex run
```

---

## 4. Deployed Salesforce Metadata Architecture

### 4.1 Custom Application
- **`Ereuna_Research_Radar.app-meta.xml`**:
  - Lightning App with brand header `#1B365D`.
  - Configured Tabs (in order, 100% interactive LWC pages — zero default Salesforce tables):
    1. `Ereuna_Home` (Radar Dashboard AppPage hosting `ereunaDashboardHome`)
    2. `Research_Map_Hub` (Research Maps Hub hosting `mapExplorer`)
    3. `Paper_Explorer` (Research Papers Hub hosting `paperExplorer`)
    4. `Gap_Board` (Research Gaps Kanban Board hosting `gapKanbanBoard`)
    5. `Findings_Explorer` (Research Findings & Evidence Hub hosting `findingsExplorer`)
    6. `standard-report` (Reports)
    7. `standard-Dashboard` (Dashboards)

### 4.2 FlexiPages & Custom Tabs
- **`Ereuna_Home.flexipage-meta.xml`**: Lightning AppPage hosting `ereunaDashboardHome`.
- **`Research_Map_Hub.flexipage-meta.xml`**: Lightning AppPage hosting `mapExplorer`.
- **`Paper_Explorer.flexipage-meta.xml`**: Lightning AppPage hosting `paperExplorer`.
- **`Gap_Board.flexipage-meta.xml`**: Lightning AppPage hosting `gapKanbanBoard`.
- **`Findings_Explorer.flexipage-meta.xml`**: Lightning AppPage hosting `findingsExplorer`.
- **`Research_Map_Record_Page.flexipage-meta.xml`**: Lightning RecordPage (`flexipage:recordHomeTemplateDesktop`) hosting `researchMapWorkspace` activated as the View override for `Research_Map__c`.
- **Custom Tabs**:
  - `Ereuna_Home` (Label: "Home")
  - `Research_Map_Hub` (Label: "Research Maps")
  - `Paper_Explorer` (Label: "Research Papers")
  - `Gap_Board` (Label: "Research Gaps")
  - `Findings_Explorer` (Label: "Research Findings")

### 4.3 Permission Sets
- **`Ereuna_Researcher_Access.permissionset-meta.xml`**:
  - Grants full CRUD on all 7 custom objects.
  - Grants Read on rollup summary fields (`Total_Papers__c`, `Total_Findings__c`, etc.).
  - Grants access to `Ereuna_Research_Radar` app and all custom tabs (`Research_Map_Hub`, `Paper_Explorer`, `Gap_Board`, `Findings_Explorer`, `Ereuna_Home`).
  - Grants Apex Class execute access to `EreunaController`, `EreunaSeeder`, and `EreunaDataService`.

### 4.4 Declarative Validation Rules
1. **`Research_Paper__c.VR_Valid_DOI_Prefix`**: DOI must begin with `"10."`.
2. **`Research_Paper__c.VR_Publication_Year_Range`**: Year must be between 1900 and current year.
3. **`Research_Map__c.VR_Synthesized_Map_Needs_Summary`**: If Status = "Synthesized", Summary cannot be blank.
4. **`Research_Finding__c.VR_Verified_Finding_Needs_Quote`**: If Status = "Verified", Exact Quote cannot be blank.

---

## 5. Lightning Web Components (LWC)

All LWCs are located in `salesforce/force-app/main/default/lwc/`:

1. **`mapExplorer`**:
   - Interactive Research Map Hub replacing standard object list tables.
   - Discipline filter pills (`All Disciplines`, `Cloud Computing`, `Distributed Systems`).
   - Live search across Topic titles and Synthesis consensus summaries.
   - Visual cards with status tags (`Synthesized`, `In Progress`, `Draft`), roll-up metric counters (`Total Papers`, `Findings`, `Gaps`, `Conflicts`).
   - 1-click **Launch Workspace** button and **+ Synthesize New Topic** modal with real-time Apex generation.
2. **`paperExplorer`**:
   - Visual academic literature discovery portal replacing plain data tables.
   - Live debounced keyword search across Title, Authors, Venue, and Abstract.
   - Discipline filter pills (`All`, `Cloud Computing`, `Distributed Systems`).
   - View Switcher: Card View (Default) vs Table View.
   - Fire citation count badges (`🔥 485 Citations`), venue badges, and expandable abstract accordions.
   - Extracted benchmark metrics pills rendered directly on each paper card.
   - 1-click **Open PDF**, **View DOI**, and **Copy BibTeX Citation** (with copy-to-clipboard toast).
3. **`gapKanbanBoard`**:
   - 4-column interactive Kanban board (`Identified`, `In Review`, `Experiment Drafted`, `Addressed`).
   - Filter dropdown by Research Topic or view across all maps.
   - Stage progression buttons directly on each card with real-time Apex status updates.
   - "+ Propose New Experiment" modal to log new scientific challenges on the fly.
4. **`findingsExplorer`**:
   - Visual Evidence & Findings Explorer replacing standard object list tables.
   - Clean layout featuring verbatim literature quotes with subtle accent rules.
   - Monochrome confidence scores, verification status, and source publication links.
   - Section name and page number citations (e.g. `Sec. 4.2, p. 8`).
5. **`researchMapWorkspace`**:
   - Minimalist research console rendered on `Research_Map_Record_Page` (100% full width, zero right sidebar).
   - Clean text header with metadata line and roll-up stats counter.
   - 5 Scoped Tabs:
     1. Citation Network (`citationNetworkGraph` - monochrome node graph)
     2. Literature Comparison (`literatureCompareMatrix` - clean comparison table)
     3. Gaps & Experiments (`gapExperimentTracker` - stage transition actions)
     4. Verified Evidence & Findings (Verbatim quotes & debate contradictions)
     5. Record Details (Standard full form)
6. **`ereunaDashboardHome`**:
   - Clean minimalist executive command center on `Ereuna_Home` tab.
   - 4 live monochrome KPI cards (`Research Maps`, `Cataloged Papers`, `Verified Findings`, `Active Gaps`).
   - Quick topic navigation and system operations links.
7. **`ereunaTopicSearch`**:
   - Literature synthesis engine embedded in dashboard with monochrome progress tracker.
8. **`citationNetworkGraph`**:
   - Dynamic SVG citation network visualizer in monochrome black and white.
9. **`literatureCompareMatrix`**:
   - Clean comparison table with black progress indicators and document links.
10. **`gapExperimentTracker`**:
    - Flat challenge cards with 1-click status transitions.

### 5.1 UI/UX Design System Guidelines
- **Color Palette**: Strictly 2-color monochrome B&W (`#000000` text/titles/borders, `#ffffff` background, `#333333`/`#666666` secondary text, `#e5e5e5` hairline rules).
- **Typography**: Clean system font stack (`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif`).
- **No Text Boxes**: No heavy `slds-box` wrappers, no nested cards, no shadows, no colored banners.
- **Authentic & Human-Crafted**: No emojis, no rainbow pills, no AI-generated gradients. High-density, professional academic aesthetic.

---

## 6. Apex Classes & Controllers

Located in `salesforce/force-app/main/default/classes/`:

1. **`EreunaController.cls`**:
   - Declared `with sharing` for security.
   - `@AuraEnabled(cacheable=true)` methods:
     - `getRecentMaps(String discipline)`
     - `getMapDetails(Id mapId)`
     - `getMapPapers(Id mapId)`
     - `getMapFindings(Id mapId)`
     - `getMapConflicts(Id mapId)`
     - `getMapGaps(Id mapId)`
     - `getCitationNetwork(Id mapId)`
   - Mutating methods:
     - `createOrSynthesizeMap(String topic, String discipline)`
     - `updateGapStatus(Id gapId, String newStatus)`
     - `initializeSampleData()`
2. **`EreunaSeeder.cls`**:
   - `seedAll()`: Populates base comprehensive workload (12 papers, 8 maps, metrics, findings, conflicts, gaps).
   - `seedBatch2()`: Ingests second round of papers, links, and experiments (totaling 18 papers, 19 links, 15 metrics, 11 findings, 3 conflicts, 7 gaps).
3. **`EreunaDataService.cls`**:
   - Foundational seed service for initial curriculum mapping.
4. **`EreunaControllerTest.cls`**:
   - Unit tests covering all controller methods with 100% pass rate.

---

## 7. Bulk Data Files for Ingestion Demonstrations

- **`salesforce/data/Research_Paper__c.csv`**:
  - Full CSV catalog containing 18 peer-reviewed papers.
  - Pre-mapped for **Salesforce Data Import Wizard** and **Data Loader**.

---

## 8. Key Documentation Directory

- **`docs/APP_FUNCTIONAL_GUIDE.md`**: Complete user manual and functional reference for every single tab, button, component, and method.
- **`docs/PROJECT_WRITEUP.md`**: Comprehensive academic project report aligned with Cloud Computing (BMEE355E) curriculum.
- **`docs/SALESFORCE_GUIDE.md`**: Step-by-step setup and grading demonstration guide.
- **`docs/EREUNA_PITCH_DOCUMENT.pdf`**: Complete 10-15 minute pitch script, architecture defense, demo flow, moat, and competitive comparison.
- **`PROJECT_MEMORY.md`**: (This file) Core AI state and knowledge snapshot.

---

## 9. Common CLI Operations

```bash
# Check connected orgs
sf org list

# Open org directly in browser
sf org open

# Deploy all metadata
sf project deploy start

# Query data counts
sf data query --query "SELECT count() FROM Research_Paper__c"
sf data query --query "SELECT count() FROM Research_Map__c"

# Run tests
sf apex run test --test-level RunLocalTests --code-coverage
```

---

## 10. Recent Architectural & UI Enhancements

- **Synthesized Research Topics Table**: Fixed missing data render bug by implementing reactive getters `hasRecentMaps` and `recentMaps` in [ereunaDashboardHome.js](file:///Users/nirbhaymehta/Desktop/Ereuna/salesforce/force-app/main/default/lwc/ereunaDashboardHome/ereunaDashboardHome.js). Synthesized topic records now populate immediately.
- **Refined Monochrome KPI Summary Cards**: Redesigned the 4 dashboard metric cards with top accent borders (`border-top: 3px solid #000000`), uppercase tracked category pills, and tabular numerals (`font-variant-numeric: tabular-nums; font-size: 2.4rem; font-weight: 800`), maintaining the exact 4-card rectangular shape in strict B&W.
- **Removed Citation Network & Influence Graph**: Completely removed the Citation Network & Influence Graph from the Research Map workspace. The workspace now focuses directly on the primary structured tools:
  - **Literature Comparison Matrix**: Comprehensive side-by-side benchmark matrix (default active tab).
  - **Gap & Experiment Tracker**: Actionable open problems and validation protocols.
  - **Verified Findings & Evidence**: Verbatim claims with page citations and confidence scores.

---

*Generated and verified for the Ereuna Cloud Computing Architecture Platform.*

