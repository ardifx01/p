"""
Blog Post #9: Vibe Coding – Duet Programmer dengan AI 
Enhanced version with new typography and layout
"""

from datetime import datetime
from django.conf import settings

blog_data = {
    "id": 9, 
    "title": "Vibe Coding – Duet Programmer dengan AI",
    "description": "Sebuah refleksi tentang era baru pemrograman: manusia dan AI berkolaborasi dalam harmoni digital, menciptakan kode yang lebih cepat, cerdas, dan bermakna.",
    "images": {
        "vibe_coding.jpg": f"{settings.BLOG_BASE_IMG_URL}/vibe_coding.jpg" 
    },
    "created_at": datetime.strptime("2025-10-18T02:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-18T02:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "author": "dhifff",
    "username": "dhifff",
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg",
    "content": [
        {
            "type": "p",
            "class": "text-base md:text-lg leading-relaxed tracking-wide mb-6",
            "text": "Dulu, menjadi programmer berarti begadang di depan monitor, menulis baris demi baris kode hingga mata lelah. Kini, sebagian besar kode itu bisa lahir dari satu baris kalimat. Dunia ini menyebutnya <strong>Vibe Coding</strong> — cara baru di mana manusia dan AI berkolaborasi menciptakan perangkat lunak."
        },
        {
            "type": "p",
            "class": "text-base md:text-lg leading-relaxed tracking-wide mb-6",
            "text": "Vibe Coding bukan sekadar tren, tapi pergeseran paradigma. Manusia kini berperan sebagai <em>visionary</em> — pengarah konsep, pengambil keputusan, dan penjaga makna. Sedangkan AI menjadi tangan eksekusi, membangun ide manusia menjadi bentuk nyata: baris kode yang hidup."
        },
        {
            "type": "h3",
            "class": "text-xl font-semibold text-white mt-10 mb-3",
            "text": "💡 Apa Itu 'Vibe Coding'?"
        },
        {
            "type": "p",
            "class": "text-base md:text-lg leading-relaxed tracking-wide mb-6",
            "text": "Istilah 'vibe' muncul karena cara kerjanya terasa alami — mengalir seperti percakapan. Kamu mengetik ide: <em>“Buat API login dengan JWT dan middleware auth.”</em> Lalu AI menulis seluruh strukturnya, melengkapi setiap fungsi dan validasi input. Kamu meninjau, lalu memperbaiki bagian yang tidak sesuai. Alurnya terasa seperti berdialog dengan rekan kerja, bukan dengan mesin."
        },
        {
            "type": "div",
            "class": "border-l-4 border-blue-500 bg-[#0d1726] p-4 rounded-lg my-6 italic text-blue-200",
            "text": "Vibe Coding adalah bentuk komunikasi dua arah antara manusia dan AI — bukan perintah satu arah, melainkan kolaborasi ide dan logika."
        },
        {
            "type": "h3",
            "class": "text-xl font-semibold text-white mt-10 mb-3",
            "text": "🚀 Keuntungan Utama"
        },
        {
            "type": "ul",
            "class": "list-disc list-inside space-y-3 text-base md:text-lg leading-relaxed mb-6",
            "items": [
                "<strong>Efisiensi Waktu:</strong> Pembuatan kode bisa dipangkas hingga 70%.",
                "<strong>Kreativitas Tanpa Batas:</strong> Kamu fokus pada ide, bukan sintaks.",
                "<strong>Kolaborasi Instan:</strong> AI bisa menjadi rekan diskusi sekaligus penguji logika.",
                "<strong>Belajar Cepat:</strong> Developer pemula bisa memahami pola kode dari hasil AI."
            ]
        },
        {
            "type": "h3",
            "class": "text-xl font-semibold text-white mt-10 mb-3",
            "text": "⚠️ Risiko dan Tantangan"
        },
        {
            "type": "p",
            "class": "text-base md:text-lg leading-relaxed tracking-wide mb-6",
            "text": "Ketika terlalu bergantung pada AI, kemampuan berpikir algoritmik bisa tumpul. Tanpa dasar yang kuat, programmer berisiko menerima kode yang salah secara logika namun tampak benar secara sintaks."
        },
        {
            "type": "div",
            "class": "border-l-4 border-red-500 bg-[#1b0b0b] p-4 rounded-lg my-6 italic text-red-200",
            "text": "AI tidak memahami visi bisnis atau konteks sosial. Ia menulis sesuai pola, bukan tujuan. Di sinilah manusia tetap menjadi pengarah utama."
        },
        {
            "type": "h3",
            "class": "text-xl font-semibold text-white mt-10 mb-3",
            "text": "🧠 Ekosistem Pendukung"
        },
        {
            "type": "ul",
            "class": "list-disc list-inside space-y-3 text-base md:text-lg leading-relaxed mb-6",
            "items": [
                "<strong>GitHub Copilot X</strong> – menulis kode real-time dengan analisis konteks proyek.",
                "<strong>Cursor IDE</strong> – editor futuristik dengan prompt-based editing.",
                "<strong>Claude & ChatGPT</strong> – AI untuk brainstorming, refactor, dan dokumentasi otomatis.",
                "<strong>Tabnine</strong> – AI lokal untuk tim enterprise dengan keamanan tinggi."
            ]
        },
        {
            "type": "h3",
            "class": "text-xl font-semibold text-white mt-10 mb-3",
            "text": "🌌 Masa Depan Developer"
        },
        {
            "type": "p",
            "class": "text-base md:text-lg leading-relaxed tracking-wide mb-6",
            "text": "Di masa depan, developer tidak lagi diukur dari seberapa cepat mengetik, tapi seberapa cerdas mereka berbicara dengan AI. Mereka yang mampu menjelaskan ide dengan jelas akan menjadi penggerak utama industri software."
        },
        {
            "type": "div",
            "class": "border-l-4 border-green-500 bg-[#10291b] p-4 rounded-lg my-6 italic text-green-200",
            "text": "Kita sedang menyaksikan pergeseran: dari ‘menulis kode’ menjadi ‘mengarahkan kecerdasan’. Inilah makna sejati dari Vibe Coding."
        },
        {
            "type": "p",
            "class": "text-base md:text-lg leading-relaxed tracking-wide mt-8",
            "text": "Kolaborasi antara manusia dan AI bukan tentang menggantikan siapa pun. Ini tentang menyatukan dua bentuk kecerdasan — logika mesin dan intuisi manusia — menjadi satu harmoni digital."
        }
    ],
    "is_featured": False,
    "tags": ["AI Programming", "Vibe Coding", "Automation", "Developer Future"],
    "category": "Programming & AI",
    "read_time": 8,
    "views": 0,
    "slug": "vibe-coding-duet-programmer-dengan-ai"
}
