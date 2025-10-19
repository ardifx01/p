"""
Blog Post #16: Cara Setup Golang di VSCode — Panduan Lengkap dengan 9 Langkah Bergambar 
Diterjemahkan dan disusun ulang dari artikel di C# Corner dengan semua tahapan visual.
"""

from datetime import datetime
from django.conf import settings

blog_data = {
    "id": 16, 
    "title": """Cara Setup Golang di VSCode""",
    "description": """Panduan bergambar langkah demi langkah menginstal Golang, men-setup VSCode, mengonfigurasi environment, serta menjalankan kode pertama menggunakan Go Modules.""",
    "images": {
        "golang_vscode_1.jpg": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_1.jpg", 
        "golang_vscode_2.jpg": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_2.jpg",
        "golang_vscode_3.jpg": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_3.jpg",
        "golang_vscode_4.jpg": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_4.jpg",
        "golang_vscode_5.jpg": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_5.jpg",
        "golang_vscode_6.jpg": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_6.jpg",
        "golang_vscode_7.jpg": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_7.jpg",
        "golang_vscode_8.jpg": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_8.jpg",
        "golang_vscode_9.jpg": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_9.jpg"
    },
    "created_at": datetime.strptime("2025-10-21T12:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-21T12:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "author": "dhiff",
    "username": "dhiff",
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg",

    "content": [
        {
            "type": "p",
            "text": (
                "Go (atau Golang) adalah bahasa pemrograman modern yang dikembangkan oleh Google, terkenal karena performa tinggi dan efisiensinya untuk backend dan sistem berskala besar. "
                "Panduan ini menjelaskan cara menyiapkan Golang di Visual Studio Code (VSCode), termasuk instalasi, konfigurasi, serta debugging kode pertama."
            )
        },

        { "type": "h2", "text": "Langkah 1: Instal Golang di Sistem" },
        {
            "type": "p",
            "text": (
                "Unduh installer Golang dari situs resmi [https://go.dev/dl/](https://go.dev/dl/), lalu jalankan instalasi. "
                "Setelah selesai, verifikasi dengan perintah berikut di terminal:"
            )
        },
        { "type": "pre", "lang": "bash", "text": "go version" },
        {
            "type": "p",
            "text": "Jika muncul hasil seperti `go version go1.23.1 windows/amd64`, maka instalasi berhasil."
        },
        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_1.jpg",
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Langkah 1: Memeriksa versi Golang setelah instalasi"
        },

        { "type": "h2", "text": "Langkah 2: Tambahkan Go ke PATH Environment" },
        {
            "type": "p",
            "text": (
                "Jika perintah `go` belum dikenali, kamu perlu menambahkan path instalasi Go ke environment variable sistem. "
                "Biasanya path-nya seperti `C:\\Go\\bin` di Windows atau `/usr/local/go/bin` di Linux/Mac."
            )
        },
        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_2.jpg", 
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Langkah 2: Menambahkan Golang ke PATH Environment"
        },

        { "type": "h2", "text": "Langkah 3: Instal Visual Studio Code" },
        {
            "type": "p",
            "text": (
                "Unduh VSCode dari [https://code.visualstudio.com](https://code.visualstudio.com) dan instal seperti biasa. "
                "Pastikan kamu dapat membuka VSCode dari Command Line dengan mengetik `code`."
            )
        },
        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_3.jpg", 
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Langkah 3: Menginstal Visual Studio Code"
        },

        { "type": "h2", "text": "Langkah 4: Instal Ekstensi Go di VSCode" },
        {
            "type": "p",
            "text": (
                "Buka VSCode → tekan `Ctrl + Shift + X` → cari *Go* → pilih **Go (by Google)** lalu klik **Install**. "
                "Ekstensi ini akan menambahkan fitur IntelliSense, linting, format otomatis, dan debugging."
            )
        },
        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_4.jpg", 
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Langkah 4: Instal ekstensi Go di VSCode"
        },

        { "type": "h2", "text": "Langkah 5: Buat Folder Proyek dan Inisialisasi Module" },
        {
            "type": "p",
            "text": (
                "Buat folder proyek baru bernama `hello_go_project`, buka di VSCode, dan jalankan perintah berikut:"
            )
        },
        { "type": "pre", "lang": "bash", "text": "go mod init example.com/hello_go_project" },
        {
            "type": "p",
            "text": (
                "Ini membuat file `go.mod` yang mendefinisikan module proyek Go kamu. "
                "VSCode akan otomatis mengenali dan mengaktifkan fitur Go Modules."
            )
        },
        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_5.jpg", 
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Langkah 5: Inisialisasi module Go di folder proyek"
        },

        { "type": "h2", "text": "Langkah 6: Buat File Program Pertama" },
        {
            "type": "p",
            "text": "Buat file bernama `main.go`, lalu isi dengan kode berikut:"
        },
        {
            "type": "pre",
            "lang": "go",
            "text": '''package main
import "fmt"

func main() {
    fmt.Println("Halo, Golang dari VSCode!")
}'''
        },
        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_6.jpg", 
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Langkah 6: Membuat dan menulis file main.go"
        },

        { "type": "h2", "text": "Langkah 7: Jalankan Program di Terminal VSCode" },
        {
            "type": "p",
            "text": (
                "Buka terminal di VSCode (Ctrl + `) dan jalankan:"
            )
        },
        { "type": "pre", "lang": "bash", "text": "go run main.go" },
        {
            "type": "p",
            "text": (
                "Jika berjalan dengan benar, kamu akan melihat output: `Halo, Golang dari VSCode!` 🎉"
            )
        },
        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_7.jpg", 
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Langkah 7: Menjalankan program Go di terminal VSCode"
        },

        { "type": "h2", "text": "Langkah 8: Install Tools Tambahan (Formatter & Debugger)" },
        {
            "type": "p",
            "text": (
                "VSCode biasanya menampilkan prompt untuk menginstal tools tambahan seperti `gofmt`, `dlv`, dan `gopls`. "
                "Klik **Install All** agar fitur seperti auto-format dan debugging aktif sepenuhnya."
            )
        },
        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_8.jpg", 
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Langkah 8: Instal tools tambahan Golang di VSCode"
        },

        { "type": "h2", "text": "Langkah 9: Debug Program Secara Langsung" },
        {
            "type": "p",
            "text": (
                "Klik ikon **Run and Debug** (Ctrl + Shift + D) di sidebar, pilih konfigurasi Go, dan tambahkan breakpoint di editor. "
                "Tekan F5 untuk menjalankan mode debug dan lihat bagaimana variabel serta flow dieksekusi langsung di VSCode."
            )
        },
        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/golang_vscode_9.jpg", 
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Langkah 9: Debugging kode Golang di VSCode"
        },

        { "type": "h2", "text": "Kesimpulan" },
        {
            "type": "p",
            "text": (
                "Dengan mengikuti sembilan langkah ini, kamu telah menyiapkan lingkungan pengembangan Golang yang profesional di VSCode. "
                "Kini kamu siap membuat API, CLI tool, atau sistem backend dengan efisiensi penuh dari ekosistem Go."
            )
        }
    ],

    "is_featured": False,
    "tags": ["Golang", "VSCode", "Backend", "Setup", "Development Tools"],
    "category": "Programming",
    "read_time": 10,
    "views": 0,
    "slug": "how-to-setup-golang-with-vscode"
}
