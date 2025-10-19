"""
Blog Post #3: ScrapeCraft by ScrapeGraphAI — Framework Berbasis Graf untuk Web Scraping Bertenaga AI 
Generated from centralized blog data
"""

from datetime import datetime
from django.conf import settings

blog_data = {
    "id": 3, 
    "title": """ScrapeCraft by ScrapeGraphAI — Framework Berbasis Graf untuk Web Scraping Bertenaga AI""",
    "description": """Mengenal ScrapeCraft, framework open-source dari ScrapeGraphAI yang memadukan Large Language Models (LLM) dengan arsitektur graf untuk scraping data web yang cerdas dan adaptif.""",
    "images": {
        "scrapecraft.jpg": f"{settings.BLOG_BASE_IMG_URL}/scrapecraft.jpg"
    },
    "created_at": datetime.strptime("2025-10-17T00:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-17T15:30:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "author": "dhiff", 
    "username": "dhiff", 
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg", 
    "content": [
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "ScrapeCraft adalah framework open-source yang dikembangkan oleh ScrapeGraphAI untuk mengotomatisasi ekstraksi data dari web menggunakan pendekatan berbasis graf dan reasoning dari model bahasa besar (LLM). Framework ini membuat proses web scraping lebih dinamis, cerdas, dan tahan terhadap perubahan struktur HTML."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-3",
            "text": "Konsep Dasar"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Berbeda dari library seperti BeautifulSoup atau Scrapy yang bergantung pada selector statis, ScrapeCraft menggunakan node graf untuk mendeskripsikan alur scraping. Setiap node mewakili aksi tertentu — misalnya mengambil halaman (fetch), mengekstrak data (extract), atau melakukan transformasi (transform). Beberapa node menggunakan LLM agar bisa memahami konteks halaman web secara semantik."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-3",
            "text": "Instalasi"
        },
        {
            "type": "code",
            "lang": "bash",
            "class": "rounded-lg bg-[#0f172a] text-gray-100 text-sm p-4 font-mono",
            "text": "pip install scrapecraft"
        },
        {
            "type": "code",
            "lang": "bash",
            "class": "rounded-lg bg-[#0f172a] text-gray-100 text-sm p-4 font-mono",
            "text": "git clone https://github.com/ScrapeGraphAI/scrapecraft.git\ncd scrapecraft\npip install -e ."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-3",
            "text": "Mendefinisikan Workflow Scraping"
        },
        {
            "type": "code",
            "lang": "json",
            "class": "rounded-lg bg-[#0f172a] text-gray-100 text-sm p-4 font-mono",
            "text": "{\n  \"nodes\": [\n    {\n      \"id\": \"fetch_homepage\",\n      \"type\": \"FetchNode\",\n      \"params\": { \"url\": \"https://example.com\" }\n    },\n    {\n      \"id\": \"extract_links\",\n      \"type\": \"LLMExtractNode\",\n      \"params\": {\n        \"prompt\": \"Extract all article URLs and titles\",\n        \"llm\": \"gpt-4o-mini\"\n      },\n      \"input\": [\"fetch_homepage\"]\n    }\n  ],\n  \"output\": [\"extract_links\"]\n}"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Graf di atas mendefinisikan dua node: satu untuk mengambil halaman web dan satu lagi untuk mengekstrak URL artikel menggunakan LLM. Arsitektur berbasis graf ini membuat workflow mudah dibaca, diubah, dan digunakan ulang."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-3",
            "text": "Menjalankan Workflow"
        },
        {
            "type": "code",
            "lang": "python",
            "class": "rounded-lg bg-[#0f172a] text-gray-100 text-sm p-4 font-mono",
            "text": "from scrapecraft import GraphRunner\n\nrunner = GraphRunner(\"workflow.json\")\nresult = runner.run()\nprint(result)"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Saat dieksekusi, ScrapeCraft membaca file JSON workflow, menjalankan node sesuai urutan dependensi, dan menggunakan API LLM untuk mengekstrak data secara kontekstual."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-3",
            "text": "Visualisasi Workflow"
        },
        {
            "type": "code",
            "lang": "python",
            "class": "rounded-lg bg-[#0f172a] text-gray-100 text-sm p-4 font-mono",
            "text": "from scrapecraft.visualize import visualize_graph\n\nvisualize_graph(\"workflow.json\")"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Fitur ini memungkinkan pengembang melihat representasi graf dari seluruh pipeline scraping untuk debugging maupun dokumentasi."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-3",
            "text": "Node Reasoning dengan LLM"
        },
        {
            "type": "code",
            "lang": "python",
            "class": "rounded-lg bg-[#0f172a] text-gray-100 text-sm p-4 font-mono",
            "text": "from scrapecraft.nodes import LLMExtractNode\n\nnode = LLMExtractNode(\n    prompt=\"Extract author names and publication dates\",\n    llm=\"gpt-4o-mini\"\n)"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Node ini memakai LLM untuk memahami struktur HTML dan mengambil informasi spesifik seperti nama penulis atau tanggal publikasi. Keunggulannya adalah fleksibilitas terhadap perubahan struktur web."
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-3",
            "text": "Kelebihan dan Kekurangan"
        },
        {
            "type": "ul",
            "class": "list-disc pl-6 mb-4 text-sm md:text-base lg:text-lg",
            "items": [
                "✅ Adaptif terhadap perubahan struktur web — tidak bergantung pada selector statis.", 
                "✅ Workflow modular dan dapat digunakan ulang.", 
                "⚠️ Biaya tinggi jika sering memanggil API LLM.", 
                "⚠️ Latensi lebih besar dibanding scraping tradisional.", 
                "⚠️ Wajib mematuhi etika web scraping** (robots.txt, terms of use)." 
            ]
        },
        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-3",
            "text": "Kesimpulan"
        },
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "ScrapeCraft menghadirkan pendekatan baru dalam dunia web scraping: memanfaatkan LLM dan graf modular untuk memahami struktur web secara semantik. Dengan integrasi reasoning AI, framework ini membuka jalan menuju web scraping yang lebih cerdas, fleksibel, dan tahan lama terhadap perubahan struktur HTML."
        }
    ],
    "is_featured": False,
    "tags": ["Web Scraping", "AI", "LLM", "Python", "Automation", "ScrapeGraphAI", "Data Extraction"],
    "category": "Technology",
    "read_time": 7,
    "views": 0,
    "slug": "scrapecraft-ai-web-scraping"
}
