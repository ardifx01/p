"""
Project #37: SistemPenggajian
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: GetStage
project_data = {
    "id": 37,
    "title": """Sistem Manajemen Perusahaan Terpadu""",
    "headline": """An integrated operational management platform for distribution, logistics, and manufacturing companies""",
    "description": ['This system provides end-to-end operational management designed to improve efficiency, transparency, and scalability in business operations.', "Modules include purchase orders, invoices, route management, financial reporting, human resources, and payroll.", 'Built with Laravel, TailwindCSS, Alpine.js, and MySQL, with responsive design and modern performance optimizations.'],
    "images": {
        "company_management_system.jpg": f"{settings.PROJECT_BASE_IMG_URL}/company_management_system.jpg"
    },
    "is_featured": False,
    "features": [{'title': 'Integrated Business Modules', 'description': 'From PO to delivery notes, invoice to payroll—all in one unified platform.'}, {'title': 'Finance & Reporting', 'description': 'Detailed revenue, expense tracking, profit analysis, and exportable reports.'}, {'title': 'HR & Payroll', 'description': 'Employee attendance, payroll generation, and performance tracking.'}],
    "tech_stack": [
        SkillsData.tech_stack["laravel"],
        SkillsData.tech_stack["php"],
        SkillsData.tech_stack["mysql"],
        SkillsData.tech_stack["tailwindcss"],

    ],
    "github_url": "https://github.com/ardifx01/Manajemen-perusahaan",
    "demo_url": "",
    "status": "completed",
    "created_at": None,
    "updated_at": datetime.strptime("2025-09-20T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "Enterprise Resource Planning, Operations, Logistics",
    "tags": [
        "Laravel",
        "ERP",
        "Logistics",
        "Finance",
        "HR",
        "Supply Chain"
    ],
    "priority": 1,
    "slug": ""
}
