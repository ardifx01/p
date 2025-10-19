"""
Project #49: SistemInformasiPengelolanAset
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: GetStage
project_data = {
    "id": 48,
    "title": """Sistem Informasi Pengelolan Aset""",
    "headline": """Web-based asset management system with Laravel & Filament Admin Panel""",
    "description": ['Aplikasi ini merupakan sistem informasi untuk mengelola aset perusahaan berbasis web.', "Memfasilitasi pencatatan, pelacakan, pengajuan, dan transfer aset antar cabang.", 'Menggunakan Laravel dengan Filament Admin Panel dan MySQL untuk backend-data yang aman dan terstruktur.'],
    "images": {
        "pengelolaan_aset.jpg": f"{settings.PROJECT_BASE_IMG_URL}/pengelolaan_aset.jpg"
    },
    "is_featured": False,
    "features": [{'title': 'Kelola Aset (Barang)', 'description': 'CRUD data barang/aset perusahaan agar tercatat dan terkelola dengan baik.'}, {'title': 'Kelola Cabang & User', 'description': 'Manajemen cabang perusahaan dan user sesuai peran: GA (pusat) dan PIC (per cabang).'}, {'title': 'Request & Transfer Barang', 'description': 'Customizable admin interface with dynamic logo and content management tools.'}],
    "tech_stack": [
        SkillsData.tech_stack["laravel"],
        SkillsData.tech_stack["php"],
        SkillsData.tech_stack["mysql"],

    ],
    "github_url": "https://github.com/ardifx01/sistem-informasi-pengelolan-aset",
    "demo_url": "",
    "status": "completed",
    "created_at": None,
    "updated_at": datetime.strptime("2025-09-05T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "Asset Management, Internal Tools, Company System",
    "tags": [
        "Laravel",
        "Filament",
        "Asset Management",
        "MySQL",
        "Web App"
    ],
    "priority": 1,
    "slug": ""
}
