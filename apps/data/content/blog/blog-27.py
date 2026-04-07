"""
Blog Post #27: Next.js Modern Kena Celah RCE Kritis via RSC 
Generated from centralized blog data
"""

from datetime import datetime
from django.conf import settings

# Blog data for: Next.js Modern Kena Celah RCE Kritis via RSC
blog_data = {
    "id": 27, 
    "title": """Next.js Modern Kena Celah RCE Kritis, Server Bisa Diambil Alih via RSC""",
    "description": """Kerentanan kritis pada React Server Components (RSC) di Next.js modern memungkinkan penyerang melakukan Remote Code Execution (RCE) dan mengambil alih server sepenuhnya tanpa autentikasi.""",
    "images": {
        "nextjs_rce_rsc.jpg": f"{settings.BLOG_BASE_IMG_URL}/nextjs_rce_rsc.jpg" 
    },
    "created_at": datetime.strptime("2025-12-09T09:30:00+07:00", "%Y-%m-%dT%H:%M:%S%z"), 
    "updated_at": datetime.strptime("2025-12-09T09:30:00+07:00", "%Y-%m-%dT%H:%M:%S%z"), 
    "author": "dhiff",
    "username": "dhiff",
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg",

    "content": [
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "Dunia web development kembali diguncang dengan temuan celah keamanan kritis pada ekosistem Next.js modern "
                "yang memanfaatkan React Server Components (RSC). Celah ini memungkinkan penyerang melakukan Remote Code "
                "Execution (RCE) secara langsung ke server hanya dengan request HTTP tertentu, tanpa perlu login."
            )
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "Dengan RCE, attacker tidak hanya bisa membaca data, tetapi juga mengeksekusi perintah sistem, mencuri "
                "environment variable, menanam malware, hingga mengambil alih full server. Risiko ini sangat tinggi terutama "
                "bagi aplikasi enterprise yang mengandalkan App Router dan RSC."
            )
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Visualisasi Serangan RSC & Dampaknya"
        },
        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/nextjs_rce_rsc.webp",
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Diagram alur serangan RCE melalui React Server Components"
        },
        {
            "type": "blockquote",
            "class": "border-l-4 border-red-600 pl-4 italic text-gray-300 my-3",
            "text": "Ini bukan sekadar bug biasa — ini adalah celah yang bisa menjadikan server kamu senjata bagi penyerang."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Apa Itu React Server Components (RSC)?"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "React Server Components adalah mekanisme rendering komponen React langsung di server tanpa mengirim seluruh "
                "logic ke client. Data antar client dan server dikirim melalui protokol khusus bernama React Flight."
            )
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Akar Masalah Kerentanan"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "Celah ini terjadi karena proses deserialisasi payload RSC tidak memvalidasi struktur data secara ketat. "
                "Payload yang dimanipulasi bisa memaksa server masuk ke jalur eksekusi berbahaya yang akhirnya mengeksekusi kode arbitrer."
            )
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Versi Next.js yang Terdampak"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "Kerentanan ini berdampak pada Next.js 15.x dan 16.x yang menggunakan React Server Components. "
                "Beberapa versi canary Next.js 14 juga teridentifikasi rentan. Aplikasi dengan Pages Router "
                "atau versi stabil lama relatif tidak terdampak."
            )
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Dampak Nyata Jika Dieksploitasi"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "Jika berhasil dieksploitasi, attacker dapat menjalankan perintah sistem operasi, membaca file sensitif, "
                "mengambil credential database, memodifikasi source code, serta menjadikan server sebagai bagian dari botnet."
            )
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Versi Aman & Patch Resmi"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "Pihak Next.js telah merilis patch keamanan untuk beberapa versi antara lain 15.0.5, 15.1.9, 15.2.6, "
                "15.3.6, 15.4.8, 15.5.7, dan 16.0.7. Upgrade adalah langkah yang wajib dilakukan secepat mungkin."
            )
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Rekomendasi Mitigasi Sementara"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "Jika belum sempat update, segera batasi akses publik ke server menggunakan firewall atau WAF. "
                "Aktifkan logging penuh, audit request mencurigakan, dan lakukan rotasi semua credential penting."
            )
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Implikasi untuk Developer & DevOps"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "Kasus ini menjadi peringatan serius bahwa fitur modern seperti server-side rendering dan server components "
                "memiliki permukaan serangan yang jauh lebih luas dibanding aplikasi frontend biasa."
            )
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Kesimpulan"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "Celah RCE di React Server Components bukan sekadar bug biasa, melainkan ancaman serius yang bisa "
                "menghancurkan seluruh infrastruktur jika diabaikan. Update, audit, dan hardening adalah harga mati."
            )
        }
    ],

    "is_featured": False,
    "tags": ["Next.js", "React", "RCE", "Cyber Security", "Web Security", "Exploit"],
    "category": "Cyber Security",
    "read_time": 10,
    "views": 0,
    "slug": "nextjs-modern-kena-celah-rce-kritis-via-rsc"
}
