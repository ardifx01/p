"""
Project #46: Propangkat Laravel 
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: Propangkat Laravel
project_data = {
    "id": 46, 
    "title": "Propangkat Laravel",
    "headline": "Sistem manajemen kepegawaian dan promosi pangkat berbasis Laravel.",
    "description": [
        "Aplikasi web untuk pengelolaan data pegawai, promosi pangkat, dan riwayat karir menggunakan framework Laravel.",
        "Mendukung alur kerja pengajuan pangkat, persetujuan, dan pelacakan status dengan dashboard administratif.",
        "Dirancang agar instansi/skema pemerintahan kecil/middle dapat mengotomasi proses promosi dan audit log secara transparan."
    ],
    "images": {
        "propangkat_laravel_dashboard.jpg": f"{settings.PROJECT_BASE_IMG_URL}/propangkat_laravel_dashboard.jpg"
    },
    "is_featured": False,
    "features": [
        {"title": "Manajemen Pegawai", "description": "Input dan pemeliharaan data pegawai lengkap: identitas, pangkat, unit kerja."},
        {"title": "Alur Promosi Pangkat", "description": "Fitur pengajuan, verifikasi, persetujuan dan pengumuman hasil promosi."},
        {"title": "Dashboard Status & Audit", "description": "Visualisasi status promosi, laporan real-time, dan riwayat aktivitas sistem."}
    ],
    "tech_stack": [
        SkillsData.tech_stack["php"],
        SkillsData.tech_stack["laravel"],
        SkillsData.tech_stack["mysql"],
        SkillsData.tech_stack["bootstrap"]
    ],
    "github_url": "https://github.com/ardifx01/propangkat-laravel",
    "demo_url": "",
    "status": "in-progress",
    "created_at": None,
    "updated_at": datetime.strptime("2025-10-24T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "Sistem Informasi Kepegawaian, Promosi Pangkat, Government Tech",
    "tags": [
        "Kepegawaian",
        "Promosi Pangkat",
        "Laravel",
        "PHP",
        "Sistem Informasi",
        "Government"
    ],
    "priority": 1,
    "slug": ""
}
