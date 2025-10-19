"""
Project #7: Scalar 
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: Scalar
project_data = {
    "id": 7, 
    "title": """Scalar""",
    "headline": """An open-source, offline-first API client and documentation platform for OpenAPI.""",
    "description": [
        "Scalar is an open-source API platform built for developers to explore and document APIs.",
        "It functions as a modern REST API client with first-class OpenAPI/Swagger support and beautiful interactive API references.",
        "Offline-ready and framework-agnostic, it integrates seamlessly with many backend stacks and provides a polished developer experience."
    ],
    "images": {
        "svg": f"{settings.PROJECT_BASE_IMG_URL}/scalar.svg"
    },
    "is_featured": False,
    "features": [
        {"title": "Offline-First API Client", "description": "Work with APIs even when disconnected; seamless developer workflows."},
        {"title": "Beautiful API References", "description": "Generates modern, interactive API docs with full OpenAPI/Swagger compatibility."},
        {"title": "Wide Integrations", "description": "Supports frameworks like FastAPI, Django, Node.js frameworks, Rust, and more."}
    ],
    "tech_stack": [
        SkillsData.tech_stack["typescript"],
        SkillsData.tech_stack["vuejs"],
        SkillsData.tech_stack["python"],
    ],
    "github_url": "https://github.com/ardifx01/scalar",
    "demo_url": "",
    "status": "active",
    "created_at": None,
    "updated_at": datetime.strptime("2025-09-09T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "API Client, Documentation, Developer Tooling",
    "tags": [
        "API Client",
        "OpenAPI",
        "Documentation",
        "Offline First",
        "Developer Tools",
        "Open Source"
    ],
    "priority": 1,
    "slug": ""
}
