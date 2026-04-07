"""
Project #45: Akreditasi-App 
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: Akreditasi-App
project_data = {
    "id": 45, 
    "title": "Akreditasi-App",
    "headline": "Aplikasi manajemen akreditasi institusi atau program studi.",
    "description": [
        "Aplikasi web yang membantu pengelolaan proses akreditasi mulai dari input data institusi/program, pengumpulan bukti, penilaian, hingga pelaporan.",
        "Mendukung dashboard status akreditasi, timeline kegiatan, dokumentasi bukti, dan ekspor ke format laporan standar.",
        "Dirancang untuk institusi pendidikan atau lembaga yang membutuhkan alur akreditasi digital dan terintegrasi."
    ],
    "images": {
        "akreditasi_app_dashboard.jpg": f"{settings.PROJECT_BASE_IMG_URL}/akreditasi_app_dashboard.jpg"
    },
    "is_featured": False,
    "features": [
        {"title": "Manajemen Institusi & Program", "description": "Input data institusi, program studi, unit, dan hierarki akreditasi."},
        {"title": "Pengumpulan Bukti & Dokumen", "description": "Upload dokumen bukti dan tautkan ke kriteria-akreditasi secara sistematis."},
        {"title": "Dashboard Status Akreditasi", "description": "Visualisasi status akreditasi akhir, timeline kegiatan, dan laporan yang tercetak."}
    ],
    "tech_stack": [
        SkillsData.tech_stack["php"],
        SkillsData.tech_stack["laravel"],
        SkillsData.tech_stack["mysql"],
        SkillsData.tech_stack["vuejs"]
    ],
    "github_url": "https://github.com/ardifx01/akreditasi-app",
    "demo_url": "",
    "status": "in-progress",
    "created_at": None,
    "updated_at": datetime.strptime("2025-10-24T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "Sistem Informasi Akademik, Akreditasi",
    "tags": [
        "Akreditasi",
        "Sistem Informasi",
        "Institusi Pendidikan",
        "Laravel",
        "Vue.js",
        "PHP"
    ],
    "priority": 1,
    "slug": ""
}

