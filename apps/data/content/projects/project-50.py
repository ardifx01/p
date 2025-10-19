"""
Project #1: MLBB Username Finder
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: MLBB Username Finder
project_data = {
    "id": 1,
    "title": """Kodbox Filemanager""",
    "headline": """A sleek self-hosted file manager and cloud collaboration platform.""",
    "description": ['Kodbox is an open-source, web-based file management and cloud storage solution.', "It enables teams and individuals to upload, preview, organize, and share files securely from any browser.", 'Packed with advanced features like granular permissions, real-time collaboration, and online previews for documents, media, and code.'],
    "images": {
        "kodbox.jpg": f"{settings.PROJECT_BASE_IMG_URL}/kodbox.jpg"
    },
    "is_featured": False,
    "features": [{'title': 'Web-Based File Management', 'description': 'Drag-and-drop upload, preview, and organize files in a modern interface.'}, {'title': 'User & Permission Controls', 'description': 'Granular roles and access settings for teams and organizations.'}, {'title': 'Cross-Platform Deployment', 'description': 'Easily deploy on Linux, Docker, or cloud servers for flexible hosting.'}],
    "tech_stack": [
        SkillsData.tech_stack["php"],
        SkillsData.tech_stack["javascript"],
    ],
    "github_url": "https://github.com/ardifx01/kodbox",
    "demo_url": "",
    "status": "completed",
    "created_at": None,
    "updated_at": datetime.strptime("2025-09-05T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "File Management, Cloud, Collaboration",
    "tags": [
        "File Manager",
        "Kodbox",
        "Cloud Storage",
        "Self-Hosted",
        "Open Source",
        "Collaboration",
        "PHP",
        "Web App"
    ],
    "priority": 1,
    "slug": ""
}
