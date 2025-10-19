"""
Blog Post #14: CRUD MySQL dengan PHP + MVC Tanpa Framework
Generated from centralized blog data
"""

from datetime import datetime
from django.conf import settings

blog_data = {
    "id": 14,
    "title": """MySQL PHP MVC CRUD Without Framework""",
    "description": """Tutorial membangun aplikasi CRUD (Create, Read, Update, Delete) dengan pola MVC di PHP secara manual, tanpa menggunakan framework apa pun.""",
    "images": {
        "php_mvc_crud.jpg": f"{settings.BLOG_BASE_IMG_URL}/php_mvc_crud.jpg" 
    },
    "created_at": datetime.strptime("2025-10-20T14:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-20T14:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "author": "dhiff",
    "username": "dhiff",
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg",

    "content": [
        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "Tutorial ini ditujukan untuk kamu yang ingin memahami struktur MVC secara mendasar — tanpa bantuan framework seperti Laravel atau Symfony. "
                "Kita akan membuat aplikasi CRUD (Create, Read, Update, Delete) menggunakan PHP + MySQL, dan memahami bagaimana controller, model, dan view bekerja bersama."
            )
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Arsitektur MVC Sederhana"
        },

        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "Pola MVC membagi aplikasi menjadi tiga lapisan: Model untuk logika data / database, Controller untuk menangani request dan routing, dan View untuk tampilan antarmuka. "
                "Dengan memisahkan tanggung jawab ini, kode jadi lebih modular, mudah diuji, dan mudah dikembangkan."
            )
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Konfigurasi Database (config.php)"
        },

        {
            "type": "pre",
            "lang": "php",
            "text": '''<?php
class config {
    function __construct() {
        $this->host = "localhost";
        $this->user = "root";
        $this->pass = "welcome";
        $this->db   = "mydb13";
    }
}
?>'''
        },

        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "File `config.php` berisi kredensial koneksi ke MySQL — host, user, password, database. "
                "Informasi ini akan digunakan oleh model untuk membuka dan menutup koneksi database."
            )
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Model: sportsModel — Operasi CRUD"
        },

        {
            "type": "pre",
            "lang": "php",
            "text": '''class sportsModel {
    function __construct($consetup) {
        $this->host = $consetup->host;
        $this->user = $consetup->user;
        $this->pass = $consetup->pass;
        $this->db   = $consetup->db;
    }

    public function open_db() {
        $this->condb = new mysqli($this->host, $this->user, $this->pass, $this->db);
        if ($this->condb->connect_error) {
            die("Error in connection: " . $this->condb->connect_error);
        }
    }

    public function close_db() {
        $this->condb->close();
    }

    public function insertRecord($obj) {
        $this->open_db();
        $query = $this->condb->prepare("INSERT INTO sports (category, name) VALUES (?, ?)");
        $query->bind_param("ss", $obj->category, $obj->name);
        $query->execute();
        $last_id = $this->condb->insert_id;
        $query->close();
        $this->close_db();
        return $last_id;
    }

    public function selectRecord($id) {
        $this->open_db();
        if ($id > 0) {
            $query = $this->condb->prepare("SELECT * FROM sports WHERE id = ?");
            $query->bind_param("i", $id);
        } else {
            $query = $this->condb->prepare("SELECT * FROM sports");
        }
        $query->execute();
        $res = $query->get_result();
        $query->close();
        $this->close_db();
        return $res;
    }
}'''
        },

        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": "Dalam `sportsModel`, kita membuat koneksi, melakukan `INSERT` dengan parameter binding untuk keamanan (menghindari SQL Injection), dan metode `selectRecord` yang bisa memilih semua data atau berdasarkan `id`."
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "Controller & Routing (sportsController)"
        },

        {
            "type": "pre",
            "lang": "php",
            "text": '''$controller = new sportsController();
$controller->mvcHandler();

class sportsController {
    public function mvcHandler() {
        $act = isset($_REQUEST['act']) ? $_REQUEST['act'] : "list";
        switch ($act) {
            case "add":
                $this->insert();
                break;
            case "edit":
                $this->update();
                break;
            case "delete":
                $this->delete();
                break;
            default:
                $this->list();
        }
    }

    public function insert() {
        // logic insert
    }
    public function list() {
        // logic list
    }
}'''
        },

        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "Controller berfungsi menginterpretasi parameter `act` (action) dari URL, lalu memanggil metode yang sesuai (insert, update, delete, list). "
                "Fungsi `mvcHandler()` hadir sebagai titik awal routing sederhana tanpa framework."
            )
        },

        {
            "type": "h2",
            "class": "text-xl lg:text-2xl text-medium mt-4 mb-2",
            "text": "View: Tampilkan Data & Form Input"
        },

        {
            "type": "p",
            "class": "mb-4 text-sm md:text-base lg:text-lg",
            "text": (
                "Untuk bagian tampilan, aplikasi ini memiliki file HTML sederhana seperti `list.php` untuk menampilkan data dalam tabel, `insert.php` untuk form penambahan, dan `update.php` untuk form edit. View menerima data dari controller melalui objek model."
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
                "Dengan pendekatan ini, kamu bisa memahami naluri dasar framework MVC tanpa kompleksitas bawaan. "
                "Meski sederhana, aplikasi CRUD berbasis MVC tanpa framework membantumu menguasai alur request → controller → model → view sebelum berpindah ke framework besar."
            )
        }
    ],

    "is_featured": False,
    "tags": ["PHP", "MVC", "CRUD", "MySQL", "Tutorial"],
    "category": "Web Development",
    "read_time": 8,
    "views": 0,
    "slug": "mysql-php-mvc-crud-without-framework"
}
