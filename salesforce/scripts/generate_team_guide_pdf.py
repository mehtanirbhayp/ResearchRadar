#!/usr/bin/env python3
"""
Generate publication-grade PDF for:
RESEARCH RADAR — Complete Team Master Guide & Technical Project Handbook
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
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#444444"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 750, "RESEARCH RADAR  |  Complete Team Master Guide & Technical Handbook")
            self.drawRightString(letter[0] - 54, 750, "Doc Ref: RR-TEAM-GUIDE-2026")
            self.setStrokeColor(colors.HexColor("#000000"))
            self.setLineWidth(0.75)
            self.line(54, 744, letter[0] - 54, 744)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#cccccc"))
        self.setLineWidth(0.5)
        self.line(54, 48, letter[0] - 54, 48)
        self.drawString(54, 36, "CONFIDENTIAL & PROPRIETARY  —  RESEARCH RADAR TEAM ONBOARDING")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 54, 36, page_text)
        self.restoreState()

def create_team_guide_pdf(filename):
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
    
    title_style = ParagraphStyle(
        'GuideTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#000000'),
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'GuideSubtitle',
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
        spaceBefore=11,
        spaceAfter=5,
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
    # COVER / HEADER
    # -------------------------------------------------------------
    story.append(Paragraph("RESEARCH RADAR", title_style))
    story.append(Paragraph("Complete Team Master Guide & Technical Project Handbook", subtitle_style))
    
    meta_table_data = [
        [
            Paragraph("<b>DOCUMENT REF:</b> RR-TEAM-GUIDE-2026", meta_style),
            Paragraph("<b>EFFECTIVE DATE:</b> October 2026", meta_style),
            Paragraph("<b>PLATFORM:</b> Salesforce Lightning PaaS", meta_style)
        ],
        [
            Paragraph("<b>TARGET ORG:</b> trailheadOrg (Developer Edition)", meta_style),
            Paragraph("<b>ARCHITECTURE:</b> 7 Relational Custom Objects", meta_style),
            Paragraph("<b>TEST COVERAGE:</b> 100% Apex Pass Rate (7/7)", meta_style)
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

    # Executive Summary Box
    exec_text = (
        "<b>PURPOSE OF THIS HANDBOOK:</b> This document gives our entire development and presentation team a complete, detailed understanding "
        "of Research Radar: what problem it solves, how it is built on Salesforce Cloud, the exact database schema, all UI components, "
        "how to demonstrate it to evaluators, and how to answer tough viva/defense questions."
    )
    exec_table = Table([[Paragraph(exec_text, callout_style)]], colWidths=[504])
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
    # SECTION 1: THE BIG IDEA IN 2 MINUTES
    # -------------------------------------------------------------
    story.append(Paragraph("1. Executive Summary: What is This Project in 2 Minutes?", h1_style))
    story.append(Paragraph(
        "Imagine you are starting your final year project, writing a research paper, or exploring a new engineering topic. "
        "Doing an academic literature review today is exhausting: researchers search Google Scholar, get 5,000 PDFs, spend weeks reading 30-page documents, "
        "and manually copy numbers into an Excel spreadsheet. If two papers contradict each other, they rarely notice until their experiment fails. "
        "And if they ask ChatGPT, it hallucinates fake papers and made-up numbers.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Research Radar solves this:</b> It is an intelligent research co-pilot. You enter any engineering topic (Computer Science, Mechanical, Civil, Electrical, Electronics, or Chemical). "
        "In 2 seconds, it connects real peer-reviewed papers into an interactive topic map, places benchmark metrics side-by-side in a comparison table, "
        "flags scientific contradictions, and gives you an actionable research gap protocol on a Kanban board so you can start experiments immediately.",
        body_style
    ))
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # SECTION 2: WHY SALESFORCE CLOUD PAAS?
    # -------------------------------------------------------------
    story.append(Paragraph("2. Why Did We Build It on Salesforce Cloud (PaaS)?", h1_style))
    story.append(Paragraph(
        "When professors or evaluators ask why we used Salesforce instead of a generic MERN or Python stack, here is the architectural rationale:",
        body_style
    ))
    story.append(Paragraph("• <b>Zero Infrastructure Hassle:</b> No need to provision AWS servers, configure Linux packages, or worry about crashes. Salesforce handles cloud hosting, scaling, and backups automatically.", bullet_style))
    story.append(Paragraph("• <b>Relational ACID Data Integrity:</b> Research data must never have orphaned records. By using Master-Detail relationships, deleting a paper automatically cascades to its extracted metrics and findings.", bullet_style))
    story.append(Paragraph("• <b>Native Validation & Roll-Ups:</b> Database rules enforce valid DOIs (must start with '10.') and publication years (1950–2026), while roll-up summary fields calculate totals in real time with zero CPU latency.", bullet_style))
    story.append(Paragraph("• <b>Lightning Web Components (LWC):</b> Built on standard W3C Web Components and Shadow DOM, giving native browser speed without bloated client libraries.", bullet_style))
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # SECTION 3: DATABASE SCHEMA (ALL 7 OBJECTS)
    # -------------------------------------------------------------
    story.append(Paragraph("3. The Database Schema: All 7 Custom Objects Explained", h1_style))
    story.append(Paragraph(
        "Our database consists of 7 custom Salesforce objects connected via relational links:",
        body_style
    ))

    schema_data = [
        [
            Paragraph("<b>Object API Name</b>", table_header_style),
            Paragraph("<b>Type / Relationship</b>", table_header_style),
            Paragraph("<b>Key Fields & Data Stored</b>", table_header_style),
            Paragraph("<b>Business Purpose</b>", table_header_style)
        ],
        [
            Paragraph("<b>Research_Map__c</b>", table_cell_style),
            Paragraph("Primary Parent", table_cell_style),
            Paragraph("Topic__c, Target_Discipline__c, Status__c, Total_Papers__c, Total_Findings__c", table_cell_style),
            Paragraph("Represents the synthesized research domain / cluster", table_cell_style)
        ],
        [
            Paragraph("<b>Research_Paper__c</b>", table_cell_style),
            Paragraph("Primary Parent", table_cell_style),
            Paragraph("Name, Authors__c, Journal__c, Publication_Year__c, DOI__c, Citations__c, BibTeX", table_cell_style),
            Paragraph("Catalog of peer-reviewed scientific publications", table_cell_style)
        ],
        [
            Paragraph("<b>Research_Map_Paper_Link__c</b>", table_cell_style),
            Paragraph("Junction Object", table_cell_style),
            Paragraph("Research_Map__c (MD), Research_Paper__c (MD), Relevance_Score__c", table_cell_style),
            Paragraph("Many-to-many link between research topics and papers", table_cell_style)
        ],
        [
            Paragraph("<b>Extracted_Metric__c</b>", table_cell_style),
            Paragraph("Child (Master-Detail)", table_cell_style),
            Paragraph("Metric_Name__c, Value__c, Unit__c, Test_Conditions__c, Research_Paper__c", table_cell_style),
            Paragraph("Numerical benchmark results extracted from papers", table_cell_style)
        ],
        [
            Paragraph("<b>Research_Finding__c</b>", table_cell_style),
            Paragraph("Child (Master-Detail)", table_cell_style),
            Paragraph("Claim_Summary__c, Verbatim_Quote__c, Page_Number__c, Confidence_Score__c", table_cell_style),
            Paragraph("Verbatim empirical evidence with page audit trail", table_cell_style)
        ],
        [
            Paragraph("<b>Research_Conflict__c</b>", table_cell_style),
            Paragraph("Lookup Object", table_cell_style),
            Paragraph("Contradiction_Summary__c, Paper_A__c, Paper_B__c, Severity__c", table_cell_style),
            Paragraph("Flags direct scientific contradictions between papers", table_cell_style)
        ],
        [
            Paragraph("<b>Research_Gap__c</b>", table_cell_style),
            Paragraph("Child (Master-Detail)", table_cell_style),
            Paragraph("Question__c, Proposed_Validation_Experiment__c, Status__c", table_cell_style),
            Paragraph("Unsolved research questions & experimental protocols", table_cell_style)
        ]
    ]

    t_schema = Table(schema_data, colWidths=[110, 85, 175, 134])
    t_schema.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#000000')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#000000')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e0e0e0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_schema)
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # SECTION 4: ALL FEATURES & UI WALKTHROUGH
    # -------------------------------------------------------------
    story.append(Paragraph("4. All Platform Features & UI Components", h1_style))
    story.append(Paragraph("• <b>Executive Dashboard (ereunaDashboardHome):</b> Real-time metric cards, full-width research topic table, and a dedicated top-bar operational menu for immediate manual access.", bullet_style))
    story.append(Paragraph("• <b>Literature Synthesis Engine (ereunaTopicSearch):</b> Allows entering any research query across CS, Mechanical, Civil, EEE, ECE, or Chemical Engineering, executing a 4-step synthesis pipeline in 2 seconds.", bullet_style))
    story.append(Paragraph("• <b>Literature Comparison Matrix (literatureCompareMatrix):</b> Side-by-side benchmark comparison matrix normalizing metrics across papers without opening spreadsheets.", bullet_style))
    story.append(Paragraph("• <b>Evidence Inspector (findingsExplorer):</b> Displays verbatim quotes with exact page numbers, confidence percentages, and methodology tags.", bullet_style))
    story.append(Paragraph("• <b>Research Gap Kanban Board (gapKanbanBoard):</b> Drag-and-drop tracker shepherding unsolved problems across 4 lifecycle stages: Identified -> In Review -> Experiment Drafted -> Addressed.", bullet_style))
    story.append(Paragraph("• <b>User Manual & Governance Tab (governanceManualView):</b> Full-page documentation tab directly on the Salesforce navigation bar with downloadable PDF resources.", bullet_style))
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # SECTION 5: HOW TO RUN & DEMO (3-MINUTE SCRIPT)
    # -------------------------------------------------------------
    story.append(Paragraph("5. Step-by-Step Live Demo Script for Presentations", h1_style))
    story.append(Paragraph(
        "Follow this exact 3-minute sequence when presenting to examiners or judges:",
        body_style
    ))
    story.append(Paragraph("1. <b>App Launcher:</b> Click the 9 dots in Salesforce, select 'Research Radar'. Show the clean, high-contrast monochrome dashboard.", bullet_style))
    story.append(Paragraph("2. <b>Discipline Filter:</b> Click 'Chemical', 'Mechanical', or 'Civil' filter pills in the topics table to show multi-branch versatility.", bullet_style))
    story.append(Paragraph("3. <b>Synthesize:</b> In the synthesis bar, type <i>'Serverless cold-start latency'</i> and click 'Generate Research Map'. Show the progress animation.", bullet_style))
    story.append(Paragraph("4. <b>Comparison Matrix:</b> Click 'Open Workspace ->' to show benchmark numbers from multiple papers side-by-side.", bullet_style))
    story.append(Paragraph("5. <b>Verified Evidence:</b> Click any finding to prove that verbatim quotes and DOI page numbers prevent AI hallucinations.", bullet_style))
    story.append(Paragraph("6. <b>Gap Board & Manual:</b> Show the Kanban board turning gaps into experiments, and point out the top-bar 'User Manual & Legal' tab.", bullet_style))
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # SECTION 6: VIVA & DEFENSE QUESTIONS
    # -------------------------------------------------------------
    story.append(Paragraph("6. Common Viva Questions & Winning Answers", h1_style))
    story.append(Paragraph(
        "<b>Q1: Why not just use Google Scholar?</b><br/>"
        "<i>Answer:</i> Google Scholar only returns links to PDFs. You still have to spend weeks reading them and making spreadsheets. "
        "Research Radar extracts the numbers, compares them side-by-side, flags contradictions, and identifies unsolved research gaps automatically.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Q2: Why not just ask ChatGPT?</b><br/>"
        "<i>Answer:</i> LLMs hallucinate fake citations, wrong numbers, and non-existent authors. Research Radar uses a deterministic relational database where every finding links directly to a publisher DOI with exact page numbers.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Q3: What prevents bad data from corrupting the database?</b><br/>"
        "<i>Answer:</i> Native Salesforce Validation Rules on the database layer reject invalid DOIs (must start with '10.') and out-of-range publication years, even if incoming APIs send bad inputs.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Q4: What happens when a paper is deleted?</b><br/>"
        "<i>Answer:</i> Master-Detail relationships automatically cascade-delete linked metrics and findings, maintaining 100% referential integrity with zero orphaned data.",
        body_style
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Team Guide PDF generated at: {filename}")

if __name__ == '__main__':
    target_path = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'RESEARCH_RADAR_TEAM_PROJECT_GUIDE.pdf')
    target_path = os.path.abspath(target_path)
    create_team_guide_pdf(target_path)
