"""
Project #42: LetMeCook Landing Page 
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: LetMeCook Landing Page
project_data = {
    "id": 42, 
    "title": "LetMeCook Landing Page",
    "headline": "Landing page modern untuk platform resep masakan berbasis komunitas.",
    "description": [
        "Halaman depan responsif yang dirancang untuk platform LetMeCook — komunitas berbagi resep, tips masak, dan video tutorial.",
        "Menampilkan modul-hero dengan ajakan bergabung, grid resep unggulan, testimoni pengguna, dan footer dengan langganan newsletter.",
        "Fokus pada UI/UX bersih dan visual appetising untuk menarik pengunjung baru serta meningkatkan konversi pengguna aktif."
    ],
    "images": {
        "letmecook_landing.jpg": f"{settings.PROJECT_BASE_IMG_URL}/letmecook_landing.jpg"
    },
    "is_featured": False,
    "features": [
        {"title": "Hero Section & Call to Action", "description": "Bagian atas halaman dengan gambar makanan besar, tombol ‘Gabung Sekarang’, dan highlight keunggulan komunitas."},
        {"title": "Grid Resep Unggulan", "description": "Tampilan foto resep dengan judul, deskripsi singkat, dan tombol ‘Lihat Resep’."},
        {"title": "Testimoni & Newsletter", "description": "Bagian testimoni pengguna dan form langganan newsletter di footer untuk meningkatkan engagement."}
    ],
    "tech_stack": [
        SkillsData.tech_stack["html5"],
        SkillsData.tech_stack["css3"],
        SkillsData.tech_stack["bootstrap"],
        SkillsData.tech_stack["javascript"]
    ],
    "github_url": "https://github.com/ardifx01/letmecook-landing-page",
    "demo_url": "",
    "status": "completed",
    "created_at": None,
    "updated_at": datetime.strptime("2025-10-24T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "Landing Page, UI/UX, Frontend",
    "tags": [
        "Landing Page",
        "Resep Masakan",
        "Komunitas",
        "Bootstrap",
        "Frontend",
        "UI/UX"
    ],
    "priority": 2,
    "slug": ""
}

