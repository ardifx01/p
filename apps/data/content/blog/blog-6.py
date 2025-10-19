"""
Blog Post #6: Gen AI vs AI Agent vs Agentic AI — Evolusi & Perbandingan Kecerdasan Buatan
Generated from centralized blog data
"""

from datetime import datetime
from django.conf import settings

# Blog data for: Gen AI vs AI Agent vs Agentic AI — Evolusi & Perbandingan Kecerdasan Buatan
blog_data = {
    "id": 6,
    "title": """Gen AI vs AI Agent vs Agentic AI — Evolusi & Perbandingan Kecerdasan Buatan""",
    "description": """Penjelasan mendalam perbedaan Generative AI, AI Agent, dan Agentic AI—arena penggunaan, kelebihan, tantangan, dan masa depan.""",
    "images": {
        "gen_ai_agentic.jpg": f"{settings.BLOG_BASE_IMG_URL}/gen_ai_agentic.jpg"
    },
    "created_at": datetime.strptime("2025-10-19T10:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-19T10:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "author": "dhiff",
    "username": "dhiff",
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg",

    "content": [
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Di dunia AI yang berkembang cepat, istilah seperti Generative AI, AI Agent, dan Agentic AI sering dipakai tanpa pemahaman jelas. Tapi sebenarnya, mereka berbeda secara konseptual, teknis, dan dari sisi tujuan penerapan. Dalam artikel ini, kita akan membedakan ketiganya, melihat contoh nyata, kelebihan dan kekurangan masing-masing, serta tren masa depan dalam ekosistem kecerdasan buatan."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Visualisasi Hubungan"
        },
        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/gen_ai_agentic.jpg",
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Diagram Gen AI → AI Agent → Agentic AI"
        },
        {
            "type": "blockquote",
            "class": "border-l-4 border-green-600 pl-4 italic text-gray-300 my-3",
            "text": "Generative AI → AI Agent → Agentic AI — Generative AI mencipta, AI Agent membantu tugas, Agentic AI mengarahkan dan bertindak."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Apa Itu Generative AI?"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Generative AI (Gen AI) adalah jenis AI yang fokus untuk menghasilkan output baru berdasarkan data latih dan prompt, seperti teks, gambar, atau kode. Model seperti GPT-4, DALL·E, dan Stable Diffusion termasuk kategori ini. Karena sifatnya reaktif (menunggu prompt), generative AI ideal untuk tugas kreatif dan generasi konten."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Apa Itu AI Agent?"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "AI Agent adalah sistem yang menggunakan model generatif atau reasoning, tapi dilengkapi dengan kemampuan alat (tool use) dan instruksi domain spesifik. Misalnya: agen email otomatis yang membaca pesan, memanggil API untuk data, lalu merespons berdasarkan logika tertentu. AI Agent memiliki batasan skop tugas dan tidak sepenuhnya otonom; ia biasanya menunggu trigger atau instruksi manusia."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Apa Itu Agentic AI?"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Agentic AI adalah evolusi AI Agent — sistem yang bisa bertindak mandiri untuk mencapai tujuan kompleks melalui beberapa langkah. Ia punya perencanaan, penyesuaian strategi, penggunaan memori & alat, dan eksekusi otomatis. Bukan sekadar menjawab prompt, tapi mengelola proses, memecah tujuan, dan memantau progres."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Perbandingan: Gen AI vs AI Agent vs Agentic AI"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "<ul class='list-disc pl-6 space-y-1'><li>Generative AI: reaktif, fokus konten kreatif berdasarkan prompt.</li><li>AI Agent: interaktif, memiliki alat dan instruksi, dalam batas tugas spesifik.</li><li>Agentic AI: otonom, merencanakan dan bertindak untuk mencapai tujuan multi-langkah.</li></ul>"
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Kelebihan & Kekurangan Tiap Paradigma"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "<ul class='list-disc pl-6 space-y-1'><li>✅ Generative AI: cepat implementasi, banyak tools tersedia.</li><li>✅ AI Agent: memperluas kemampuan AI tanpa intervensi penuh manusia.</li><li>✅ Agentic AI: potensi otomatisasi penuh dan efisiensi tinggi.</li><li>⚠️ Generative AI: risiko hallucination, kurang kontrol kontekstual.</li><li>⚠️ AI Agent: biasanya terbatas pada domain kecil.</li><li>⚠️ Agentic AI: kompleks, tantangan orkestrasi, keamanan, dan auditabilitas tinggi.</li></ul>"
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Tren & Masa Depan"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Banyak ahli menyebut Generative AI akan tetap menjadi basis konten, tapi Agentic AI akan memimpin transformasi sistem cerdas. Misalnya, generative AI menulis draft kampanye, AI Agent mengirim email otomatis, dan Agentic AI memantau performa serta melakukan optimasi. Protokol baru seperti Model Context Protocol (MCP) akan memperkuat jaringan agen otomatis (mesh agents)."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 md:mt-5 mb-2 md:mb-3",
            "text": "Kesimpulan"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Generative AI, AI Agent, dan Agentic AI adalah tiga tahap evolusi kecerdasan buatan. GenAI mencipta, AI Agent mengeksekusi, dan Agentic AI mengorkestrasi. Ketiganya membentuk fondasi masa depan AI yang lebih mandiri, efisien, dan kontekstual. Pemahaman mendalam terhadap tiap paradigma akan menentukan seberapa siap kita memasuki era sistem cerdas yang benar-benar otonom."
        }
    ],

    "is_featured": False,
    "tags": ["Generative AI", "AI Agent", "Agentic AI", "Autonomous Systems"],
    "category": "AI",
    "read_time": 10,
    "views": 0,
    "slug": "gen-ai-vs-ai-agent-vs-agentic-ai"
}
