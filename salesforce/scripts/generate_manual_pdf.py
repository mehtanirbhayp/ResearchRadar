#!/usr/bin/env python3
"""
Generate publication-grade PDF:
Research Radar - User Manual, Terms & Conditions, Legal Disclaimers, Data Provenance, and Regulatory Compliance Framework
Multi-Disciplinary Engineering & Applied Sciences Standard
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#555555"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 750, "RESEARCH RADAR  |  User Manual, Terms, Legal Disclaimer & Compliance")
            self.drawRightString(letter[0] - 54, 750, "Doc Ref: RR-MANUAL-2026-V1")
            self.setStrokeColor(colors.HexColor("#000000"))
            self.setLineWidth(0.75)
            self.line(54, 744, letter[0] - 54, 744)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#d0d0d0"))
        self.setLineWidth(0.5)
        self.line(54, 48, letter[0] - 54, 48)
        self.drawString(54, 36, "CONFIDENTIAL & PROPRIETARY  —  RESEARCH RADAR PLATFORM GOVERNANCE")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 54, 36, page_text)
        self.restoreState()

def create_manual_pdf(filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=60,
        bottomMargin=60
    )

    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#000000'),
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#333333'),
        spaceAfter=12
    )

    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#444444')
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=12.5,
        leading=16,
        textColor=colors.HexColor('#000000'),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor('#111111'),
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#222222'),
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'BulletDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11.5,
        textColor=colors.HexColor('#222222'),
        leftIndent=12,
        spaceAfter=3
    )

    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#111111')
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor('#ffffff')
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#111111')
    )

    story = []

    # -------------------------------------------------------------
    # COVER / HEADER BANNER
    # -------------------------------------------------------------
    story.append(Paragraph("RESEARCH RADAR", title_style))
    story.append(Paragraph("Multi-Disciplinary Engineering & Applied Sciences Literature Intelligence Platform", subtitle_style))
    
    meta_table_data = [
        [
            Paragraph("<b>DOCUMENT REF:</b> RR-MANUAL-2026-V1", meta_style),
            Paragraph("<b>EFFECTIVE DATE:</b> October 2026", meta_style),
            Paragraph("<b>PLATFORM VERSION:</b> v4.2 Lightning PaaS", meta_style)
        ],
        [
            Paragraph("<b>PRIMARY SCOPE:</b> Engineering & Physical Sciences", meta_style),
            Paragraph("<b>BRANCHES:</b> CS, Electrical, Mechanical, Civil, Chemical, Materials", meta_style),
            Paragraph("<b>SECURITY STANDARD:</b> Enterprise Academic Compliance", meta_style)
        ]
    ]
    meta_table = Table(meta_table_data, colWidths=[170, 170, 164])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f7f7f7')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#000000')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e0e0e0')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 10))

    # Executive Overview Box
    exec_summary_text = (
        "<b>EXECUTIVE NOTICE:</b> Research Radar is an enterprise-grade autonomous academic literature intelligence platform architected "
        "natively on Salesforce Lightning PaaS. This document constitutes the formal User Operational Manual, Terms & Conditions, "
        "Engineering Research Disclaimers, Data Provenance Disclosures, and Regulatory Compliance Documentation for researchers, faculty, and institutions."
    )
    exec_table = Table([[Paragraph(exec_summary_text, callout_style)]], colWidths=[504])
    exec_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#ffffff')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#000000')),
        ('LINEBEFORE', (0,0), (0,-1), 4, colors.HexColor('#000000')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(exec_table)
    story.append(Spacer(1, 10))

    # -------------------------------------------------------------
    # SECTION 1: COMPREHENSIVE USER OPERATIONAL MANUAL
    # -------------------------------------------------------------
    story.append(Paragraph("1. User Operational Manual", h1_style))
    story.append(Paragraph(
        "Research Radar accelerates academic literature reviews across engineering and scientific disciplines from several weeks "
        "to sub-second deterministic queries. It organizes complex scientific corpora into actionable, structured entities linked via relational ACID schemas.",
        body_style
    ))

    story.append(Paragraph("1.1 Architecture & Primary Workspaces", h2_style))
    story.append(Paragraph(
        "Upon logging into Salesforce, select <b>Research Radar</b> from the App Launcher (9-dot menu). "
        "The system provides five dedicated functional workspaces accessible via the top navigation bar:",
        body_style
    ))
    story.append(Paragraph("• <b>Research Radar Dashboard:</b> Real-time executive KPIs, quick branch filters (All, Chemical, Mechanical, Civil, EEE, ECE), literature synthesis bar, and top-bar governance menu.", bullet_style))
    story.append(Paragraph("• <b>Research Maps Hub:</b> Master topological catalog displaying synthesized maps, discipline tags, and launch buttons for deep interactive workspaces.", bullet_style))
    story.append(Paragraph("• <b>Research Papers Catalog:</b> Full-text repository indexed by DOI, publication year, peer-reviewed journal prestige, citation counts, and BibTeX citations.", bullet_style))
    story.append(Paragraph("• <b>Research Gap Board:</b> Interactive Kanban board tracking open empirical questions and proposed validation experiment protocols across lifecycle stages.", bullet_style))
    story.append(Paragraph("• <b>Verified Findings Explorer:</b> Granular empirical claim catalog featuring verbatim quote extractions, statistical confidence scores, and methodological tags.", bullet_style))

    story.append(Paragraph("1.2 Autonomous Literature Synthesis Workflow", h2_style))
    story.append(Paragraph(
        "To synthesize a new research cluster or explore uncharted engineering domains:",
        body_style
    ))
    story.append(Paragraph("1. <b>Navigate to Dashboard:</b> Locate the 'Literature Synthesis Engine' search bar.", bullet_style))
    story.append(Paragraph("2. <b>Input Query:</b> Enter your research phrase (e.g., <i>'Serverless cold-start latency mitigation'</i>, <i>'GaN microgrid power conversion'</i>, or <i>'Microchannel conjugate heat transfer'</i>).", bullet_style))
    story.append(Paragraph("3. <b>Select Discipline Focus:</b> Filter by All Disciplines, Computer Science, Electrical, Mechanical, Civil, Chemical, or Materials Science.", bullet_style))
    story.append(Paragraph("4. <b>Execute Synthesis:</b> Click <b>Generate Research Map</b>. Apex controllers query indexed databases, instantiate a new Research_Map__c record, correlate matching peer-reviewed papers via junction objects, extract quantitative metrics, and flag active contradictions.", bullet_style))
    story.append(Paragraph("5. <b>Launch Interactive Workspace:</b> Click <b>Open Workspace &rarr;</b> in the synthesized topics table to inspect the deep multi-paper comparison matrix and empirical evidence.", bullet_style))

    story.append(Paragraph("1.3 Metric Comparison Matrix & Engineering Parameters", h2_style))
    story.append(Paragraph(
        "Inside the Research Map Interactive Workspace, the <b>Literature Comparison Matrix</b> aligns benchmark values side-by-side across physical and engineering metrics:",
        body_style
    ))
    story.append(Paragraph("• <b>Performance & Latency:</b> Cold-start latency (ms), execution overhead, throughput (req/s), and computational scalability.", bullet_style))
    story.append(Paragraph("• <b>Energy & Power Density:</b> Power conversion efficiency %, power density (W/cm²), and electrochemical overpotentials (mV).", bullet_style))
    story.append(Paragraph("• <b>Thermal & Transport Phenomena:</b> Heat transfer coefficient (W/m²·K), thermal conductivity, and Nusselt/Reynolds correlations.", bullet_style))
    story.append(Paragraph("• <b>Materials & Structural Yield:</b> Space-Time Yield (g/kg·h), separation selectivity factor, and compressive strength (MPa).", bullet_style))

    story.append(Paragraph("1.4 Research Gap Lifecycle Management", h2_style))
    story.append(Paragraph(
        "The Research Gap Kanban Board enables principal investigators and graduate researchers to shepherd unresolved scientific questions into active experimental trials:",
        body_style
    ))
    story.append(Paragraph("• <b>Identified:</b> Contradiction or missing variable highlighted by synthesis engine.", bullet_style))
    story.append(Paragraph("• <b>In Review:</b> Research committee evaluating physical feasibility and lab resource availability.", bullet_style))
    story.append(Paragraph("• <b>Experiment Drafted:</b> Comprehensive protocol formalizing sample preparation, test setups, and instrumentation.", bullet_style))
    story.append(Paragraph("• <b>Addressed:</b> Empirical data gathered, validating or refuting conflicting prior literature.", bullet_style))

    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # SECTION 2: TERMS AND CONDITIONS OF SERVICE
    # -------------------------------------------------------------
    story.append(Paragraph("2. Terms and Conditions of Service", h1_style))
    story.append(Paragraph(
        "By accessing or utilizing Research Radar, the user agrees to be bound by the following academic terms and conditions:",
        body_style
    ))

    story.append(Paragraph("2.1 Academic Integrity & Acceptable Use", h2_style))
    story.append(Paragraph(
        "Research Radar is provided exclusively for verified academic, educational, and scientific research. "
        "Users agree to abide by international standards of academic integrity (such as IEEE, ACM, ACS, and COPE publication ethics). "
        "Users shall not utilize the platform to generate misleading, falsified, or plagiarized research output.",
        body_style
    ))

    story.append(Paragraph("2.2 Intellectual Property & Research Ownership", h2_style))
    story.append(Paragraph(
        "• <b>User-Generated Syntheses:</b> Users retain 100% intellectual property ownership over newly synthesized Research Maps, original experimental gap protocols, and derived lab hypotheses formulated within their private org tenancy.",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Primary Source Copyrights:</b> All cataloged research papers, original abstracts, publisher metadata, and verbatim quotations remain the copyrighted property of their respective authors and publishing societies (e.g., IEEE, ACM, Elsevier, ACS, Wiley, Springer Nature).",
        bullet_style
    ))
    story.append(Paragraph(
        "• <b>Fair Use Compliance:</b> Platform excerpting complies strictly with 17 U.S. Code § 107 (Fair Use) and Directive (EU) 2019/790 for Text and Data Mining (TDM) in scientific research.",
        bullet_style
    ))

    story.append(Paragraph("2.3 Subscription Quotas & Prohibited Operations", h2_style))
    story.append(Paragraph(
        "Users are prohibited from: (a) attempting to reverse engineer or decompile Apex codebase; (b) launching unthrottled automated scraping bots against the platform API; "
        "or (c) sublicensing access credentials to unauthorized commercial third parties.",
        body_style
    ))

    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # SECTION 3: LEGAL DISCLAIMER & RESEARCH INTEGRITY ADVISORY
    # -------------------------------------------------------------
    story.append(Paragraph("3. Legal Disclaimer & Research Integrity Advisory", h1_style))
    
    # Revised Academic/Engineering Notice Box
    disclaimer_lead_text = (
        "<b>ACADEMIC RESEARCH & ENGINEERING IMPLEMENTATION NOTICE:</b><br/>"
        "Research Radar is an automated computational intelligence platform developed strictly for academic literature synthesis, "
        "conceptual exploratory research, and citation analysis. <b>Algorithmic outputs, extracted metrics, and synthesized research maps "
        "are assistive resources and DO NOT constitute certified peer review, professional engineering design certification, "
        "or actionable laboratory protocols.</b>"
    )
    disclaimer_table = Table([[Paragraph(disclaimer_lead_text, callout_style)]], colWidths=[504])
    disclaimer_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#fafafa')),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#000000')),
        ('LINEBEFORE', (0,0), (0,-1), 4, colors.HexColor('#000000')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(disclaimer_table)
    story.append(Spacer(1, 6))

    story.append(Paragraph("3.1 Independent Professional & Experimental Verification", h2_style))
    story.append(Paragraph(
        "Researchers, engineers, and practitioners must independently verify all extracted data, quantitative metrics, mathematical formulas, "
        "and methodological procedures against primary publisher DOI sources before applying them in physical engineering implementations, "
        "structural designs, electronic circuits, software systems, or laboratory experiments.",
        body_style
    ))

    story.append(Paragraph("3.2 Operational & Laboratory Safety Advisory", h2_style))
    story.append(Paragraph(
        "Experimental and physical engineering research (including chemical processes, electrical prototyping, thermal management, and structural fabrication) "
        "involves inherent physical hazards. All experimental testing must be conducted under qualified institutional supervision with appropriate "
        "Environmental Health & Safety (EHS), OSHA, and IEEE electrical safety protocols.",
        body_style
    ))

    story.append(Paragraph("3.3 Warranty & Liability Limitation", h2_style))
    story.append(Paragraph(
        "THE PLATFORM IS PROVIDED 'AS IS' WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED. UNDER NO CIRCUMSTANCES SHALL RESEARCH RADAR, "
        "ITS DEVELOPERS, OR AFFILIATED INSTITUTIONS BE HELD LIABLE FOR DIRECT, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL DAMAGES "
        "ARISING FROM RELIANCE ON SYNTHESIZED LITERATURE, DESIGN CHOICES, OR PHYSICAL EXPERIMENTAL FAILURES.",
        body_style
    ))

    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # SECTION 4: DATA SOURCES & PROVENANCE ARCHITECTURE
    # -------------------------------------------------------------
    story.append(Paragraph("4. Data Sources & Provenance Architecture", h1_style))
    story.append(Paragraph(
        "Research Radar enforces strict citation provenance. Every cataloged paper, metric, and finding originates from authoritative, "
        "peer-reviewed academic indexing repositories across all STEM branches:",
        body_style
    ))

    sources_data = [
        [
            Paragraph("<b>Repository Source</b>", table_header_style),
            Paragraph("<b>Ingestion Protocol</b>", table_header_style),
            Paragraph("<b>Coverage Scope</b>", table_header_style),
            Paragraph("<b>Attribution Standard</b>", table_header_style)
        ],
        [
            Paragraph("<b>CrossRef REST API</b>", table_cell_style),
            Paragraph("Direct HTTPS JSON-LD", table_cell_style),
            Paragraph("Official DOI registration, metadata, funding agencies across all branches", table_cell_style),
            Paragraph("Permanent DOI URI Links", table_cell_style)
        ],
        [
            Paragraph("<b>OpenAlex Academic Graph</b>", table_cell_style),
            Paragraph("REST Entity Endpoint", table_cell_style),
            Paragraph("250M+ publications: CS, Electrical, Mechanical, Civil, Chemical", table_cell_style),
            Paragraph("CC0 Open Metadata License", table_cell_style)
        ],
        [
            Paragraph("<b>Semantic Scholar (S2)</b>", table_cell_style),
            Paragraph("Graph API v1", table_cell_style),
            Paragraph("Highly influential citations, citation velocity, TLDR summaries", table_cell_style),
            Paragraph("Semantic Scholar Attribution", table_cell_style)
        ],
        [
            Paragraph("<b>arXiv & TechRxiv</b>", table_cell_style),
            Paragraph("OAI-PMH & Atom Feeds", table_cell_style),
            Paragraph("Preprints in Computer Science, Systems, Electrical, and Physics", table_cell_style),
            Paragraph("arXiv Open Access terms", table_cell_style)
        ],
        [
            Paragraph("<b>Publisher Feeds (IEEE/ACM/Elsevier)</b>", table_cell_style),
            Paragraph("Authorized TDM APIs", table_cell_style),
            Paragraph("Full-text structured XML, tables, benchmarks, conference proceedings", table_cell_style),
            Paragraph("Publisher Fair Use / TDM", table_cell_style)
        ]
    ]

    sources_table = Table(sources_data, colWidths=[120, 100, 164, 120])
    sources_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#000000')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#000000')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e0e0e0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(sources_table)
    story.append(Spacer(1, 6))

    story.append(Paragraph("4.1 Ingestion & Verification Pipeline", h2_style))
    story.append(Paragraph(
        "1. <b>DOI Resolvability Check:</b> Every publication undergoes programmatic regex validation against the International DOI Foundation (IDF) resolver standard.",
        bullet_style
    ))
    story.append(Paragraph(
        "2. <b>Deduplication:</b> Canonical DOIs prevent duplicate indexing across cross-listed preprint repositories and final peer-reviewed journal issues.",
        bullet_style
    ))
    story.append(Paragraph(
        "3. <b>Extraction Provenance:</b> Every extracted finding retains exact page number, table index, and verbatim quotation to maintain an unalterable chain of custody.",
        bullet_style
    ))

    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # SECTION 5: REGULATORY COMPLIANCE & GOVERNANCE STANDARDS
    # -------------------------------------------------------------
    story.append(Paragraph("5. Regulatory Compliance & Governance Standards", h1_style))
    story.append(Paragraph(
        "Research Radar is designed to satisfy the world's most stringent academic, data privacy, and scientific standards:",
        body_style
    ))

    reg_data = [
        [
            Paragraph("<b>Regulation / Framework</b>", table_header_style),
            Paragraph("<b>Compliance Mechanism</b>", table_header_style),
            Paragraph("<b>Implementation Details</b>", table_header_style)
        ],
        [
            Paragraph("<b>GDPR (EU 2016/679) & CCPA</b>", table_cell_style),
            Paragraph("Zero-Data Retention Architecture", table_cell_style),
            Paragraph("No private user search queries or proprietary draft hypotheses are sold, monetized, or shared with external model trainers.", table_cell_style)
        ],
        [
            Paragraph("<b>EU Artificial Intelligence Act</b>", table_cell_style),
            Paragraph("Transparency & Explainability (Article 52)", table_cell_style),
            Paragraph("All AI-synthesized research summaries clearly disclose algorithmic provenance and cite underlying human-authored primary literature.", table_cell_style)
        ],
        [
            Paragraph("<b>FAIR Scientific Data Principles</b>", table_cell_style),
            Paragraph("Findable, Accessible, Interoperable, Reusable", table_cell_style),
            Paragraph("Structured JSON-LD schema, BibTeX exports, and standardized engineering ontologies.", table_cell_style)
        ],
        [
            Paragraph("<b>IEEE & ACM Code of Ethics</b>", table_cell_style),
            Paragraph("Algorithmic Accountability", table_cell_style),
            Paragraph("Strict measures to prevent algorithmic bias, hallucinated metrics, and research misrepresentation.", table_cell_style)
        ]
    ]

    reg_table = Table(reg_data, colWidths=[140, 130, 234])
    reg_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#000000')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#000000')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e0e0e0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(reg_table)
    story.append(Spacer(1, 10))

    # Concluding Sign-off Box
    closing_text = (
        "<b>OFFICIAL ATTESTATION:</b><br/>"
        "This document constitutes the authoritative regulatory disclosure for Research Radar across all engineering disciplines. "
        "For governance inquiries, compliance audits, or data rights requests, contact the Research Radar Compliance Board "
        "at <b>compliance@researchradar.academic</b> or inspect the active institutional Salesforce repository."
    )
    closing_table = Table([[Paragraph(closing_text, body_style)]], colWidths=[504])
    closing_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f9f9f9')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#000000')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(closing_table)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"User Manual & Regulatory Compliance PDF generated successfully at: {filename}")

if __name__ == '__main__':
    target_path = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'RESEARCH_RADAR_USER_MANUAL_AND_REGULATORY_COMPLIANCE.pdf')
    target_path = os.path.abspath(target_path)
    create_manual_pdf(target_path)
