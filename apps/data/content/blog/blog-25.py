from datetime import datetime
from django.conf import settings

blog_data = {
    "id": 25,
    "title": "Mengenal Model Context Protocol (MCP): Standar Baru Integrasi LLM dengan Data dan Tools Eksternal",
    "description": "Ulasan komprehensif tentang Model Context Protocol (MCP): konsep dasar, motivasi, arsitektur, cara kerja, contoh implementasi, tantangan teknis, dan perannya dalam membangun agen AI generasi berikutnya.",
    "images": {
        "mcp-model-context-protocol-overview.jpg": f"{settings.BLOG_BASE_IMG_URL}/mcp-model-context-protocol-overview.jpg"
    },
    "created_at": datetime.strptime("2025-10-27T10:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-27T10:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),

    "author": "dhiff",
    "username": "dhiff",
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg",

    "content": [

        {
            "type": "p",
            "class": "mb-4 text-base lg:text-lg",
            "text":
            "Model Context Protocol (MCP) adalah standar baru yang mulai banyak diadopsi oleh ekosistem AI modern. "
            "Tujuannya sederhana namun fundamental: menyediakan cara yang aman, terstruktur, dan seragam untuk "
            "menghubungkan model bahasa besar (LLM) dengan data, API, sistem file, basis data, maupun tools eksternal. "
            "Daripada membangun integrasi custom yang berbeda untuk setiap LLM atau aplikasi, MCP menawarkan protokol "
            "universal yang bisa dipakai oleh berbagai host, agent, dan developer."
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl font-semibold mt-6 mb-3",
            "text": "1. Mengapa MCP Diciptakan?"
        },
        {
            "type": "p",
            "class": "mb-4 text-base lg:text-lg",
            "text":
            "AI modern bekerja lebih baik ketika bisa memahami konteks dunia nyata: data produk, dokumen internal, "
            "tiket Jira, skema database, atau struktur kode proyek. Namun sebelum MCP, interaksi LLM dengan sistem "
            "eksternal sangat berantakan. Setiap vendor AI (OpenAI, Anthropic, Google) memiliki mekanisme integrasi "
            "sendiri, dan setiap developer membuat middleware custom yang sulit dipelihara."
        },

        {
            "type": "p",
            "class": "mb-4 text-base lg:text-lg",
            "text":
            "MCP muncul untuk menyelesaikan masalah ini. Ia menciptakan bahasa yang sama antara model dan dunia luar. "
            "Dengan protokol standar, model dapat meminta data, menjalankan tools, mengeksekusi perintah, dan "
            "melakukan reasoning berdasarkan konteks real-time secara aman dan terkontrol."
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl font-semibold mt-6 mb-3",
            "text": "2. Inti Konsep MCP"
        },

        {
            "type": "p",
            "class": "mb-3",
            "text": "• MCP adalah protokol komunikasi dua arah antara \"klien\" (host, aplikasi, agen) dan \"server\" (penyedia data atau tools)."
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• LLM tidak langsung memanggil API; ia meminta konteks melalui klien MCP, lalu klien berbicara dengan server MCP."
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• Server MCP bertanggung jawab menyediakan akses ke API, database, filesystem, dan layanan eksternal lainnya."
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• Klien MCP menjaga keamanan, autentikasi, sandboxing, serta menentukan alat mana yang boleh dipakai model."
        },

        {
            "type": "p",
            "class": "mb-4 text-base lg:text-lg",
            "text":
            "Dengan cara ini, LLM bisa menjadi \"otak\", sedangkan MCP menyediakan \"indera\" dan \"tangan\" untuk membaca "
            "konteks dunia nyata dan melakukan tindakan nyata."
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl font-semibold mt-6 mb-3",
            "text": "3. Arsitektur MCP: Klien, Server, dan Tools"
        },

        {
            "type": "p",
            "class": "mb-3",
            "text": "• Klien MCP adalah host yang menjalankan agen atau UI, seperti editor, aplikasi desktop, atau server aplikasi."
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• Server MCP adalah komponen yang menyediakan data dan fungsi: API bisnis, database, file explorer, Git repo, dll."
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• Tools MCP adalah fungsi yang dapat dijalankan oleh model: query DB, baca file, update file, generate code, dsb."
        },

        {
            "type": "p",
            "class": "mb-4 text-base lg:text-lg",
            "text":
            "Hubungan keduanya sederhana: klien MCP berbicara ke server MCP melalui protokol standar, dan model hanya "
            "berinteraksi melalui perintah yang telah diamanatkan oleh klien."
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl font-semibold mt-6 mb-3",
            "text": "4. Cara Kerja MCP (Alur Lengkap)"
        },

        {
            "type": "p",
            "class": "mb-3",
            "text": "• Model meminta sesuatu, misalnya: “Tolong carikan tiket Jira yang statusnya In Progress minggu ini.”"
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• Klien MCP mengidentifikasi bahwa ada server MCP ‘jira’ yang memiliki tool dan data yang diperlukan."
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• Klien mengirim request ke server MCP Jira via protokol MCP."
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• Server MCP menghubungi API Jira, memproses data, dan mengembalikan response terstruktur."
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• Klien MCP menyampaikan hasilnya kembali ke model dalam bentuk konteks yang dipahami oleh LLM."
        },

        {
            "type": "p",
            "class": "mb-4 text-base lg:text-lg",
            "text":
            "Dengan cara ini, AI dapat bekerja dalam domain nyata tanpa harus memegang API-key secara langsung atau "
            "punya akses penuh terhadap seluruh sistem. Klien MCP menjadi firewall cerdas."
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl font-semibold mt-6 mb-3",
            "text": "5. Contoh Penggunaan MCP di Dunia Nyata"
        },

        {
            "type": "p",
            "class": "mb-3",
            "text": "• Mendesain UI di Figma lalu meminta AI menghasilkan kode React/Flutter berdasarkan file desain."
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• Agen AI untuk DevOps membaca log sistem, mencari error terbaru, dan membuatkan patch otomatis."
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• Menghubungkan database perusahaan agar AI dapat membuat query SQL real-time untuk laporan analitis."
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• Sistem AI personal assistant yang bisa membaca kalender, dokumen, dan file lokal dengan sandbox aman."
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• Integrasi Git repository untuk code review otomatis dan pembuatan PR langsung dari model."
        },

        {
            "type": "p",
            "class": "mb-4 text-base lg:text-lg",
            "text":
            "Semua ini sebelumnya memerlukan integrasi manual yang berat. Dengan MCP, semua menjadi standarisasi "
            "yang siap digunakan ulang di berbagai host."
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl font-semibold mt-6 mb-3",
            "text": "6. Contoh Struktur Server MCP (Python)"
        },

        {
            "type": "pre",
            "lang": "python",
            "text": """from mcp.server import Server
import requests

server = Server("jira")

@server.tool()
def get_issues(status: str):
    resp = requests.get(f"https://jira.company.com/issues?status={status}")
    return resp.json()

if __name__ == "__main__":
    server.run()"""
        },

        {
            "type": "p",
            "class": "mb-4 text-base lg:text-lg",
            "text":
            "Setelah server MCP dibuat, ia dapat dihubungkan oleh berbagai klien MCP, termasuk agen AI dalam aplikasi internal."
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl font-semibold mt-6 mb-3",
            "text": "7. Tantangan dan Kebutuhan Keamanan"
        },

        {
            "type": "p",
            "class": "mb-3",
            "text": "• Akses berlebihan pada server MCP bisa membuka pintu ke data sensitif."
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• Tools yang dapat melakukan perubahan file atau menjalankan command harus dibatasi ketat."
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• Perlu ada audit log untuk semua permintaan MCP yang terjadi di sistem."
        },
        {
            "type": "p",
            "class": "mb-3",
            "text": "• Sandbox harus memisahkan akses API agar model tidak bisa melakukan aksi yang tidak diizinkan."
        },

        {
            "type": "p",
            "class": "mb-4 text-base lg:text-lg",
            "text":
            "Keamanan menjadi prioritas besar karena MCP membuat LLM memiliki kemampuan untuk melihat data nyata dan "
            "menjalankan action di dunia nyata."
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl font-semibold mt-6 mb-3",
            "text": "8. Masa Depan MCP dan Ekosistemnya"
        },

        {
            "type": "p",
            "class": "mb-4 text-base lg:text-lg",
            "text":
            "MCP diprediksi menjadi fondasi integrasi AI modern. Semakin banyak model, aplikasi, IDE, dan tools yang "
            "mengadopsinya, semakin mudah developer membangun agen AI yang benar-benar terhubung dengan sistem nyata. "
            "Ecosystem-nya berkembang cepat dengan library Python, TypeScript, Rust, dan berbagai server open-source "
            "untuk database, ticketing, desain, DevOps, dan banyak lagi."
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl font-semibold mt-6 mb-3",
            "text": "9. Kesimpulan"
        },

        {
            "type": "p",
            "class": "mb-4 text-base lg:text-lg",
            "text":
            "Model Context Protocol membawa pendekatan baru dalam membangun aplikasi AI. "
            "Ia menghubungkan model dengan data dan tools nyata secara standar, memungkinkan agen AI bekerja "
            "lebih efektif, aman, dan terstruktur. Dengan MCP, developer dapat menciptakan sistem AI yang benar-benar "
            "memahami konteks dan dapat melakukan tindakan berdasarkan informasi real-time."
        }
    ],

    "is_featured": False,
    "tags": ["MCP", "Model Context Protocol", "LLM Tools", "AI Workflow", "AI Integration"],
    "category": "AI & Development",
    "read_time": 13,
    "views": 0,
    "slug": "mcp-model-context-protocol"
}
