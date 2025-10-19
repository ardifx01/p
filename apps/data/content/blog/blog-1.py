"""
Blog Post #1: Gaji Programmer di Indonesia 
Generated from centralized blog data
"""

from datetime import datetime
from django.conf import settings

# Blog data for: Gaji Programmer di Indonesia
blog_data = {
    "id": 1, 
    "title": """Gaji Programmer di Indonesia""",
    "description": """Menelusuri rata-rata gaji profesi IT di Indonesia: dari junior developer hingga software engineer senior, dan faktor-faktor yang memengaruhi angka tersebut.""",
    "images": {
        "gajiIT.jpg": f"{settings.BLOG_BASE_IMG_URL}/gajiIT.jpg"
    },
    "created_at": datetime.strptime("2025-10-17T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-17T14:30:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "author": "dhiff",
    "username": "dhiff", 
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg", 
    "content": [
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Bidang teknologi informasi kini menjadi salah satu sektor dengan pertumbuhan tercepat di Indonesia. Permintaan terhadap programmer, software engineer, dan profesional IT terus meningkat seiring transformasi digital di berbagai industri."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Faktor yang Mempengaruhi Besaran Gaji"
        },
        {
            "type": "ul",
            "class": "list-disc pl-6 mb-4 text-sm md:text-base lg:text-lg",
            "items": [
                "Tingkat pengalaman — junior, mid-level, dan senior memiliki rentang gaji yang signifikan.",
                "Keahlian teknis — penguasaan framework modern (misalnya React, Django, Go) meningkatkan nilai di pasar kerja.",
                "Lokasi kerja — gaji di kota besar seperti Jakarta atau Bandung lebih tinggi dibanding kota kecil.",
                "Jenis perusahaan — startup, korporasi global, atau lembaga pemerintahan memiliki struktur kompensasi berbeda.",
                "Sertifikasi dan portofolio — proyek nyata dan sertifikasi dari lembaga kredibel dapat memperkuat posisi tawar."
            ]
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Rata-rata Gaji Berdasarkan Posisi"
        },
        {
            "type": "ul",
            "class": "list-disc pl-6 mb-4 text-sm md:text-base lg:text-lg",
            "items": [
                "Junior Developer: Rp 5–8 juta per bulan.",
                "Mid-Level Developer: Rp 9–15 juta per bulan.",
                "Senior Developer / Software Engineer: Rp 16–30 juta per bulan.",
                "DevOps Engineer / System Administrator: Rp 12–25 juta per bulan.",
                "Data Analyst / Data Scientist: Rp 10–25 juta per bulan.",
                "Mobile Developer: Rp 9–20 juta per bulan."
            ]
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Perlu dicatat bahwa angka tersebut bervariasi tergantung industri dan lokasi. Beberapa startup teknologi di Jakarta bahkan menawarkan kompensasi hingga dua kali lipat untuk posisi dengan tanggung jawab tinggi atau keahlian spesifik."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Tren dan Prospek Karier Programmer"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Dengan adopsi AI, cloud computing, dan data-driven system, permintaan terhadap talenta IT akan terus meningkat. Banyak perusahaan kini beralih ke model kerja remote, memperluas peluang kerja programmer ke pasar global tanpa batas geografis."
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Selain kemampuan teknis, kemampuan komunikasi, kolaborasi tim lintas fungsi, dan adaptasi terhadap teknologi baru menjadi faktor penting dalam menentukan jenjang karier dan kompensasi."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Kesimpulan"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Menjadi programmer di Indonesia memberikan prospek cerah, terutama bagi mereka yang terus belajar dan memperbarui keahliannya. Dengan portofolio kuat, pemahaman bisnis, dan etos kerja yang baik, peluang mendapatkan gaji kompetitif sangat terbuka lebar."
        }
    ],
    "is_featured": False,
    "tags": ["Programmer", "IT Career", "Salary", "Indonesia", "Technology", "Software Engineering"],
    "category": "Career",
    "read_time": 5,
    "views": 0,
    "slug": "gaji-programmer-indonesia"
}

