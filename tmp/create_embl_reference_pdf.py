from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path("cvs/recommendation_letters")
PDF = ROOT / "Fatemeh_Torabi_EMBL_EBI_Software_Engineer_Data_Discovery_JR3882_Reference_Draft.pdf"

doc = SimpleDocTemplate(
    str(PDF),
    pagesize=A4,
    leftMargin=1.8 * cm,
    rightMargin=1.8 * cm,
    topMargin=1.65 * cm,
    bottomMargin=1.65 * cm,
)

styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="HeaderLeft",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=12,
        textColor=colors.HexColor("#263238"),
        alignment=TA_LEFT,
    )
)
styles.add(
    ParagraphStyle(
        name="HeaderRight",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=11,
        textColor=colors.HexColor("#37474F"),
        alignment=TA_RIGHT,
    )
)
styles.add(
    ParagraphStyle(
        name="Body",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10.2,
        leading=13.2,
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="BodyBold",
        parent=styles["Body"],
        fontName="Helvetica-Bold",
        spaceAfter=9,
    )
)
styles.add(
    ParagraphStyle(
        name="Signoff",
        parent=styles["Body"],
        fontName="Helvetica-Bold",
        spaceAfter=5,
    )
)

story = []
header = Table(
    [
        [
            Paragraph(
                "Dr Fatemeh Torabi<br/>"
                "Assistant Professor in Health Data Science and Senior Researcher<br/>"
                "University of Cambridge and Dementias Platform UK",
                styles["HeaderLeft"],
            ),
            Paragraph(
                "2 Parkhouse, 40 Queen Ediths Way<br/>"
                "Cambridge CB1 8PW, United Kingdom<br/>"
                "+44 7535 804266<br/>"
                "fatemeh.torabi@ice.cam.ac.uk",
                styles["HeaderRight"],
            ),
        ]
    ],
    colWidths=[9.2 * cm, 7.1 * cm],
)
header.setStyle(
    TableStyle(
        [
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("LINEBELOW", (0, 0), (-1, -1), 0.6, colors.HexColor("#90A4AE")),
        ]
    )
)
story.append(header)
story.append(Spacer(1, 12))

content = [
    ("[Date]", "Body"),
    (
        "Re: Recommendation for Alieyeh Sarabandi Moghaddam - Software Engineer, "
        "Data Discovery (JR3882), EMBL-EBI",
        "BodyBold",
    ),
    ("Dear Members of the Hiring Committee,", "BodyBold"),
    (
        "I am pleased to recommend Ms Alieyeh Sarabandi Moghaddam for the Software Engineer - "
        "Data Discovery position at EMBL-EBI. I have worked with Alieyeh as a research and writing "
        "supervisor within Dementias Platform UK (DPUK), and have come to know her as an intellectually "
        "curious, conscientious and technically strong colleague whose work sits naturally at the interface "
        "of biomedical data, software engineering and research infrastructure.",
        "Body",
    ),
    (
        "The focus of this role - integrating biological data and metadata, supporting FAIR discovery, "
        "and developing reliable software for a broad research community - is very well aligned with "
        "Alieyeh's strengths. In her current work she contributes to systems and workflows that make genomic, "
        "multi-omic and cohort resources more findable, interpretable and usable. She thinks carefully about "
        "identifiers, provenance, metadata completeness, terminology, data quality and the practical needs of "
        "researchers who must assess whether a dataset is suitable before formal access or analysis.",
        "Body",
    ),
    (
        "Our most substantial collaboration led to <i>Choosing the Right Genomic Dataset: A Five-Pillar "
        "Framework for Researchers</i>, published by <i>Real World Data Science</i> with Alieyeh as first "
        "author. She took a broad and technically complex topic and developed it into a practical framework "
        "spanning dataset discovery, governance, assay and technology choice, cohort design, quality control, "
        "harmonisation and research readiness. This work demonstrated her ability to synthesise evidence, "
        "identify the decisions that matter to research validity and communicate technical ideas clearly "
        "without losing precision.",
        "Body",
    ),
    (
        "Alieyeh's broader DPUK work gives her directly relevant experience for a data discovery platform. "
        "She has worked on reproducible genomic and multi-omic workflows, metadata and provenance, secure data "
        "processing, dataset validation and researcher-facing discovery and feasibility tooling. She has also "
        "designed and supervised work on omics metadata infrastructure, including domain modelling, standards-aware "
        "metadata, validation and search-oriented structures. Her BSc in Computer Engineering and MSc in Health "
        "Data Science allow her to move confidently between software implementation, data engineering, statistical "
        "analysis and biomedical interpretation.",
        "Body",
    ),
    (
        "I have been particularly impressed by the way Alieyeh approaches feedback and technical ambiguity. "
        "She listens closely, tests suggestions against the evidence, and revises with purpose rather than "
        "making superficial changes. She is also willing to question assumptions and defend a position when the "
        "scientific reasoning supports it. This balance of receptiveness and independence is important for a "
        "software engineer working in an established, collaborative codebase where design decisions must serve "
        "long-term maintainability and user needs.",
        "Body",
    ),
    (
        "I recommend Alieyeh with confidence for the Software Engineer - Data Discovery role. She would "
        "bring strong analytical ability, research maturity, biomedical metadata insight, clear communication "
        "and a collaborative engineering mindset to EMBL-EBI. I expect her to make a thoughtful and valuable "
        "contribution to EBI Search and to the continued development of data discovery services for the "
        "international research community.",
        "Body",
    ),
    ("Yours faithfully,", "Signoff"),
    ("Dr Fatemeh Torabi", "Signoff"),
    (
        "Assistant Professor in Health Data Science and Senior Researcher<br/>"
        "University of Cambridge and Dementias Platform UK",
        "Body",
    ),
]

for text, style in content:
    story.append(Paragraph(text, styles[style]))

doc.build(story)
print(PDF)
