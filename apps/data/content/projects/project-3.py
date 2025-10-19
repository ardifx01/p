"""
Project #3: Zettlr 
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: Zettlr
project_data = {
    "id": 3, 
    "title": """Zettlr""",
    "headline": """A free, open-source Markdown editor and publication workbench for writers and researchers.""",
    "description": [
        "Zettlr is a cross-platform, free and open-source Markdown editor designed to support writers, scholars, and researchers throughout the entire writing lifecycle.",
        "It emphasizes privacy and local file ownership—no forced cloud synchronization or telemetry—while offering powerful citation and export capabilities.",
        "Ideal for note-taking, academic writing, and publication workflows, Zettlr integrates with reference managers and supports a wide range of export formats."
    ],
    "images": {
        "zettlr.png": f"{settings.PROJECT_BASE_IMG_URL}/zettlr.png"
    },
    "is_featured": False,
    "features": [
        {"title": "Privacy-First Markdown Editing", "description": "Work entirely offline with local files—no telemetry, no forced cloud sync."},
        {"title": "Citation & Reference Manager Integration", "description": "Seamlessly connect with Zotero, JabRef, Mendeley, and others for academic writing."},
        {"title": "Flexible Exporting & Templates", "description": "Export to PDF, HTML, DOCX, LaTeX, and more using Pandoc; supports custom templates."},
    ],
    "tech_stack": [
        SkillsData.tech_stack["typescript"],
        SkillsData.tech_stack["electron"],
	SkillsData.tech_stack["nodejs"],
    ],
    "github_url": "https://github.com/ardifx01/Zettlr",
    "demo_url": "",
    "status": "active",
    "created_at": None,
    "updated_at": datetime.strptime("2025-09-09T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "Markdown Editor, Academic Writing, Productivity",
    "tags": [
        "Markdown",
        "Writing",
        "Academic",
        "Citation",
        "Knowledge Management",
        "Open Source"
    ],
    "priority": 1,
    "slug": ""
}
