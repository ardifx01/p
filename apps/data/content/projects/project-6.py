"""
Project #6: Hyperswitch 
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: Hyperswitch
project_data = {
    "id": 6, 
    "title": """Hyperswitch""",
    "headline": """An open-source, high-performance payments switch written in Rust.""",
    "description": [
        "Hyperswitch is a modular payments infrastructure that lets businesses connect to multiple payment processors via a unified API.",
        "It supports features like intelligent routing, retry strategies, card vaulting, cost observability, reconciliation, and flexible orchestration.",
        "Built for scale and performance, it’s designed to reduce vendor lock-in and streamline integration across global payment methods."
    ],
    "images": {
        "hyperswitch.png": f"{settings.PROJECT_BASE_IMG_URL}/hyperswitch.png"
    },
    "is_featured": False,
    "features": [
        {"title": "Unified Payments API", "description": "Abstracts multiple PSPs behind a single API interface."},
        {"title": "Intelligent Routing & Retry", "description": "Optimize for cost and success with smart fallback logic."},
        {"title": "PCI-Compliant Vaulting", "description": "Securely store and reuse payment credentials across merchants."}
    ],
    "tech_stack": [
        SkillsData.tech_stack["rust"],
        SkillsData.tech_stack["postgresql"],
        SkillsData.tech_stack["docker"], 
    ],
    "github_url": "https://github.com/ardifx01/hyperswitch", 
    "demo_url": "",
    "status": "active",
    "created_at": None,
    "updated_at": datetime.strptime("2025-08-11T00:00:00+00:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "Payments, Microservices, Fintech",
    "tags": [
        "Rust",
        "Payments",
        "Open Source",
        "Fintech",
        "Gateway",
        "Infrastructure"
    ],
    "priority": 1,
    "slug": ""
}
