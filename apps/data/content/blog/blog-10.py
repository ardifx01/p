"""
Blog Post #10: What’s New in PHP 8.4.6? A More Stable Foundation!
Generated from centralized blog data
"""

from datetime import datetime
from django.conf import settings

# Blog data for: What’s New in PHP 8.4.6? A More Stable Foundation!
blog_data = {
    "id": 10,
    "title": """What’s New in PHP 8.4.6? A More Stable Foundation!""",
    "description": """Rilis minor PHP 8.4.6 menghadirkan perbaikan stabilitas, bug fixes, dan optimasi agar fondasi PHP 8.4 semakin kokoh.""",
    "images": {
        "php.jpg": f"{settings.BLOG_BASE_IMG_URL}/php.jpg" 
    },
    "created_at": datetime.strptime("2025-04-14T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-04-14T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "author": "dhiff",
    "username": "dhiff",
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg",

    "content": [
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "PHP 8.4.6 resmi dirilis pada 10 April 2025. Meskipun bukan rilis fitur besar, PHP Foundation fokus pada stabilitas, "
                "perbaikan bug, dan penguatan fondasi agar pembaruan besar sebelumnya dapat diandalkan dalam produksi."
            )
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Stabilitas Jadi Prioritas"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "Sejak rilis PHP 8.4 di akhir 2024 dengan fitur-fitur seperti Property Hooks dan Asymmetric Visibility, maka perilis berikutnya seperti 8.4.6 "
                "difokuskan untuk memperkuat fondasi tersebut—bukan menambah fitur besar baru."
            )
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Perbaikan Utama di PHP 8.4.6"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Berikut beberapa perubahan signifikan yang diperkenalkan:"
        },
        {
            "type": "ul",
            "class": "list-disc pl-6 space-y-1",
            "items": [
                "Memperbaiki isu multilevel inheritance di Property Hooks dan proxy virtual properties.",
                "Menangani bug JIT yang menyebabkan segmentation fault atau perilaku salah saat akses properti.",
                "Memperkuat keamanan memori dengan memperbaiki penggunaan after-free saat penghancuran module.",
                "Optimalisasi get_object_vars() dan caching untuk lazy proxies.",
                "Memecahkan regresi performa `foreach` dari bug GH-13193.",
                "Fix pada ekstensi khusus seperti BCMath, DBA, DOM, GD, LDAP, Mbstring, dan PDO.",
                "Perbaikan kompatibilitas Windows terkait penanganan line-ending."
            ]
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Apakah Harus Upgrade ke PHP 8.4.6?"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "Jawabannya: ya. Jika sistemmu sudah berjalan di PHP 8.4.x, maka versi 8.4.6 adalah update penting untuk memperkuat stabilitas, "
                "memperbaiki bug kritik, dan meningkatkan keandalan. Pastikan backup dilakukan sebelum upgrade."
            )
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Tips Upgrade Aman"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "Beberapa hal yang perlu diperhatikan saat upgrade:\n"
                "- Uji di environment staging terlebih dahulu.\n"
                "- Periksa kompatibilitas ekstensi dan modul.\n"
                "- Perbarui opcode cache dan clear cache.\n"
                "- Monitor aplikasi setelah upgrade untuk error atau regresi."
            )
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Visualisasi Alur Update"
        },
        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/php_update_flow.webp",
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Diagram alur rilis versi dan update stabilitas PHP"
        },
        {
            "type": "blockquote",
            "class": "border-l-4 border-green-600 pl-4 italic text-gray-300 my-3",
            "text": "PHP 8.4.6 bukan fitur baru — tapi fondasi yang lebih kokoh untuk ekosistem 8.4"
        }
    ],

    "is_featured": False,
    "tags": ["PHP", "PHP 8.4", "Web Development", "Stability", "Changelog"],
    "category": "Web Development",
    "read_time": 6,
    "views": 0,
    "slug": "whats-new-in-php-8-4-6-a-more-stable-foundation"
}
