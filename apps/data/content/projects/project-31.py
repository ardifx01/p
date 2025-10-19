"""
Project #31: Kodbox Filemanager  
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: Kodbox Filemanager
project_data = {
    "id": 31,
    "title": """Kodbox Filemanager""",
    "headline": """A modern, self-hosted file management and collaboration platform built with PHP, designed to be a lightweight alternative to commercial cloud storage.""",
    "description": [
        "Kodbox is an open-source, web-based file manager and cloud storage platform.",
        "It enables individuals and teams to securely upload, preview, organize, and share files directly from a browser.",
        "The system supports user management, roles, and permissions, making it suitable for personal and business use.",
        "Built on PHP, it can be deployed on Linux, Windows, or Docker environments, offering flexibility and scalability.",
        "Kodbox provides a cost-effective and customizable solution for file storage, collaboration, and document management."
    ],
    "images": {
        "kodbox_preview.webp": f"{settings.PROJECT_BASE_IMG_URL}/kodbox.jpg",
        # "kodbox.webp": f"{settings.PROJECT_BASE_IMG_URL}/kodbox.webp"
    },
    "is_featured": True,
    "features": [
        {
            "title": "Web-Based File Manager",
            "description": "Upload, preview, rename, and organize files with a clean and responsive browser interface."
        },
        {
            "title": "User & Permission Management",
            "description": "Support for multiple users, roles, and fine-grained access control to files and folders."
        },
        {
            "title": "Collaboration Tools",
            "description": "Share files or folders with links, set expiration dates, and manage read/write permissions."
        },
        {
            "title": "Multi-Platform Deployment",
            "description": "Deployable on PHP servers across Linux, Windows, or Docker environments."
        }
    ],
    "tech_stack": [
        SkillsData.tech_stack["php"],
        SkillsData.tech_stack["mysql"],
        SkillsData.tech_stack["javascript"],
        SkillsData.tech_stack["html"],
        SkillsData.tech_stack["css"]
    ],
    "github_url": "https://github.com/ardifx01/kodbox",
    "demo_url": "",
    "status": "completed",
    "created_at": datetime.strptime("2025-09-02T15:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-09-02T15:10:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "productivity",
    "tags": ["filemanager", "cloud-storage", "php", "self-hosted", "open-source", "collaboration", "document-management"],
}
