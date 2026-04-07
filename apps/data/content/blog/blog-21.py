from datetime import datetime
from django.conf import settings

blog_data = {
    "id": 21,
    "title": """Integrasi Firebase ke Aplikasi React Native""",
    "description": """Panduan lengkap mengintegrasikan Firebase dengan aplikasi React Native: mulai dari konfigurasi proyek, instalasi paket, setup Android/iOS, hingga implementasi autentikasi email-password.""",
    "images": {
        "firebase-reactnative-setup.jpg": f"{settings.BLOG_BASE_IMG_URL}/firebase-reactnative-setup.jpg"
    },
    "created_at": datetime.strptime("2025-10-23T11:30:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-23T11:30:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "author": "dhiff",
    "username": "dhiff",
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg",

    "content": [

        {
            "type": "p",
            "text": "Firebase menyediakan backend siap pakai untuk autentikasi, database, dan penyimpanan data, sehingga sangat ideal untuk aplikasi React Native. Artikel ini memberikan panduan integrasi Firebase ke aplikasi React Native berdasarkan langkah-langkah dari dokumentasi dan praktik umum yang digunakan developer."
        },

        {
            "type": "h2",
            "text": "1. Membuat Proyek Firebase"
        },
        {
            "type": "p",
            "text": "Masuk ke Firebase Console, pilih 'Add Project', masukkan nama proyek, lalu selesaikan proses setup. Setelah proyek dibuat, registrasikan aplikasi Android dan iOS agar masing-masing platform dapat terhubung dengan Firebase."
        },

        {
            "type": "h2",
            "text": "2. Instalasi Paket Firebase di React Native"
        },
        {
            "type": "p",
            "text": "Untuk React Native CLI, gunakan paket resmi dari @react-native-firebase:"
        },
        {
            "type": "pre",
            "lang": "bash",
            "text": "npm install @react-native-firebase/app @react-native-firebase/auth"
        },
        {
            "type": "p",
            "text": "Jika menggunakan Expo, instalasi berbeda karena Expo memiliki integrasi melalui SDK Firebase:"
        },
        {
            "type": "pre",
            "lang": "bash",
            "text": "expo install firebase"
        },

        {
            "type": "h2",
            "text": "3. Konfigurasi Firebase untuk Android"
        },
        {
            "type": "p",
            "text": "Pada Firebase Console, pilih setup aplikasi Android, masukkan applicationId, kemudian download file google-services.json. File tersebut harus ditempatkan pada direktori android/app/."
        },
        {
            "type": "p",
            "text": "Tambahkan konfigurasi berikut pada android/build.gradle:"
        },
        {
            "type": "pre",
            "lang": "gradle",
            "text": "classpath 'com.google.gms:google-services:4.3.15'"
        },
        {
            "type": "p",
            "text": "Kemudian pada android/app/build.gradle:"
        },
        {
            "type": "pre",
            "lang": "gradle",
            "text": "apply plugin: 'com.google.gms.google-services'"
        },

        {
            "type": "h2",
            "text": "4. Konfigurasi Firebase untuk iOS"
        },
        {
            "type": "p",
            "text": "Unduh file GoogleService-Info.plist dari Firebase Console dan drag ke folder iOS project melalui Xcode. Lanjutkan dengan instalasi CocoaPods:"
        },
        {
            "type": "pre",
            "lang": "bash",
            "text": "cd ios && pod install && cd .."
        },

        {
            "type": "h2",
            "text": "5. Mengaktifkan Authentication di Firebase"
        },
        {
            "type": "p",
            "text": "Masuk ke menu Authentication pada Firebase Console, buka tab Sign-in method, lalu aktifkan Email/Password. Metode autentikasi lain dapat diaktifkan sesuai kebutuhan aplikasi."
        },

        {
            "type": "h2",
            "text": "6. Contoh Implementasi Login dan Signup"
        },
        {
            "type": "pre",
            "lang": "javascript",
            "text": '''import auth from '@react-native-firebase/auth';

export const signupUser = async (email, password) => {
  try {
    await auth().createUserWithEmailAndPassword(email, password);
  } catch (error) {
    console.log(error);
  }
};

export const loginUser = async (email, password) => {
  try {
    await auth().signInWithEmailAndPassword(email, password);
  } catch (error) {
    console.log(error);
  }
};'''
        },

        {
            "type": "h2",
            "text": "7. Best Practices Keamanan"
        },
        {
            "type": "p",
            "text": "1. Jangan menyimpan credential dalam bentuk hard-coded. Gunakan environment variables.\n2. Aktifkan email verification untuk mencegah penyalahgunaan akun.\n3. Implementasikan Firebase Security Rules untuk Firestore atau Realtime Database.\n4. Gunakan monitoring Firebase untuk memantau sign-in mencurigakan.\n5. Uji aplikasi pada Android dan iOS setelah integrasi untuk memastikan kompatibilitas."
        },

        {
            "type": "h2",
            "text": "8. Kesimpulan"
        },
        {
            "type": "p",
            "text": "Integrasi Firebase dengan React Native memberikan fondasi backend yang kuat tanpa memerlukan server sendiri. Dengan mengikuti langkah-langkah konfigurasi di atas dan mengimplementasikan best practices keamanan, aplikasi dapat dibangun dengan lebih cepat dan tetap aman."
        }
    ],

    "is_featured": False,
    "tags": ["React Native", "Firebase", "Mobile Development", "Authentication"],
    "category": "Mobile Development",
    "read_time": 8,
    "views": 0,
    "slug": "integrasi-firebase-react-native"
}
