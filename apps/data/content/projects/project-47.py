"""
Project #47: Absensi Sekolah QR Code 
Generated from centralized projects data
"""

from datetime import datetime
from django.conf import settings
from apps.data.about.skills_data import SkillsData

# Project data for: Absensi Sekolah QR Code
project_data = {
    "id": 47, 
    "title": "Absensi Sekolah QR Code",
    "headline": "Sistem absensi sekolah berbasis QR Code untuk siswa dan guru.",
    "description": [
        "Aplikasi web yang memfasilitasi proses presensi siswa dan guru menggunakan pemindaian QR Code.",
        "Dikembangkan dengan CodeIgniter 4 sebagai kerangka kerja backend dan dilengkapi generator QR Code, scanner, notifikasi WA, serta dashboard manajemen absensi. :contentReference[oaicite:1]{index=1}",
        "Menargetkan efisiensi dalam pencatatan kehadiran dan pengelolaan data siswa/guru di sekolah."
    ],
    "images": {
        "absensiqr.jpg": f"{settings.PROJECT_BASE_IMG_URL}/absensiqr.jpg" 
    },
    "is_featured": False,
    "features": [
        {"title": "Pemindaian QR Code & Validasi", "description": "Siswa/guru memindai QR Code unik yang telah dibuat dan sistem mencatat kehadiran secara otomatis. :contentReference[oaicite:2]{index=2}"},
        {"title": "Generator QR Code + Download", "description": "Administrator dapat menghasilkan QR Code unik per siswa/guru dan mengunduhnya untuk didistribusikan. :contentReference[oaicite:3]{index=3}"},
        {"title": "Dashboard & Laporan Absensi", "description": "Dashboard monitoring dan laporan kehadiran dalam format PDF tersedia untuk petugas sekolah. :contentReference[oaicite:4]{index=4}"}
    ],
    "tech_stack": [
        SkillsData.tech_stack["php"],
        SkillsData.tech_stack["codeigniter"],
        SkillsData.tech_stack["javascript"],
        SkillsData.tech_stack["mysql"]
    ],
    "github_url": "https://github.com/ardifx01/absensi-sekolah-qr-code",
    "demo_url": "",
    "status": "in-progress",
    "created_at": None,
    "updated_at": datetime.strptime("2023-08-18T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "category": "Absensi, Sekolah, QR Code, Sistem Informasi",
    "tags": [
        "Absensi",
        "QR Code",
        "Sekolah",
        "LMS",
        "Open Source",
        "CodeIgniter 4"
    ],
    "priority": 1,
    "slug": ""
}
