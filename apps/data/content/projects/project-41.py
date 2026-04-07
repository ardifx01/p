"""
Project #41: Faskesku.id 
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: Faskesku.id
project_data = {
    "id": 41, 
    "title": "Faskesku.id",
    "headline": "Platform manajemen fasilitas kesehatan berbasis web untuk monitoring dan layanan pasien.",
    "description": [
        "Aplikasi web yang membantu fasilitas-kesehatan (faskes) dalam mengelola jadwal layanan, data pasien, dan statistik operasional.",
        "Memfasilitasi dashboard status layanan, integrasi dengan sistem BPJS atau JKN, dan pelaporan real-time untuk manajemen rumah sakit/klinik.",
        "Dirancang untuk meningkatkan transparansi, efisiensi layanan, dan kualitas pengalaman pasien di Indonesia."
    ],
    "images": {
        "faskesku_dashboard.jpg": f"{settings.PROJECT_BASE_IMG_URL}/faskesku_dashboard.jpg"
    },
    "is_featured": False,
    "features": [
        {"title": "Dashboard Operasional Faskes", "description": "Ringkasan layanan, jumlah pasien, kapasitas, dan indikator kinerja dalam satu tampilan."},
        {"title": "Manajemen Jadwal & Layanan", "description": "Faskes dapat mengatur jadwal layanan, dokter/tenaga medis, dan ruang layanan secara dinamis."},
        {"title": "Pelaporan & Statistik Real-time", "description": "Data layanan pasien, antrian, dan laporan performa faskes yang bisa diekspor atau di-share ke manajemen atau regulator."}
    ],
    "tech_stack": [
        SkillsData.tech_stack["php"],
        SkillsData.tech_stack["javascript"],
        SkillsData.tech_stack["mysql"]
    ],
    "github_url": "https://github.com/ardifx01/faskesku.id",
    "demo_url": "",
    "status": "in-progress",
    "created_at": None,
    "updated_at": datetime.strptime("2025-10-24T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "Sistem Informasi Kesehatan, Manajemen Faskes",
    "tags": [
        "Fasilitas Kesehatan",
        "Manajemen Faskes",
        "Dashboard",
        "BPJS",
        "PHP",
        "Javascript"
    ],
    "priority": 1,
    "slug": ""
}
