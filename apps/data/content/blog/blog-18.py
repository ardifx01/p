"""
Blog Post #18: Cybersecurity — Menjaga Informasi Tetap Aman di Dunia Online 
Diterjemahkan dan disusun ulang untuk pembaca umum dan IT enthusiast. Format konsisten dengan blog sebelumnya.
"""

from datetime import datetime
from django.conf import settings

# Blog data for: Cybersecurity — Menjaga Informasi Tetap Aman di Dunia Online
blog_data = {
    "id": 18, 
    "title": """Cybersecurity — Menjaga Informasi Tetap Aman di Dunia Online""",
    "description": """Ringkas, praktis, dan modern: konsep dasar, ancaman umum, praktik terbaik, serta alur respons insiden agar tetap aman saat online.""",
    "images": {
        "cybersecurity_safe_online.jpg": f"{settings.BLOG_BASE_IMG_URL}/cybersecurity_safe_online.jpg" 
    },
    "created_at": datetime.strptime("2025-10-21T18:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-21T18:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "author": "dhiff",
    "username": "dhiff",
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg",

    "content": [
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Keamanan siber adalah serangkaian praktik dan kontrol untuk melindungi data, akun, dan perangkat dari akses tidak sah, kebocoran, dan penyalahgunaan. Artikel ini merangkum fondasi penting, ancaman umum, praktik terbaik yang bisa langsung diterapkan, hingga alur tanggapan insiden."
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-5 mb-3",
            "text": "Visualisasi Konsep"
        },
        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/cybersecurity_safe_online.svg",
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Infografik ringkas: CIA Triad, ancaman umum, praktik terbaik, dan alur tanggapan insiden"
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-5 mb-3",
            "text": "CIA Triad: Kerangka Utama"
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• Confidentiality: hanya pihak berwenang yang boleh mengakses data. Contoh: enkripsi, MFA, kontrol akses. <br>• Integrity: data tidak diubah tanpa izin. Contoh: hashing, tanda tangan digital, kontrol versi. <br>• Availability: layanan dan data tetap tersedia saat dibutuhkan. Contoh: backup, HA, DR, pemantauan kapasitas."
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-5 mb-3",
            "text": "Ancaman Umum yang Perlu Diwaspadai"
        },
        {
            "type": "ul",
            "class": "list-disc pl-6 space-y-1",
            "items": [
                "Phishing dan rekayasa sosial yang menipu pengguna memasukkan kredensial.",
                "Malware, ransomware, dan trojan yang mengenkripsi atau mencuri data.",
                "Credential stuffing dan brute force karena kata sandi lemah atau daur ulang.",
                "Kebocoran data akibat konfigurasi salah pada bucket/storage dan layanan publik.",
                "Serangan supply chain lewat dependensi/SDK berbahaya dan update palsu."
            ]
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-5 mb-3",
            "text": "Praktik Terbaik yang Bisa Langsung Diterapkan"
        },
        {
            "type": "ul",
            "class": "list-disc pl-6 space-y-1",
            "items": [
                "Aktifkan MFA/2FA pada email, cloud, banking, dan akun inti.",
                "Gunakan password manager dan passphrase unik panjang.",
                "Update OS, browser, aplikasi; terapkan patch rutin.",
                "Selalu pakai HTTPS/TLS; gunakan VPN tepercaya pada jaringan publik.",
                "Backup 3-2-1 dan uji pemulihan berkala.",
                "Prinsip least privilege, segmentasi jaringan, dan pendekatan Zero Trust.",
                "Waspadai tautan/lampiran mencurigakan; verifikasi sumber.",
                "Pantau login aktif, lokasi perangkat, dan revoke session mencurigakan."
            ]
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-5 mb-3",
            "text": "Checklist Hardening Cepat"
        },
        {
            "type": "ul",
            "class": "list-disc pl-6 space-y-1",
            "items": [
                "Nonaktifkan layanan yang tidak diperlukan di perangkat/VM.",
                "Batasi port inbound dengan firewall; gunakan allowlist ketat.",
                "Aktifkan disk/file encryption pada laptop dan ponsel.",
                "Pisahkan akun admin dan akun harian.",
                "Audit izin aplikasi pihak ketiga secara berkala."
            ]
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-5 mb-3",
            "text": "Alur Tanggapan Insiden (IR) yang Disarikan"
        },
        {
            "type": "ol",
            "class": "list-decimal pl-6 space-y-1",
            "items": [
                "Identifikasi: deteksi indikasi kompromi, klasifikasikan keparahan.",
                "Isolasi: putus koneksi/akun bermasalah untuk mencegah penyebaran.",
                "Analisis: kumpulkan artefak, log, dan indikator kompromi.",
                "Pemulihan: pulihkan layanan/data secara bertahap dengan verifikasi integritas.",
                "Perkuatan: patch, rotate secrets, perbaiki kontrol yang lemah.",
                "Postmortem: dokumentasi akar masalah, perbarui SOP, edukasi tim."
            ]
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-5 mb-3",
            "text": "Kesimpulan"
        },
        {
            "type": "p",
            "class": "mb-2",
            "text": "Keamanan siber bukan satu alat, melainkan kebiasaan dan kontrol berlapis. Mulai dari MFA, password manager, pembaruan rutin, hingga backup dan Zero Trust. Bangun kebiasaan aman, latih kewaspadaan, dan siap dengan rencana pemulihan."
        }
    ],

    "is_featured": False,
    "tags": ["Cybersecurity", "Privacy", "MFA", "Zero Trust", "Backup", "Incident Response"],
    "category": "Security",
    "read_time": 8,
    "views": 0,
    "slug": "cybersecurity-keeping-information-safe-online"
}
