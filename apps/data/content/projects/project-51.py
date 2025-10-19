"""
Project #51: GoStage
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: GetStage
project_data = {
    "id": 1,
    "title": """GoStage""",
    "headline": """A modern concert ticketing platform built with Next.js.""",
    "description": ['GetStage is a web-based ticketing solution designed for concerts, festivals, and live events.', "It allows users to browse events, view details, and purchase tickets seamlessly with a secure checkout process.", 'The platform provides event organizers with a modern interface for managing ticket sales and promoting shows online.'],
    "images": {
        "gostage.jpg": f"{settings.PROJECT_BASE_IMG_URL}/gostage.jpg"
    },
    "is_featured": False,
    "features": [{'title': 'Concert Ticket Sales', 'description': 'A seamless ticket purchasing experience for users with instant confirmation.'}, {'title': 'Event Listings', 'description': 'Browse upcoming concerts, festivals, and shows with detailed event pages.'}, {'title': 'Secure Checkout', 'description': 'Integrated payment gateway for safe and reliable transactions.'}],
    "tech_stack": [
        SkillsData.tech_stack["nextjs"],
        SkillsData.tech_stack["typescript"],
        SkillsData.tech_stack["tailwindcss"],
        SkillsData.tech_stack["postgresql"],

    ],
    "github_url": "https://github.com/ardifx01/getstage",
    "demo_url": "https://gostage.mnkdigital.tech/",
    "status": "completed",
    "created_at": None,
    "updated_at": datetime.strptime("2025-09-05T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "Ticketing, Events, Concerts",
    "tags": [
        "Ticketing",
        "Concert",
        "Event Management",
        "Next.js",
        "TailwindCSS",
        "Web App"
    ],
    "priority": 1,
    "slug": ""
}
