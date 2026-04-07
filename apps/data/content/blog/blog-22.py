from datetime import datetime
from django.conf import settings

blog_data = {
    "id": 22,
    "title": """Menguasai Angular CLI: Konfigurasi Lanjutan untuk Workspace Multi-Project""",
    "description": """Panduan teknis mendalam tentang cara membangun, mengkonfigurasi, dan mengelola workspace multi-project menggunakan Angular CLI. Termasuk konsep dasar, struktur proyek, manipulasi angular.json, shared libraries, path alias, environment build, hingga best practice skala enterprise.""",
    "images": {
        "angular-workspace-diagram.jpg": f"{settings.BLOG_BASE_IMG_URL}/angular-workspace-diagram.jpg"
    },
    "created_at": datetime.strptime("2025-10-24T10:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-24T10:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "author": "dhiff",
    "username": "dhiff",
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg",

    "content": [

        # ——————————————————————————————————————————
        # INTRO / PENGERTIAN
        # ——————————————————————————————————————————
        {
            "type": "p",
            "text": "Dalam pengembangan aplikasi frontend skala besar, kebutuhan modularisasi, pemisahan domain bisnis, dan manajemen source code yang efisien menjadi hal yang sangat penting. Angular CLI menyediakan kemampuan powerful berupa workspace multi-project, yaitu satu struktur repository yang dapat menampung banyak aplikasi (apps) dan pustaka (libraries) di bawah satu konfigurasi terpadu. Pendekatan ini umum digunakan dalam pengembangan enterprise, monorepo architecture, white-label platform, dan ekosistem produk dengan banyak modul UI yang saling berbagi komponen."
        },

        {
            "type": "p",
            "text": "Artikel ini membahas secara mendalam bagaimana membangun workspace multi-project menggunakan Angular CLI: dimulai dari konsep dasar, struktur file, konfigurasi angular.json, path alias, pembuatan library bersama, hingga pengelolaan build dan integrasi CI/CD. Tutorial ini disusun agar dapat menjadi referensi jangka panjang bagi tim frontend atau arsitek aplikasi."
        },


        # ——————————————————————————————————————————
        # 1. PENGERTIAN WORKSPACE MULTI-PROJECT
        # ——————————————————————————————————————————
        {
            "type": "h2",
            "text": "1. Apa Itu Workspace Multi-Project dalam Angular?"
        },
        {
            "type": "p",
            "text": "Workspace multi-project adalah sebuah workspace Angular yang tidak hanya berisi satu aplikasi utama, tetapi dapat memuat beberapa aplikasi sekaligus seperti admin panel, client app, dashboard analitik, atau aplikasi white-label. Selain itu, workspace juga dapat berisi banyak library internal seperti UI components, utility helpers, state management module, dan sebagainya."
        },
        {
            "type": "p",
            "text": "Semua aplikasi dan library tersebut dikelola melalui satu berkas konfigurasi utama bernama angular.json. Hal ini memungkinkan konsistensi konfigurasi, pengurangan duplikasi codebase, dan pengelolaan dependency yang lebih efisien."
        },


        # ——————————————————————————————————————————
        # 2. MEMBUAT WORKSPACE TANPA APLIKASI DEFAULT
        # ——————————————————————————————————————————
        {
            "type": "h2",
            "text": "2. Membuat Workspace Baru Tanpa Aplikasi Default"
        },
        {
            "type": "p",
            "text": "Untuk membuat workspace multi-project yang rapi, kita perlu membuat workspace kosong tanpa aplikasi bawaan. Perintah berikut digunakan agar Angular CLI hanya membuat folder workspace tanpa app default:"
        },
        {
            "type": "pre",
            "lang": "bash",
            "text": "ng new enterprise-workspace --create-application=false"
        },
        {
            "type": "p",
            "text": "Output perintah di atas akan menghasilkan struktur folder minimal yang siap diisi aplikasi dan library baru. Ini sangat ideal untuk monorepo enterprise."
        },


        # ——————————————————————————————————————————
        # 3. STRUKTUR PROJECT & ANGULAR.JSON
        # ——————————————————————————————————————————
        {
            "type": "h2",
            "text": "3. Memahami Struktur Workspace dan Konfigurasi angular.json"
        },
        {
            "type": "p",
            "text": "Setelah workspace dibuat, Angular CLI menghasilkan folder projects/ yang menampung semua aplikasi dan library. File angular.json akan memiliki struktur dasar yang berisi daftar project, konfigurasi build, test, serve, lint, outputPath, environment file, dan sebagainya."
        },
        {
            "type": "pre",
            "lang": "json",
            "text": '''{
  "projects": {
    "admin-app": {
      "root": "projects/admin-app/",
      "sourceRoot": "projects/admin-app/src",
      "architect": {
        "build": {
          "builder": "@angular-devkit/build-angular:browser",
          "options": {
            "outputPath": "dist/admin-app"
          }
        }
      }
    }
  }
}'''
        },
        {
            "type": "p",
            "text": "Konfigurasi ini menentukan bagaimana aplikasi dibangun, lokasi aset, environment file yang digunakan, serta konfigurasi build spesifik per aplikasi."
        },


        # ——————————————————————————————————————————
        # 4. MEMBUAT APP DAN LIBRARY
        # ——————————————————————————————————————————
        {
            "type": "h2",
            "text": "4. Membuat Aplikasi dan Library dalam Workspace"
        },
        {
            "type": "p",
            "text": "Setelah workspace siap, aplikasi dapat dibuat dengan perintah:"
        },
        {
            "type": "pre",
            "lang": "bash",
            "text": "ng generate application admin-app"
        },
        {
            "type": "p",
            "text": "Untuk library internal (misalnya untuk berbagi komponen UI):"
        },
        {
            "type": "pre",
            "lang": "bash",
            "text": "ng generate library shared-ui"
        },
        {
            "type": "p",
            "text": "Library ini dapat di-import ke seluruh aplikasi dalam workspace tanpa perlu membuat package NPM terpisah."
        },


        # ——————————————————————————————————————————
        # 5. PATH MAPPING & PENGGUNAAN ALIAS
        # ——————————————————————————————————————————
        {
            "type": "h2",
            "text": "5. Konfigurasi Path Mapping dan Alias Import"
        },
        {
            "type": "p",
            "text": "Agar import komponen lebih bersih, kita dapat mengonfigurasi path alias di tsconfig.base.json:"
        },
        {
            "type": "pre",
            "lang": "json",
            "text": '''{
  "compilerOptions": {
    "paths": {
      "@shared/*": ["projects/shared-ui/src/lib/*"]
    }
  }
}'''
        },
        {
            "type": "p",
            "text": "Sehingga import komponen dapat ditulis seperti ini:"
        },
        {
            "type": "pre",
            "lang": "typescript",
            "text": "import { ButtonComponent } from '@shared/components';"
        },


        # ——————————————————————————————————————————
        # 6. ENVIRONMENT CONFIG & OUTPUT PATH
        # ——————————————————————————————————————————
        {
            "type": "h2",
            "text": "6. Mengatur Environment, Output Path, dan Build Variants"
        },
        {
            "type": "p",
            "text": "Setiap aplikasi dapat memiliki environment build berbeda seperti development, staging, dan production. Konfigurasi ini ditentukan di angular.json bagian architect.build.configurations. Misalnya:"
        },
        {
            "type": "pre",
            "lang": "json",
            "text": '''"configurations": {
  "production": {
    "fileReplacements": [
      {
        "replace": "src/environments/environment.ts",
        "with": "src/environments/environment.prod.ts"
      }
    ],
    "optimization": true
  }
}'''
        },


        # ——————————————————————————————————————————
        # 7. INTEGRASI CI/CD
        # ——————————————————————————————————————————
        {
            "type": "h2",
            "text": "7. Penerapan CI/CD untuk Workspace Multi-Project"
        },
        {
            "type": "p",
            "text": "Dalam CI/CD, build dapat ditargetkan ke aplikasi tertentu saja tanpa mem-build seluruh project. Contoh workflow GitHub Actions:"
        },
        {
            "type": "pre",
            "lang": "yaml",
            "text": '''- name: Build Admin App
  run: ng build admin-app --configuration production'''
        },
        {
            "type": "p",
            "text": "Hal ini mempercepat pipeline dan mengurangi beban server CI."
        },


        # ——————————————————————————————————————————
        # 8. TROUBLESHOOTING
        # ——————————————————————————————————————————
        {
            "type": "h2",
            "text": "8. Troubleshooting Umum"
        },
        {
            "type": "p",
            "text": "1. Error path alias tidak ditemukan — pastikan path di tsconfig.base.json benar.  \n2. Build gagal pada library — lakukan re-export semua komponen di public-api.ts.  \n3. Aplikasi tidak muncul saat `ng serve` — periksa configurasi serve.targets di angular.json.  \n4. Perubahan library tidak terbaca — jalankan `ng build shared-ui --watch` atau gunakan path alias."
        },


        # ——————————————————————————————————————————
        # 9. KESIMPULAN
        # ——————————————————————————————————————————
        {
            "type": "h2",
            "text": "9. Kesimpulan"
        },
        {
            "type": "p",
            "text": "Workspace multi-project Angular memberikan fleksibilitas besar dalam pengembangan aplikasi skala besar dengan struktur modular dan efisien. Dengan pengaturan Angular CLI yang tepat, konfigurasi angular.json yang rapih, integrasi path alias, dan pemanfaatan library internal, tim dapat membangun platform frontend yang scalable, maintainable, dan siap untuk enterprise production."
        }
    ],

    "is_featured": False,
    "tags": ["Angular", "Angular CLI", "Workspace", "Frontend Architecture", "Monorepo"],
    "category": "Frontend Development",
    "read_time": 16,
    "views": 0,
    "slug": "menguasai-angular-cli-konfigurasi-lanjutan-workspace-multi-project"
}
