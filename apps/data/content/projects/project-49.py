"""
Project #49: Sistem Pembelajaran Daring UNTAGSMG 
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: Sistem Pembelajaran Daring UNTAGSMG
project_data = {
    "id": 49, 
    "title": "Sistem Pembelajaran Daring UNTAGSMG",
    "headline": "Platform pembelajaran daring untuk mahasiswa dan dosen di UNTAG Semarang.",
    "description": [
        "Platform ini dibangun sebagai sistem pembelajaran daring (LMS) untuk Universitas 17 Agustus 1945 Semarang (UNTAG SMG).",
        "Mulai digunakan sejak awal 2020 dan diperbarui kembali versi LMS-terbarunya pada 2024. :contentReference[oaicite:2]{index=2}",
        "Fitur utama meliputi akses kursus per fakultas/jurusan/semester, berbagai format materi pembelajaran, sistem akun mahasiswa & dosen, pengumuman akademik, dan pengelolaan kelas serta konten pembelajaran. :contentReference[oaicite:3]{index=3}"
    ],
    "images": {
        "spada.jpg": f"{settings.PROJECT_BASE_IMG_URL}/spada.jpg" 
    },
    "is_featured": False,
    "features": [
        {"title": "Akses Kursus Terintegrasi", "description": "Mahasiswa dan dosen dapat mengakses kursus dari berbagai fakultas, jurusan, dan semester."},
        {"title": "Materi Multi-Format", "description": "Materi pembelajaran tersedia dalam beragam format untuk mendukung proses belajar fleksibel."},
        {"title": "Manajemen Pengguna & Kelas", "description": "Sistem login akun mahasiswa & dosen, pengelolaan kelas, konten, dan pengumuman akademik."}
    ],
    "tech_stack": [
        SkillsData.tech_stack["php"],
        SkillsData.tech_stack["javascript"],
        SkillsData.tech_stack["mysql"],
     ], 
    "github_url": "https://github.com/ardifx01/sistem-pembelajaran-daring-untagsmg",
    "demo_url": "",
    "status": "in-progress",
    "created_at": None,
    "updated_at": datetime.strptime("2024-01-01T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "E-Learning, LMS, Akademik",
    "tags": [
        "E-Learning",
        "LMS",
        "Akademik",
        "Open Source",
        "PHP",
        "JavaScript"
    ],
    "priority": 1,
    "slug": ""
}
