"""
Project #43: Kodbox Filemanager
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: BeliMadu.com
project_data = {
    "id": 43,
    "title": """Kodbox Filemanager""",
    "headline": """Self-hosted file management and collaboration platform.""",
    "description": ['Kodbox is an open-source, web-based file manager.', 'It supports file sharing, permission management, and online editing.'],
    "images": {
        "belimadu_com.webp": f"{settings.PROJECT_BASE_IMG_URL}/kodbox.webp"
    },
    "is_featured": True,
    "features": [{'title': "File Sharing", 'description': 'Share files with links and permissions.'}, {'title': 'Cross-Platform', 'description': 'Deployable on Linux, Windows, or Docker.'}],
    "tech_stack": [
        SkillsData.tech_stack["php"],
        SkillsData.tech_stack["mysql"],
        SkillsData.tech_stack["javascript"],
        SkillsData.tech_stack["html"]
    ],
    "github_url": "https://github.com/ardifx01/kodbox",
    "demo_url": "",
    "status": "completed",
    "created_at": None,
    "updated_at": datetime.strptime("2025-04-16T21:51:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "File Management",
    "tags": ["filemanager", "php", "cloud-storage", "self-hosted", "document-management", "collaboration", "open-source"],
    "priority": 1,
    "slug": ""
}
