"""
Blog Post #15: Membangun REST API dengan Gin Framework dan Golang 
Dilengkapi penjelasan tiap bagian kode untuk pemahaman mendalam.
"""

from datetime import datetime
from django.conf import settings

blog_data = {
    "id": 15, 
    "title": """Membangun REST API dengan Gin Framework dan Golang""",
    "description": """Panduan lengkap membuat REST API berbasis Golang menggunakan framework Gin: arsitektur proyek, validasi input, CRUD dengan GORM, dan praktik terbaik untuk production.""",
    "images": {
        "api-golang.jpg": f"{settings.BLOG_BASE_IMG_URL}/api-golang.jpg"
    },
    "created_at": datetime.strptime("2025-10-20T19:30:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-20T19:30:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "author": "dhiff",
    "username": "dhiff",
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg",

    "content": [
        {
            "type": "p",
            "text": "Gin adalah framework HTTP untuk Golang yang sangat ringan dan cepat. Ia populer karena kemudahan routing, integrasi JSON, serta dukungan middleware yang kuat. Artikel ini membahas langkah demi langkah membangun REST API CRUD berbasis Gin + GORM, lengkap dengan validasi, struktur proyek modular, serta tips deployment production."
        },
        {
            "type": "h2",
            "text": "Visualisasi Arsitektur"
        },
        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/gin_rest_api.webp",
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Diagram REST API Gin: Client → Router → Middleware → Handler → Service → Repository → Database"
        },
        {
            "type": "p",
            "text": "Gambar di atas memperlihatkan alur kerja REST API dengan pattern layered architecture. Request masuk ke router Gin, melewati middleware (seperti logger, recovery), lalu dikirim ke handler yang memanggil service. Service memproses logika bisnis dan berinteraksi dengan repository (GORM) untuk CRUD data."
        },
        {
            "type": "h2",
            "text": "1️⃣ Inisialisasi Proyek dan Dependensi"
        },
        {
            "type": "p",
            "text": "Pertama, buat folder proyek baru, inisialisasi module Go, dan install dependensi utama (Gin, GORM, validator, dotenv)."
        },
        {
            "type": "pre",
            "lang": "bash",
            "text": '''mkdir gin-books-api && cd gin-books-api
go mod init example.com/gin-books-api
go get github.com/gin-gonic/gin gorm.io/gorm gorm.io/driver/postgres
go get github.com/go-playground/validator/v10 github.com/joho/godotenv'''
        },
        {
            "type": "p",
            "text": "Gin untuk routing HTTP, GORM untuk ORM ke database, validator untuk validasi payload, dan godotenv untuk memuat variabel lingkungan dari file `.env`."
        },
        {
            "type": "h2",
            "text": "2️⃣ Struktur Folder Proyek"
        },
        {
            "type": "pre",
            "lang": "bash",
            "text": '''.
├─ cmd/server/main.go       # entry point
├─ internal/
│  ├─ config/               # konfigurasi aplikasi
│  ├─ database/             # koneksi DB
│  ├─ domain/book/          # model + DTO
│  ├─ handler/              # controller HTTP
│  ├─ middleware/           # logging & recovery
│  ├─ repository/           # query DB via GORM
│  └─ service/              # logika bisnis
└─ pkg/response/response.go # helper JSON response'''
        },
        {
            "type": "p",
            "text": "Struktur ini memisahkan concern: handler fokus HTTP, service untuk logic, repository untuk akses data. Pendekatan ini menjaga maintainability proyek besar."
        },
        {
            "type": "h2",
            "text": "3️⃣ File Konfigurasi dan Environment"
        },
        {
            "type": "pre",
            "lang": "bash",
            "text": '''# .env
APP_PORT=8080
DB_DSN=host=localhost user=postgres password=secret dbname=booksdb port=5432 sslmode=disable'''
        },
        {
            "type": "pre",
            "lang": "go",
            "text": '''// internal/config/config.go
package config

import ("os"; "log"; "github.com/joho/godotenv")

type Config struct {
\tAppPort string
\tDBDsn   string
}

func Load() *Config {
\t_ = godotenv.Load()
\tcfg := &Config{
\t\tAppPort: os.Getenv("APP_PORT"),
\t\tDBDsn:   os.Getenv("DB_DSN"),
\t}
\tif cfg.DBDsn == "" { log.Fatal("DB_DSN kosong") }
\treturn cfg
}'''
        },
        {
            "type": "p",
            "text": "File ini bertanggung jawab membaca environment variable dan menyiapkan konfigurasi. Dengan cara ini, kamu bisa menjalankan aplikasi di berbagai environment tanpa hardcode credential."
        },
        {
            "type": "h2",
            "text": "4️⃣ Koneksi Database dengan GORM"
        },
        {
            "type": "pre",
            "lang": "go",
            "text": '''// internal/database/postgres.go
package database

import ("gorm.io/gorm"; "gorm.io/driver/postgres"; "log")

func NewPostgres(dsn string) *gorm.DB {
\tdb, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
\tif err != nil { log.Fatalf("Gagal konek DB: %v", err) }
\treturn db
}'''
        },
        {
            "type": "p",
            "text": "Fungsi ini membuat instance koneksi database dengan driver Postgres. Jika gagal, program berhenti agar tidak melanjutkan dengan koneksi rusak."
        },
        {
            "type": "h2",
            "text": "5️⃣ Model dan DTO (Data Transfer Object)"
        },
        {
            "type": "pre",
            "lang": "go",
            "text": '''// internal/domain/book/model.go
package book
import "time"

type Book struct {
\tID uint `gorm:"primaryKey"`
\tTitle string
\tAuthor string
\tYear int
\tCreatedAt time.Time
\tUpdatedAt time.Time
}

type CreateBookDTO struct {
\tTitle string `validate:"required"`
\tAuthor string `validate:"required"`
\tYear int `validate:"gte=0"`
}'''
        },
        {
            "type": "p",
            "text": "Struct `Book` adalah representasi tabel database. DTO digunakan untuk validasi input dari pengguna agar tidak langsung memakai entity database mentah."
        },
        {
            "type": "h2",
            "text": "6️⃣ Repository Layer"
        },
        {
            "type": "pre",
            "lang": "go",
            "text": '''// internal/repository/book_repo.go
package repository
import ("gorm.io/gorm"; "example.com/gin-books-api/internal/domain/book")

type BookRepo struct { DB *gorm.DB }

func (r *BookRepo) FindAll() ([]book.Book, error) {
\tvar books []book.Book
\treturn books, r.DB.Find(&books).Error
}'''
        },
        {
            "type": "p",
            "text": "Repository menyimpan fungsi CRUD yang berinteraksi langsung dengan database. Dengan layer ini, logika data terpisah dari handler dan service."
        },
        {
            "type": "h2",
            "text": "7️⃣ Service Layer"
        },
        {
            "type": "pre",
            "lang": "go",
            "text": '''// internal/service/book_service.go
package service
import ("example.com/gin-books-api/internal/domain/book"; "example.com/gin-books-api/internal/repository")

type BookService struct { Repo *repository.BookRepo }

func (s *BookService) GetAllBooks() ([]book.Book, error) {
\treturn s.Repo.FindAll()
}'''
        },
        {
            "type": "p",
            "text": "Service layer mengelola logika bisnis, seperti validasi tambahan atau transformasi data sebelum dikirim ke handler. Dengan layer ini, unit test menjadi lebih mudah."
        },
        {
            "type": "h2",
            "text": "8️⃣ Handler & Routing"
        },
        {
            "type": "pre",
            "lang": "go",
            "text": '''// internal/handler/book_handler.go
package handler
import ("github.com/gin-gonic/gin"; "net/http"; "example.com/gin-books-api/internal/service")

type BookHandler struct { Service *service.BookService }

func (h *BookHandler) GetBooks(c *gin.Context) {
\tbooks, _ := h.Service.GetAllBooks()
\tc.JSON(http.StatusOK, gin.H{"data": books})
}'''
        },
        {
            "type": "p",
            "text": "Handler menerima request HTTP, memanggil service, dan mengirimkan response JSON ke client. Gin membuat binding data dan response JSON sangat mudah."
        },
        {
            "type": "h2",
            "text": "9️⃣ Middleware dan Server Entry Point"
        },
        {
            "type": "pre",
            "lang": "go",
            "text": '''// cmd/server/main.go
package main
import ("github.com/gin-gonic/gin"; "example.com/gin-books-api/internal/config"; "example.com/gin-books-api/internal/database"; "example.com/gin-books-api/internal/handler"; "example.com/gin-books-api/internal/repository"; "example.com/gin-books-api/internal/service")

func main() {
\tcfg := config.Load()
\tdb := database.NewPostgres(cfg.DBDsn)
\trepo := &repository.BookRepo{DB: db}
\tsvc := &service.BookService{Repo: repo}
\th := &handler.BookHandler{Service: svc}

\tr := gin.Default()
\tr.GET("/books", h.GetBooks)
\tr.Run(":" + cfg.AppPort)
}'''
        },
        {
            "type": "p",
            "text": "File utama ini menginisialisasi semua komponen (config, DB, repo, service, handler) dan menjalankan server Gin. Rute `/books` menampilkan semua data buku dari database."
        },
        {
            "type": "h2",
            "text": "🔟 Kesimpulan"
        },
        {
            "type": "p",
            "text": "Dengan arsitektur modular ini, REST API berbasis Gin menjadi scalable dan mudah diuji. Setiap lapisan punya tanggung jawab terpisah, memudahkan pengembangan tim besar. Langkah selanjutnya bisa menambahkan fitur JWT Auth, pagination, logging, dan caching."
        }
    ],

    "is_featured": False,
    "tags": ["Golang", "Gin", "REST API", "Backend", "GORM"],
    "category": "Backend Development",
    "read_time": 10,
    "views": 0,
    "slug": "create-rest-api-with-gin-framework-and-golang"
}
