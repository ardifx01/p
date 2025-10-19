"""
Blog Post #7: SQL Topics Penting untuk Wawancara Data Science.
"""

from datetime import datetime
from django.conf import settings


blog_data = {
    "id": 7,
    "title": "Topik SQL yang Wajib Dikuasai untuk Wawancara Data Science",
    "description": (
        "Daftar konsep SQL yang paling sering ditanyakan dalam wawancara Data Science, "
        "dengan contoh query nyata dan tips efektif untuk latihan."
    ),

    "images": {
        "sql_interview.jpg": f"{settings.BLOG_BASE_IMG_URL}/sql_interview.jpg", 
    },

    "author": "dhiff",
    "username": "dhiff",
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg",

    "created_at": datetime.strptime("2025-10-18T10:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-18T10:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),

    "content": [
        {
            "type": "p",
            "text": (
                "SQL tetap menjadi bahasa paling penting yang harus dikuasai oleh setiap calon Data Scientist. "
                "Selain Python dan statistik, kemampuan menulis query yang efisien dan bersih sering menjadi penentu "
                "sukses atau tidaknya dalam wawancara Data Science. Artikel ini membahas topik SQL terpenting "
                "yang wajib kamu pahami, lengkap dengan contoh query dan alasan mengapa hal itu sering muncul di interview."
            )
        },

        { "type": "h2", "text": "Gambaran Visual: Hierarki Topik SQL" },

        {
            "type": "p",
            "text": (
                "Berikut ilustrasi hubungan antar topik SQL yang sering diuji dalam wawancara: mulai dari dasar SELECT, "
                "penggabungan tabel, hingga analisis dengan fungsi jendela."
            )
        },

        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/sql_interview.jpg",
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Diagram visual topik SQL untuk Data Science Interview"
        },

        { "type": "h2", "text": "1. Dasar-Dasar SQL" },

        {
            "type": "p",
            "text": (
                "Topik pertama yang selalu diuji adalah kemampuan dasar: `SELECT`, `WHERE`, `ORDER BY`, dan `LIMIT`. "
                "Interviewers ingin melihat apakah kamu paham bagaimana mengambil data secara efisien."
            )
        },

        {
            "type": "pre",
            "lang": "sql",
            "text": '''SELECT name, age
FROM employees
WHERE age > 30
ORDER BY age DESC
LIMIT 5;'''
        },

        { "type": "h2", "text": "2. JOIN dan Relasi Antar Tabel" },

        {
            "type": "p",
            "text": (
                "Hampir semua dataset di dunia nyata tersebar di banyak tabel. Karena itu, JOIN menjadi skill penting "
                "untuk menggabungkan data dengan benar."
            )
        },

        {
            "type": "pre",
            "lang": "sql",
            "text": '''SELECT c.customer_id, o.order_id
FROM customers c
INNER JOIN orders o
  ON c.customer_id = o.customer_id;'''
        },

        {
            "type": "blockquote",
            "text": (
                "JOIN adalah fondasi analitik relasional. Ketahui perbedaan antara INNER, LEFT, RIGHT, dan FULL JOIN."
            )
        },

        { "type": "h2", "text": "3. Agregasi & GROUP BY" },

        {
            "type": "p",
            "text": (
                "Setelah menggabungkan data, kamu perlu meringkasnya. Gunakan fungsi agregasi seperti `COUNT()`, `SUM()`, "
                "`AVG()`, `MIN()`, dan `MAX()` bersama `GROUP BY`."
            )
        },

        {
            "type": "pre",
            "lang": "sql",
            "text": '''SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;'''
        },

        { "type": "h2", "text": "4. Subquery & CTE (Common Table Expressions)" },

        {
            "type": "p",
            "text": (
                "Subquery dan CTE sering digunakan untuk menyusun analisis kompleks menjadi langkah yang lebih mudah dibaca. "
                "CTE memudahkan debugging query panjang."
            )
        },

        {
            "type": "pre",
            "lang": "sql",
            "text": '''WITH high_earners AS (
  SELECT name, salary
  FROM employees
  WHERE salary > 100000
)
SELECT * FROM high_earners WHERE name LIKE 'A%';'''
        },

        { "type": "h2", "text": "5. Window Functions (Analisis Tingkat Lanjut)" },

        {
            "type": "p",
            "text": (
                "Fungsi jendela memberikan kemampuan analisis tambahan seperti ranking, moving average, dan cumulative sum. "
                "Ini topik yang sangat disukai interviewer karena menunjukkan kemampuan analitik SQL tingkat lanjut."
            )
        },

        {
            "type": "pre",
            "lang": "sql",
            "text": '''SELECT
  product_id,
  RANK() OVER (PARTITION BY category ORDER BY SUM(amount) DESC) AS rank_in_category
FROM sales
GROUP BY product_id, category
HAVING RANK() <= 3;'''
        },

        { "type": "h2", "text": "6. Soal Populer dan Tips Latihan" },

        {
            "type": "p",
            "text": (
                "Beberapa soal SQL yang paling sering muncul dalam interview:\n"
                "- Gaji tertinggi ke-2\n"
                "- Pelanggan dengan lebih dari 5 order\n"
                "- Produk dengan penjualan tertinggi per kategori\n"
                "- Karyawan tanpa manajer (NULL manager_id)"
            )
        },

        {
            "type": "pre",
            "lang": "sql",
            "text": '''-- Gaji tertinggi ke-2
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Pelanggan dengan lebih dari 5 order
SELECT customer_id, COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) > 5;'''
        },

        { "type": "h2", "text": "Kesimpulan" },

        {
            "type": "p",
            "text": (
                "Untuk wawancara Data Science, fokus pada dasar hingga analisis lanjutan: SELECT, JOIN, GROUP BY, CTE, "
                "dan Window Functions. Latihan dengan dataset publik seperti HR Dataset atau Northwind akan membantu kamu "
                "menguasai logika bisnis dan efisiensi query."
            )
        }
    ],

    # Metadata akhir (penting agar konsisten)
    "is_featured": False,
    "tags": ["SQL", "Data Science", "Interview", "Database", "Query Optimization"],
    "category": "Data Science",
    "read_time": 8,
    "views": 0,
    "slug": "sql-topics-for-data-science-interviews"
}
