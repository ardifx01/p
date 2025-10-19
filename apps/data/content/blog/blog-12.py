"""
Blog Post #12: Optimizing Web & Mobile Accessibility
Generated from centralized blog data
"""

from datetime import datetime
from django.conf import settings

# Blog data for: Optimizing Web & Mobile Accessibility
blog_data = {
    "id": 12,
    "title": """Optimizing Web & Mobile Accessibility""",
    "description": """Panduan praktis membangun pengalaman web dan aplikasi mobile yang inklusif dengan prinsip aksesibilitas modern (a11y) – untuk semua pengguna, tanpa kecuali.""",
    "images": {
        "blog.jpg": f"{settings.BLOG_BASE_IMG_URL}/blog.jpg" 
    },
    "created_at": datetime.strptime("2025-10-17T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-17T13:45:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "author": "dhiff", 
    "username": "dhiff", 
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg", 
    "content": [
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Aksesibilitas web dan mobile (a11y) berarti memastikan situs serta aplikasi dapat digunakan oleh semua orang, termasuk mereka dengan keterbatasan penglihatan, pendengaran, motorik, maupun kognitif. Prinsip ini bukan sekadar tambahan, melainkan bagian dari tanggung jawab sosial dalam desain digital."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Mengapa Aksesibilitas Penting?"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Lebih dari satu miliar orang di dunia hidup dengan disabilitas, dan aksesibilitas digital membuka peluang yang sama bagi mereka untuk berinteraksi, belajar, dan bekerja. Selain itu, web yang aksesibel cenderung lebih SEO-friendly, memiliki pengalaman pengguna lebih baik, dan menghindarkan dari pelanggaran hukum di negara tertentu."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Empat Prinsip Utama: POUR"
        },
        {
            "type": "ul",
            "class": "list-disc pl-6 mb-4 text-sm md:text-base lg:text-lg",
            "items": [
                "Perceivable – informasi harus bisa ditangkap oleh semua pengguna, termasuk melalui teks alternatif atau subtitle.",
                "Operable – antarmuka dapat dikontrol oleh berbagai input seperti keyboard, suara, atau sentuhan.",
                "Understandable – navigasi dan bahasa mudah dimengerti, instruksi jelas.",
                "Robust – konten dapat dibaca oleh berbagai teknologi bantu dan browser."
            ]
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Langkah Praktis untuk Web & Mobile"
        },
        {
            "type": "ul",
            "class": "list-disc pl-6 mb-4 text-sm md:text-base lg:text-lg",
            "items": [
                "Gunakan struktur heading <h1>–<h3> secara hierarkis, bukan hanya untuk styling.",
                "Tambahkan teks alternatif (alt text) pada semua gambar.",
                "Pastikan kontras warna antara teks dan latar cukup tinggi.",
                "Sediakan navigasi berbasis keyboard.",
                "Ukuran tombol dan link cukup besar untuk tap pada layar kecil.",
                "Form memiliki label dan pesan kesalahan yang deskriptif.",
                "Multimedia seperti video memiliki subtitle atau transkrip.",
                "Desain harus responsif dan adaptif terhadap perubahan orientasi dan zoom."
            ]
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Tantangan dan Praktik Terbaik"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Implementasi aksesibilitas membutuhkan konsistensi lintas tim desain dan pengembang. Kadang ada kompromi antara estetika dan fungsi, namun fokus utama tetap pada kemudahan pengguna. Audit rutin dan pengujian langsung dengan pengguna disabilitas membantu memastikan solusi benar-benar efektif."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Kesimpulan"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Aksesibilitas bukan hanya fitur tambahan, tetapi standar etika dalam dunia digital. Dengan mengikuti prinsip POUR dan langkah-langkah praktis di atas, pengembang dapat menciptakan pengalaman web dan aplikasi yang benar-benar inklusif."
        }
    ],
    "is_featured": False,
    "tags": ["Accessibility", "Web Development", "Mobile", "UI/UX", "Inclusivity", "Frontend", "Best Practices"],
    "category": "Technology",
    "read_time": 6,
    "views": 0,
    "slug": "web-mobile-accessibility-guide"
}
