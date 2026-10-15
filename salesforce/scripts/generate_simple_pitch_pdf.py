#!/usr/bin/env python3
"""
Generate Plain-English, Simple 10-15 Minute Presentation Pitch PDF
Document: RESEARCH RADAR - Pitch Deck & Presentation Guide
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
            self.drawString(54, 750, "RESEARCH RADAR  |  10–15 Minute Project Pitch (Plain English)")
            self.drawRightString(letter[0] - 54, 750, "Presentation Script & Deck")
            self.setStrokeColor(colors.HexColor("#000000"))
            self.setLineWidth(0.75)
            self.line(54, 744, letter[0] - 54, 744)

        # Footer (all pages)
        self.setStrokeColor(colors.HexColor("#cccccc"))
        self.setLineWidth(0.5)
        self.line(54, 48, letter[0] - 54, 48)
        self.drawString(54, 36, "RESEARCH RADAR — CONFIDENTIAL PITCH GUIDE")
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(letter[0] - 54, 36, page_text)
        self.restoreState()

def create_pitch_pdf(filename):
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
        'PitchTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#000000'),
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'PitchSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#333333'),
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'SlideH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor('#000000'),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SlideH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#111111'),
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'PitchBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=colors.HexColor('#222222'),
        spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'PitchBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=11.5,
        textColor=colors.HexColor('#222222'),
        leftIndent=12,
        spaceAfter=3
    )

    hook_style = ParagraphStyle(
        'HookStyle',
        parent=styles['Normal'],
        fontName='Helvetica-BoldOblique',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#000000')
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
    story.append(Paragraph("10 to 15-Minute Pitch Deck & Presentation Script (Simple Words)", subtitle_style))
    
    hook_box = [
        [Paragraph("<b>THE ONE-SENTENCE HOOK:</b><br/><i>'Research Radar turns 3 months of painful research paper reading into 10 minutes of crystal-clear answers, side-by-side comparisons, and ready-to-run experiments.'</i>", hook_style)]
    ]
    t_hook = Table(hook_box, colWidths=[504])
    t_hook.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f5f5f5')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#000000')),
        ('LINEBEFORE', (0,0), (0,-1), 4, colors.HexColor('#000000')),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_hook)
    story.append(Spacer(1, 10))

    # -------------------------------------------------------------
    # SLIDE 1: INTRODUCTION & HOOK
    # -------------------------------------------------------------
    story.append(Paragraph("Slide 1: Introduction & The Core Question (1 Min)", h1_style))
    story.append(Paragraph(
        "<b>What to say:</b> 'Good morning/afternoon everyone. If you have ever had to write a project report, a thesis, or conduct an academic literature review, "
        "how much time did you waste downloading 50 PDFs, skimming 30-page papers, and manually copying numbers into an Excel spreadsheet? "
        "For almost every student and researcher, that process takes weeks or months. Today, we are presenting <b>Research Radar</b>—a smart cloud co-pilot "
        "that turns that entire painful process into a 2-second search.'",
        body_style
    ))
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # SLIDE 2: THE PROBLEM (3 HEADACHES)
    # -------------------------------------------------------------
    story.append(Paragraph("Slide 2: The Real-World Problem (2–3 Mins)", h1_style))
    story.append(Paragraph(
        "Why is academic research broken today? Every researcher suffers from 3 major headaches:",
        body_style
    ))
    story.append(Paragraph("1. <b>Information Overload:</b> Over 3 million peer-reviewed papers are published every year. Searching Google Scholar gives you 5,000 PDF links with no clue where to start.", bullet_style))
    story.append(Paragraph("2. <b>The 'Excel Spreadsheet' Nightmare:</b> Comparing numbers between papers requires opening 20 browser tabs and manually typing numbers into a spreadsheet. It is slow, tedious, and error-prone.", bullet_style))
    story.append(Paragraph("3. <b>ChatGPT Hallucinations:</b> Asking general AI models for research help is dangerous because AI frequently invents fake paper titles, fake authors, and made-up numbers that ruin academic credibility.", bullet_style))
    story.append(Paragraph("4. <b>Hidden Contradictions:</b> Paper A says an approach achieves 95% efficiency; Paper B tested it under real temperatures and found it fails completely. Researchers miss these contradictions until their own lab experiment fails.", bullet_style))
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # SLIDE 3: THE SOLUTION (RESEARCH RADAR)
    # -------------------------------------------------------------
    story.append(Paragraph("Slide 3: The Solution — What Research Radar Does (2 Mins)", h1_style))
    story.append(Paragraph(
        "Think of Research Radar as a <b>smart GPS for scientific knowledge</b> across all engineering branches (Computer Science, Mechanical, Civil, Electrical, Electronics, and Chemical):",
        body_style
    ))
    story.append(Paragraph("• <b>Instant Topic Maps:</b> Type any research question, and in 2 seconds it connects the relevant peer-reviewed papers into an organized topic map.", bullet_style))
    story.append(Paragraph("• <b>Side-by-Side Comparison Matrix:</b> Automatically places benchmark numbers side-by-side (like comparing phone specs on Amazon!).", bullet_style))
    story.append(Paragraph("• <b>100% Fact-Checked Evidence:</b> Every finding includes the exact verbatim quote and page number linked directly to the publisher's registered DOI.", bullet_style))
    story.append(Paragraph("• <b>Contradiction Spotter:</b> Instantly flags where two papers disagree so you don't repeat prior mistakes.", bullet_style))
    story.append(Paragraph("• <b>Research Gap Kanban Board:</b> Identifies what has NOT been solved yet, and provides a ready-to-test experiment protocol so researchers know what to do next.", bullet_style))
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # SLIDE 4: ARCHITECTURE & CLOUD ENGINE
    # -------------------------------------------------------------
    story.append(Paragraph("Slide 4: How We Solved It — Cloud Architecture (2 Mins)", h1_style))
    story.append(Paragraph(
        "Instead of building a fragile prototype on a local computer, we built Research Radar natively on the <b>Salesforce Lightning Platform (PaaS)</b>:",
        body_style
    ))
    story.append(Paragraph("• <b>Enterprise Cloud Reliability:</b> Runs on high-availability cloud infrastructure with zero server maintenance, automated backups, and 99.9% uptime.", bullet_style))
    story.append(Paragraph("• <b>Relational Data Integrity (ACID):</b> All 7 custom objects (Maps, Papers, Metrics, Quotes, Contradictions, Gaps) are relationally linked. When a paper is updated, all comparisons update automatically.", bullet_style))
    story.append(Paragraph("• <b>Fast Modern Interface:</b> Built with Lightning Web Components (LWC) using open web standards for instant browser performance and responsive design.", bullet_style))
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # SLIDE 5: LIVE DEMO WALKTHROUGH
    # -------------------------------------------------------------
    story.append(Paragraph("Slide 5: Live Demo Walkthrough (4–5 Mins)", h1_style))
    story.append(Paragraph(
        "During the live demo, showcase the 4 primary user experiences:",
        body_style
    ))
    story.append(Paragraph("1. <b>The Executive Dashboard:</b> Show the 4 KPI cards and demonstrate the branch filter buttons (All, Chemical, Mechanical, Civil, EEE, ECE).", bullet_style))
    story.append(Paragraph("2. <b>One-Click Topic Synthesis:</b> Type a topic (e.g. <i>'Serverless cold-start latency'</i>), click 'Generate Research Map', and watch the 4-step pipeline create a research map in 2 seconds.", bullet_style))
    story.append(Paragraph("3. <b>The Comparison Matrix:</b> Click 'Open Workspace' and show how benchmark numbers from multiple papers appear side-by-side cleanly.", bullet_style))
    story.append(Paragraph("4. <b>The Evidence Inspector:</b> Click a finding to show the verbatim quote, page number, and confidence score.", bullet_style))
    story.append(Paragraph("5. <b>The Gap Kanban Board:</b> Show how unsolved problems are turned into experiment cards that researchers can drag through validation stages.", bullet_style))
    story.append(Spacer(1, 6))

    # -------------------------------------------------------------
    # SLIDE 6: COMPETITOR COMPARISON
    # -------------------------------------------------------------
    story.append(Paragraph("Slide 6: Why Research Radar Beats Competitors (2 Mins)", h1_style))
    story.append(Paragraph(
        "How do we stand out against existing tools?",
        body_style
    ))

    comp_data = [
        [
            Paragraph("<b>Capability</b>", table_header_style),
            Paragraph("<b>Google Scholar</b>", table_header_style),
            Paragraph("<b>ChatGPT / AI</b>", table_header_style),
            Paragraph("<b>Connected Papers</b>", table_header_style),
            Paragraph("<b>Research Radar</b>", table_header_style)
        ],
        [
            Paragraph("<b>Gives Direct Answers</b>", table_cell_style),
            Paragraph("No (links only)", table_cell_style),
            Paragraph("Hallucinates fake data", table_cell_style),
            Paragraph("No (bubble graph only)", table_cell_style),
            Paragraph("<b>Yes (Fact-Checked)</b>", table_cell_style)
        ],
        [
            Paragraph("<b>Side-by-Side Comparison</b>", table_cell_style),
            Paragraph("No (manual Excel)", table_cell_style),
            Paragraph("No (unstructured text)", table_cell_style),
            Paragraph("No metrics extracted", table_cell_style),
            Paragraph("<b>Yes (Instant Matrix)</b>", table_cell_style)
        ],
        [
            Paragraph("<b>Spots Contradictions</b>", table_cell_style),
            Paragraph("No", table_cell_style),
            Paragraph("No", table_cell_style),
            Paragraph("No", table_cell_style),
            Paragraph("<b>Yes (Auto-Flagged)</b>", table_cell_style)
        ],
        [
            Paragraph("<b>Turns Gaps into Experiments</b>", table_cell_style),
            Paragraph("No", table_cell_style),
            Paragraph("No", table_cell_style),
            Paragraph("No", table_cell_style),
            Paragraph("<b>Yes (Kanban Board)</b>", table_cell_style)
        ],
        [
            Paragraph("<b>Audit Trail & Trust</b>", table_cell_style),
            Paragraph("Yes (PDF files)", table_cell_style),
            Paragraph("None (Zero proof)", table_cell_style),
            Paragraph("Yes (citations)", table_cell_style),
            Paragraph("<b>Yes (Quote & DOI link)</b>", table_cell_style)
        ]
    ]

    t_comp = Table(comp_data, colWidths=[110, 95, 105, 95, 99])
    t_comp.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#000000')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#000000')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e0e0e0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_comp)
    story.append(Spacer(1, 8))

    # -------------------------------------------------------------
    # SLIDE 7: CONCLUSION & SUMMARY
    # -------------------------------------------------------------
    story.append(Paragraph("Slide 7: Conclusion & Wrap-up (1 Min)", h1_style))
    story.append(Paragraph(
        "<b>Closing Statement:</b> 'Research drives human innovation—from electric vehicles to renewable energy and artificial intelligence. "
        "Yet researchers waste almost half their time doing repetitive manual reading, searching, and copying numbers into spreadsheets. "
        "Research Radar solves this problem with enterprise cloud computing, turning weeks of frustration into minutes of actionable discovery. "
        "Thank you, and we look forward to your questions!'",
        body_style
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Simple pitch PDF generated at: {filename}")

if __name__ == '__main__':
    target_path = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'RESEARCH_RADAR_SIMPLE_PITCH.pdf')
    target_path = os.path.abspath(target_path)
    create_pitch_pdf(target_path)
    # Also update RESEARCH_RADAR_PITCH_DOCUMENT.pdf
    pitch_doc_path = os.path.join(os.path.dirname(__file__), '..', '..', 'docs', 'RESEARCH_RADAR_PITCH_DOCUMENT.pdf')
    create_pitch_pdf(os.path.abspath(pitch_doc_path))
