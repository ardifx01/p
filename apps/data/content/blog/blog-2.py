"""
Blog Post #2: Apa Itu GitHub? 
Generated from centralized blog data
"""

from datetime import datetime
from django.conf import settings

blog_data = {
    "id": 2, 
    "title": """Apa Itu GitHub?""",
    "description": """GitHub sebagai platform kolaborasi kode: definisi, fungsi dasar, dan langkah awal penggunaan bagi pemula.""",
    "images": {
        "github.jpg": f"{settings.BLOG_BASE_IMG_URL}/github.jpg" 
    },
    "created_at": datetime.strptime("2025-10-17T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-17T15:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "author": "dhiff", 
    "username": "dhiff", 
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg", 
    "content": [
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "GitHub adalah platform berbasis web untuk pengembang yang menggabungkan sistem kontrol versi Git, manajemen proyek, dan kolaborasi sosial dalam satu ekosistem terpadu. Platform ini memungkinkan ribuan developer di seluruh dunia berkontribusi pada kode sumber secara bersamaan."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Fungsi Dasar GitHub"
        },
        {
            "type": "ul",
            "class": "list-disc pl-6 mb-4 text-sm md:text-base lg:text-lg",
            "items": [
                "Menyimpan dan mengelola repositori kode menggunakan Git secara online.",
                "Mendukung version control melalui commit, branch, merge, dan pull request.",
                "Memfasilitasi kolaborasi tim lintas lokasi melalui issue tracker, discussion, dan review kode.",
                "Menjadi portofolio profesional bagi pengembang melalui tampilan profil dan kontribusi publik."
            ]
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Cara Memulai: Langkah untuk Pemula"
        },
        {
            "type": "ul",
            "class": "list-disc pl-6 mb-4 text-sm md:text-base lg:text-lg",
            "items": [
                "Daftar akun GitHub secara gratis di situs resmi.",
                "Verifikasi email dan lengkapi profil dengan foto, bio, serta preferensi bahasa pemrograman.",
                "Buat repository baru, isi nama proyek dan deskripsi singkat.",
                "Pilih apakah repository bersifat publik atau privat.",
                "Mulai commit dan eksplorasi fitur kolaborasi seperti pull request dan branch."
            ]
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Istilah Penting di GitHub"
        },
        {
            "type": "ul",
            "class": "list-disc pl-6 mb-4 text-sm md:text-base lg:text-lg",
            "items": [
                "Repository (Repo) – wadah utama proyek kode sumber.",
                "Commit – rekaman setiap perubahan kode.",
                "Branch – cabang kerja terpisah untuk eksperimen atau fitur baru.",
                "Merge – proses penggabungan perubahan antar branch.",
                "Clone – menyalin repository dari GitHub ke komputer lokal.",
                "Push dan Pull – sinkronisasi perubahan antara repository lokal dan remote."
            ]
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Kesimpulan"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "GitHub telah menjadi pusat ekosistem pengembangan modern. Platform ini tidak hanya memudahkan pengelolaan kode, tetapi juga membangun budaya kolaborasi terbuka di dunia pemrograman. Untuk pemula, cukup mulai dengan membuat akun, memahami konsep repository, dan rajin berkontribusi pada proyek terbuka."
        }
    ],
    "is_featured": False,
    "tags": ["GitHub", "Version Control", "Git", "Programming", "Collaboration", "Developer Tools"],
    "category": "Technology",
    "read_time": 5,
    "views": 0,
    "slug": "apa-itu-github"
}
