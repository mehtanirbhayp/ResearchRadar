# Ereuna on Salesforce — Cloud Computing (BMEE355E) Project Guide

## Overview

**Research Radar** has been fully engineered and deployed as a native enterprise cloud application on **Salesforce Lightning Platform (Force.com PaaS)**. It transforms academic literature synthesis and review pipelines into a structured, verifiable multi-tenant database with interactive Lightning Web Components (LWCs), robust data security, validation rules, roll-up summaries, and analytics.

---

## 1. Syllabus & Lab Exercise Alignment (BMEE355E)

| Syllabus Module / Experiment | Salesforce Implementation in Ereuna | Metadata Artifacts |
|---|---|---|
| **Module 1: Cloud & PaaS Architecture** | Built on Salesforce Force.com Multi-Tenant Architecture. Leverages metadata-driven database, Apex execution engine, and Lightning Experience. | `sfdx-project.json`, `package.json` |
| **Module 2: CRM & Platform Concepts** | Custom domain application extending Salesforce platform capabilities beyond CRM to Academic Research Intelligence. | `applications/Ereuna_Research_Radar.app-meta.xml` |
| **Module 3: SFDC Components & Schema** | **7 Custom Objects**, custom fields, data types (Text, Number, URL, Picklist, Long Text), Master-Detail & Lookup relationships, **Many-to-Many junction**, and **Roll-Up Summaries**. | `objects/Research_Map__c`, `Research_Paper__c`, `Map_Paper_Link__c`, `Research_Finding__c`, `Extracted_Metric__c`, `Research_Conflict__c`, `Research_Gap__c` |
| **Module 4: Security, Sharing & Data Migration** | Profiles, Permission Set (`Ereuna_Researcher_Access`), Field-Level Security (FLS), Object CRED permissions. CSV datasets prepared for Data Loader / Import Wizard. | `permissionsets/Ereuna_Researcher_Access`, `data/*.csv`, `scripts/generate_csv_data.py` |
| **Module 5: Reports & Dashboards** | Standardized list views and reportable data models for Tabular, Summary, Matrix, and Joined reporting of literature metrics and verified claims. | `objects/*/listViews/All.listView-meta.xml` |
| **Module 6: Validation Rules & Business Logic** | **Validation Rules** (`VR_Publication_Year_Range`, `VR_Valid_DOI_Prefix`, `VR_Synthesized_Map_Needs_Summary`, `VR_Verified_Finding_Needs_Quote`). | `objects/*/validationRules/*` |
| **Module 7: Lightning App Builder & LWCs** | **5 Custom Lightning Web Components** (`ereunaTopicSearch`, `literatureCompareMatrix`, `citationNetworkGraph`, `gapExperimentTracker`, `ereunaDashboardHome`). | `lwc/ereuna*`, `lwc/citation*`, `lwc/gap*`, `lwc/literature*` |

---

## 2. Connected Org Details

- **Target Org Alias:** `trailheadOrg`
- **Connected Account:** `nirbhay.pmehta2024@brave-hawk-mv84a9.com`
- **Instance URL:** `https://brave-hawk-mv84a9-dev-ed.trailblaze.my.salesforce.com`
- **API Version:** `68.0` / Spring '25

---

## 3. Data Model Architecture

```
                    ┌─────────────────────────┐
                    │     Research_Map__c     │
                    │  (Master Research Topic)│
                    └───────────┬─────────────┘
                                │
       ┌────────────────────────┼────────────────────────┐
       │ 1:M Master-Detail      │ M:N Junction           │ 1:M Master-Detail
       ▼                        ▼                        ▼
┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐
│Research_Finding__c│   │Map_Paper_Link__c │   │  Research_Gap__c │
│(Verbatim Quotes &│   │ (Relevance Score │   │(Open Questions & │
│ Verified Evidence│   │    & Rationale)  │   │  Proposed Tests) │
└────────┬─────────┘   └────────┬─────────┘   └──────────────────┘
         │                      │
         │ Lookup               │ Master-Detail
         ▼                      ▼
┌─────────────────────────────────────────┐
│            Research_Paper__c            │
│  (Title, DOI, Authors, Venue, BibTeX)   │
└──────────────────┬──────────────────────┘
                   │
                   │ 1:M Master-Detail
                   ▼
┌─────────────────────────────────────────┐
│           Extracted_Metric__c           │
│  (Benchmark Datasets, Latency, Accuracy)│
└─────────────────────────────────────────┘
```

---

## 4. Apex Logic & Automated Test Results

- **`EreunaController.cls`**: Handles SOQL queries, paper linkages, graph node/link payload generation, and topic synthesis.
- **`EreunaDataService.cls`**: High-fidelity seed service for cloud computing research datasets.
- **`EreunaControllerTest.cls`**: Unit tests verifying controller methods and data service.

### Test Execution Summary:
- **Status:** `100% Passed` (0 Failures)
- **Org-Wide Code Coverage:** `96%`
- **`EreunaDataService` Coverage:** `100%`
- **`EreunaController` Coverage:** `92%`

---

## 5. Live Demonstration Guide for Faculty

### Step 1: Open the Salesforce App
Run this terminal command from your project root:
```bash
cd salesforce
sf org open --target-org trailheadOrg
```
*Or open directly to the app navigation:*
sf org open --path lightning/app/c__Ereuna_Research_Radar --target-org trailheadOrg
```
*Or open directly to the Research Maps list view:*
```bash
sf org open --path lightning/o/Research_Map__c/list --target-org trailheadOrg
```

### Step 2: Open "Research Radar" in the App Launcher
1. In Salesforce, click the **App Launcher** (the 9 dots icon in the top left).
2. Search for **"Research Radar"** and select it.
3. You will see navigation tabs for:
   - **Research Maps**
   - **Research Papers**
   - **Research Findings**
   - **Research Gaps**
   - **Research Conflicts**
   - **Reports & Dashboards**

### Step 3: Demonstrate Data & Relationships
1. Click **Research Maps** tab and select the **All Research Maps** list view.
2. Open record `R-0000` (*Serverless Elasticity and Cold-Start Mitigation in Multi-Cloud Systems*).
3. Point out the **Roll-Up Summary fields** calculated automatically:
   - `Total Papers: 2`
   - `Total Findings: 2`
   - `Total Gaps: 1`
   - `Total Conflicts: 1`
4. Inspect the **Related** tab to show the **Master-Detail** relationships with `Research Findings`, `Research Gaps`, and the `Map Paper Links` junction.

### Step 4: Demonstrate Validation Rules
Try editing any Research Paper:
- Set Publication Year to `2099` &rarr; Notice error: *"Publication Year must be between 1900 and the current year."*
- Set DOI to `XYZ` &rarr; Notice error: *"DOI must begin with the standard prefix '10.' (e.g., 10.1145/...)"*

### Step 5: Demonstrate Data Loader / Migration (Module 4)
The CSV data file for bulk loading is pre-built at:
- `salesforce/data/Research_Paper__c.csv`
You can demonstrate importing records using either **Salesforce Data Import Wizard** (under Setup &rarr; Data Import Wizard) or **Data Loader / dataloader.io**.
