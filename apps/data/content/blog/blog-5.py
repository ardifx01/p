"""
Blog Post #5: Enabling APIs for AI-First Systems — Membangun Backend untuk Agen AI
Terjemahan dan pengembangan dari artikel C# Corner “Enabling APIs for AI-First Systems”.
"""

from datetime import datetime
from django.conf import settings


blog_data = {
    "id": 5,
    "title": "Enabling APIs for AI-First Systems: Backend Bertenaga Agen AI",
    "description": (
        "Bagaimana cara merancang API agar siap dikonsumsi sistem AI-first (agen) "
        "menggunakan spesifikasi OpenAPI dan server MCP."
    ),
    "images": {
        "enabling_ai.jpg": f"{settings.BLOG_BASE_IMG_URL}/enabling_ai.jpg",
 
    },
    "author": "dhiff",
    "username": "dhiff",
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg",
    "created_at": datetime.strptime("2025-10-17T15:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-17T15:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),

    "content": [
        {
            "type": "p",
            "text": (
                "Dalam ekosistem AI-first modern, agen pintar seperti Claude, Copilot, dan ChatGPT kini dapat "
                "memanggil API secara langsung untuk menjalankan tugas. Artikel ini membahas bagaimana developer bisa "
                "membuat API yang siap dikonsumsi oleh agen AI, menggunakan kombinasi antara OpenAPI Spec dan "
                "MCP Server (Modular Command Protocol)."
            )
        },

        { "type": "h2", "text": "Gambaran Visual: Arsitektur API AI-First" },

        {
            "type": "p",
            "text": (
                "Berikut ilustrasi sederhana tentang alur komunikasi antara agen AI, MCP Server, dan backend API. "
                "Agen berinteraksi melalui protokol MCP, yang menjadi jembatan menuju API berbasis FastAPI atau "
                "sistem lain di sisi server."
            )
        },

        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/api_visual_diagram.webp",
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Diagram alur komunikasi AI Agent → MCP Server → Backend API"
        },

        {
            "type": "blockquote",
            "text": (
                "AI Agent → MCP Server → Backend API (FastAPI)\n\n"
                "OpenAPI Spec + MCP membuat agen AI memahami dan mengeksekusi fungsi API tanpa dokumentasi manual."
            )
        },

        { "type": "h2", "text": "Refresher: Konsep Dasar API dan HTTP Verbs" },

        {
            "type": "p",
            "text": (
                "Sebagian besar API berbasis HTTP dan menggunakan verb seperti GET, POST, PUT, PATCH, DELETE, dan OPTIONS — "
                "setiap verb merepresentasikan aksi terhadap resource tertentu."
            )
        },

        {
            "type": "pre",
            "lang": "python",
            "text": '''# Contoh API sederhana menggunakan FastAPI
from fastapi import FastAPI

app = FastAPI()
menu = ["Pizza", "Burger", "Pasta"]
current_order: str = None

@app.get("/menu")
def get_menu():
    return {"menu": menu}

@app.post("/order")
def place_order(item: str):
    global current_order
    current_order = item
    return {"message": f"Order placed for {item}"}

@app.delete("/order")
def delete_order():
    global current_order
    current_order = None
    return {"message": "Order deleted"}'''
        },

        {
            "type": "p",
            "text": (
                "API menyediakan endpoint yang bisa dipanggil agen AI untuk aksi layaknya manusia — menambah pesanan, "
                "membaca menu, atau menghapus pesanan."
            )
        },

        { "type": "h2", "text": "Menghubungkan API ke Agen Melalui OpenAPI Spec" },

        {
            "type": "p",
            "text": (
                "Agar agen AI mengerti cara menggunakan API tanpa instruksi manusia, API harus memiliki "
                "OpenAPI Specification (Swagger). File ini berisi detail endpoint, parameter, dan format respons. "
                "Agen dapat membaca spec ini dan memetakan fungsinya ke kemampuan mereka."
            )
        },

        { "type": "h2", "text": "Membangun MCP Server dari OpenAPI" },

        {
            "type": "p",
            "text": "Langkah berikutnya: mengubah OpenAPI Spec menjadi MCP Server sebagai perantara agen ↔ backend."
        },

        {
            "type": "pre",
            "lang": "python",
            "text": '''import httpx
from fastmcp import FastMCP

client = httpx.AsyncClient(base_url="http://localhost:8000")
openapi_spec = httpx.get("http://localhost:8000/openapi.json").json()

mcp = FastMCP.from_openapi(
    openapi_spec=openapi_spec,
    client=client,
    name="Restaurant MCP Server"
)

if __name__ == "__main__":
    mcp.run(transport="http", port=8001)'''
        },

        {
            "type": "p",
            "text": (
                "Dengan MCP Server aktif, agen seperti Claude atau Copilot mengakses API melalui MCP tanpa menulis ulang kode. "
                "Layer ini menjadi jembatan standar yang membuat backend lebih fleksibel dan aman."
            )
        },

        { "type": "h2", "text": "Keuntungan dan Tantangan Desain API AI-First" },

        {
            "type": "p",
            "text": """
<ul class='list-disc pl-6 space-y-1'>
  <li>✅ Kontrak API eksplisit via OpenAPI Spec.</li>
  <li>✅ Agen AI bisa mengeksekusi aksi langsung.</li>
  <li>✅ Lapisan MCP menjaga keamanan dan modularitas.</li>
  <li>⚠️ Overhead konfigurasi saat setup MCP server.</li>
  <li>⚠️ Potensi latensi tambahan antar layer.</li>
</ul>
"""
        },

        { "type": "h2", "text": "Kesimpulan" },

        {
            "type": "p",
            "text": (
                "Dalam dunia AI-first, backend tidak hanya melayani UI, tetapi juga agen cerdas. "
                "Dengan memadukan OpenAPI dan MCP, API dapat berinteraksi langsung dengan agen AI secara kontekstual dan aman."
            )
        },

        {
            "type": "p",
            "text": (
                "Desain ini menempatkan backend sebagai bagian dari ekosistem otonom di mana manusia dan mesin bekerja sejajar."
            )
        }
    ],

    # ===== metadata di bagian bawah (sesuai format yang kamu minta) =====
    "is_featured": False,
    "tags": ["API", "AI", "OpenAPI", "MCP", "Agents", "Backend", "FastAPI", "Automation"],
    "category": "API & AI",
    "read_time": 9,
    "views": 2000,
    "slug": "enabling-apis-for-ai-first-systems"
}
