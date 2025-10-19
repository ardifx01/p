"""
Project #2: Docmost
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: Docmost
project_data = {
    "id": 2,
    "title": """Docmost""",
    "headline": """A modern open-source collaborative documentation platform.""",
    "description": [
        "Docmost is an open-source, self-hosted documentation and knowledge-sharing platform.",
        "It allows teams and individuals to write, organize, and collaborate on docs in real time.",
        "With a clean interface and flexible permissions, Docmost makes it easy to build internal wikis, project docs, or knowledge bases."
    ],
    "images": {
        "docmost.jpg": f"{settings.PROJECT_BASE_IMG_URL}/docmost.jpg"
    },
    "is_featured": False,
    "features": [
        {"title": "Collaborative Editing", "description": "Multiple users can write and edit documentation simultaneously in real time."},
        {"title": "Structured Organization", "description": "Organize docs into workspaces, categories, and projects for easy navigation."},
        {"title": "Self-Hosted & Open Source", "description": "Deploy on your own server for full control and customization."}
    ],
    "tech_stack": [
        SkillsData.tech_stack["nextjs"],
        SkillsData.tech_stack["typescript"],
        SkillsData.tech_stack["tailwindcss"],
        SkillsData.tech_stack["postgresql"],
    ],
    "github_url": "https://github.com/ardifx01/docmost",
    "demo_url": "",
    "status": "in-progress",
    "created_at": None,
    "updated_at": datetime.strptime("2025-09-09T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "Documentation, Collaboration, Knowledge Base",
    "tags": [
        "Documentation",
        "Wiki",
        "Knowledge Base",
        "Collaboration",
        "Open Source",
        "Next.js"
    ],
    "priority": 1,
    "slug": ""
}
