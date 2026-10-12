# Ereuna Research Radar: Project State & AI Memory Storage

> **Notice for Future AI Models & Collaborators**:  
> This file is the primary context snapshot and memory storage for the **Ereuna Research Radar** project. If you are a new AI model or engineer taking over this repository, reading this document provides 100% full context of the project architecture, deployed Salesforce components, database records, CLI credentials, and operational workflows.

---

## 1. Project Overview & Context

- **Project Name**: Ereuna Research Radar
- **Original Context**: Academic literature intelligence and research synthesis engine for Cloud Computing & Distributed Systems.
- **Course**: BMEE355E Cloud Computing
- **Original Tech Stack**: Started as a custom web app (Next.js/Node), then fully migrated and implemented natively on **Salesforce Lightning Platform (PaaS / SaaS)** per course curriculum instructions.
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

The Salesforce database is populated with realistic academic research data:

| Object API Name | Label | Total Seeded Records | Role in System |
| :--- | :--- | :---: | :--- |
| `Research_Map__c` | Research Map | **8** | High-level synthesis topics with roll-up counters & summaries |
| `Research_Paper__c` | Research Paper | **18** | Peer-reviewed academic papers with DOIs, citations, venues |
| `Map_Paper_Link__c` | Map Paper Link | **19** | Junction object connecting papers to maps with relevance scores |
| `Research_Finding__c` | Research Finding | **11** | Empirical claims verified with verbatim quotes and page numbers |
| `Extracted_Metric__c` | Extracted Metric | **15** | Quantitative benchmarks (latency, throughput, CO2, memory) |
| `Research_Conflict__c` | Research Conflict | **3** | Scientific debates between Paper A and Paper B with severity |
| `Research_Gap__c` | Research Gap | **7** | Open research questions with proposed validation experiments |

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
  - Configured Tabs (in order):
    1. `Ereuna_Home` (Radar Dashboard AppPage)
    2. `Research_Map__c`
    3. `Research_Paper__c`
    4. `Research_Finding__c`
    5. `Research_Gap__c`
    6. `Research_Conflict__c`
    7. `standard-report`
    8. `standard-Dashboard`

### 4.2 FlexiPages & Custom Tabs
- **`Ereuna_Home.flexipage-meta.xml`**: Lightning AppPage hosting `ereunaDashboardHome`.
- **`Ereuna_Home.tab-meta.xml`**: Custom Tab linking to the `Ereuna_Home` FlexiPage.

### 4.3 Permission Sets
- **`Ereuna_Researcher_Access.permissionset-meta.xml`**:
  - Grants full CRUD on all 7 custom objects.
  - Grants Read on rollup summary fields (`Total_Papers__c`, `Total_Findings__c`, etc.).
  - Grants access to `Ereuna_Research_Radar` app and all custom tabs.
  - Grants Apex Class execute access to `EreunaController` and `EreunaDataService`.

### 4.4 Declarative Validation Rules
1. **`Research_Paper__c.VR_Valid_DOI_Prefix`**: DOI must begin with `"10."`.
2. **`Research_Paper__c.VR_Publication_Year_Range`**: Year must be between 1900 and current year.
3. **`Research_Map__c.VR_Synthesized_Map_Needs_Summary`**: If Status = "Synthesized", Summary cannot be blank.
4. **`Research_Finding__c.VR_Verified_Finding_Needs_Quote`**: If Status = "Verified", Exact Quote cannot be blank.

---

## 5. Lightning Web Components (LWC)

All LWCs are located in `salesforce/force-app/main/default/lwc/`:

1. **`ereunaDashboardHome`**:
   - Executive dashboard on `Ereuna_Home` tab.
   - 4 live KPI cards (`Research Maps`, `Cataloged Papers`, `Verified Findings`, `Active Gaps`).
   - Discipline filter bar (`All`, `Cloud Computing`, `Distributed Systems`).
   - Interactive table with click-to-navigate record links.
2. **`ereunaTopicSearch`**:
   - Search bar and topic synthesizer embedded in dashboard.
   - Triggers `EreunaController.createOrSynthesizeMap()`.
3. **`citationNetworkGraph`**:
   - Dynamic SVG force-directed citation network visualizer.
   - Sized by citation count, node hover tooltips, and click modal details.
4. **`literatureCompareMatrix`**:
   - Side-by-side multi-column comparison table of papers in a research map.
5. **`gapExperimentTracker`**:
   - Kanban-inspired status cards with interactive status transitions (`Identified` &rarr; `In Review` &rarr; `Experiment Drafted` &rarr; `Addressed`).

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

*Generated and verified for the Ereuna Cloud Computing Architecture Platform.*
