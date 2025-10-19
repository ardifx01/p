"""
Project #44: karimunkab.go.id
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: GetStage
project_data = {
    "id": 44,
    "title": """KarimunKab""",
    "headline": """Official government website for Kabupaten Karimun, powered by Laravel""",
    "description": ['KarimunKab is a government web platform developed to provide information and digital public services for Kabupaten Karimun.', "It includes landing pages, OPD (Organisasi Perangkat Daerah) news, and integrated document previews.", 'The system is designed to improve transparency, accessibility, and ease of use for citizens and administrators alike.'],
    "images": {
        "karimunkab.jpg": f"{settings.PROJECT_BASE_IMG_URL}/karimunkab.jpg"
    },
    "is_featured": True,
    "features": [{'title': 'Landing Page with Search', 'description': 'Homepage equipped with a functional search box and links to OPD content.'}, {'title': 'Dynamic Content', 'description': 'News, documents, and public information published by each OPD.'}, {'title': 'Admin Panel', 'description': 'Customizable admin interface with dynamic logo and content management tools.'}],
    "tech_stack": [
        SkillsData.tech_stack["laravel"],
        SkillsData.tech_stack["php"],
        SkillsData.tech_stack["css3"],

    ],
    "github_url": "https://github.com/ardifx01/karimunkab",
    "demo_url": "https://karimunkab.go.id",
    "status": "completed",
    "created_at": None,
    "updated_at": datetime.strptime("2025-09-05T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "Ticketing, Events, Concerts",
    "tags": [
        "Laravel",
        "PHP",
        "Government",
        "Public Service",
        "Website",
        "SEO"
    ],
    "priority": 1,
    "slug": ""
}
