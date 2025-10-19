"""
Project #4: Justnote-Client 
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: Justnote-Client
project_data = {
    "id": 4, 
    "title": """Justnote-Client""",
    "headline": """A simple, fast, privacy-focused cross-platform note-taking app.""",
    "description": [
        "Justnote-Client is part of Justnote, a privacy-focused note-taking application designed to give users full control and ownership of their data.",
        "Features include end-to-end encryption, nested lists, tags, pin-to-top, ability to lock notes or lists, dark mode, and support across web, Android, and iOS platforms.",
        "Built with a focus on speed and usability, it emphasizes user privacy without sacrificing functionality."
    ],
    "images": {
        "justnote-client.png": f"{settings.PROJECT_BASE_IMG_URL}/justnote-client.png",
    },
    "is_featured": False,
    "features": [
        {"title": "End-to-End Encryption", "description": "Your notes are encrypted locally—only you can decrypt them."},
        {"title": "Cross-Platform", "description": "Available on the web, Android, and iOS for seamless note access."},
        {"title": "Rich Usability Features", "description": "Includes nested lists, tags, pinning, locking notes/lists, and dark mode for an enhanced UX."}
    ],
    "tech_stack": [
        SkillsData.tech_stack["reactnative"],  
        SkillsData.tech_stack["redux"],
        SkillsData.tech_stack["ckeditor"], 
    ],
    "github_url": "https://github.com/ardifx01/justnote-client", 
    "demo_url": "https://justnote.cc",
    "status": "active",
    "created_at": None,
    "updated_at": datetime.strptime("2025-09-09T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "Note-Taking, Privacy, Productivity",
    "tags": [
        "Privacy",
        "E2EE",
        "Note-Taking",
        "Cross-Platform",
        "React",
        "Mobile App",
        "Web App"
    ],
    "priority": 1,
    "slug": ""
}
