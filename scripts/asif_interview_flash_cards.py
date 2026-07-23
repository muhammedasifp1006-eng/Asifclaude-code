"""Generate Asif's interview flash cards PDF.

This script writes a small PDF that can be used for interview preparation.
By default it matches the requested output path under /mnt/data, but a custom
path can be supplied as the first CLI argument.
"""

from __future__ import annotations

import sys
from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate


DEFAULT_OUTPUT = Path("/mnt/data/Asif_Interview_Flash_Cards.pdf")

CARDS = [
    ("Tell me about yourself", "ME → Diploma → Certifications → MIRTH GROUP → Quick Learner"),
    ("Digital Marketing", "ONLINE promotion"),
    ("SEO", "Google ranking"),
    ("Google Ads", "Paid ads"),
    ("Social Media", "Facebook Instagram LinkedIn"),
    ("Hire You", "Hardworking • Honest • Quick learner"),
    ("Why this job", "Learn • Grow • Contribute"),
    ("Strength", "Responsible • Team player"),
    ("Weakness", "Always improving"),
    (
        "Don't know answer",
        "I haven't worked on that directly yet, but I'm learning quickly.",
    ),
]


def build_flash_cards(output_path: Path = DEFAULT_OUTPUT) -> None:
    """Build the interview flash cards PDF at the given path."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(str(output_path))
    story = [Paragraph("<b>ASIF INTERVIEW FLASH CARDS</b>", styles["Title"])]

    for question, answer in CARDS:
        story.append(Paragraph(f"<b>Q:</b> {question}", styles["Heading2"]))
        story.append(Paragraph(f"<b>A:</b> {answer}", styles["BodyText"]))

    doc.build(story)


def main() -> None:
    output_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUTPUT
    build_flash_cards(output_path)
    print("ok")


if __name__ == "__main__":
    main()
