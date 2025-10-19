"""
Blog Post #8: Mengirim Alert WhatsApp Otomatis dari Google Form via Twilio . 
"""

from datetime import datetime
from django.conf import settings


blog_data = {
    "id": 7,
    "title": "Notifikasi WhatsApp Otomatis dari Google Form dengan Twilio",
    "description": (
        "Cara mengirim alert WhatsApp secara otomatis saat ada respon Google Form, menggunakan Google Sheets, Make, dan Twilio WhatsApp API."
    ),
    "images": {
        "whatsapp_form_alert.jpg": f"{settings.BLOG_BASE_IMG_URL}/whatsapp_form_alert.jpg", 
    },
    "author": "dhiff",
    "username": "dhiff",
    "author_image": f"{settings.BASE_URL}/static/img/pp.jpg",
    "created_at": datetime.strptime("2025-10-18T18:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),
    "updated_at": datetime.strptime("2025-10-18T18:00:00+07:00", "%Y-%m-%dT%H:%M:%S%z"),

    "content": [
        {
            "type": "p",
            "text": (
                "Bayangkan setiap kali seseorang mengisi Google Form, kamu langsung menerima notifikasi di WhatsApp — bukan hanya di email. "
                "Dengan Twilio, Google Sheets / Forms, dan Make.com, itu bisa diwujudkan dalam hitungan menit. Artikel ini menjelaskan langkah-langkah lengkapnya."
            )
        },

        {
            "type": "h2",
            "text": "Ilustrasi Arus Data Visual"
        },

        {
            "type": "img",
            "src": f"{settings.BLOG_BASE_IMG_URL}/whatsapp_flow_diagram.webp",
            "class": "rounded-xl border border-zinc-700 my-4 shadow-lg",
            "alt": "Diagram alur: Form → Sheet → Make → Twilio → WhatsApp"
        },

        {
            "type": "blockquote",
            "text": (
                "Google Form → Google Sheets → Make scenario → Twilio WhatsApp → Notifikasi ke penerima"
            )
        },

        {
            "type": "h2",
            "text": "Ringkasan Alur dan Komponen"
        },

        {
            "type": "p",
            "text": (
                "Alur notifikasi WhatsApp tersebut dibangun dari beberapa bagian: "
                "Google Forms menyimpan jawaban di Sheets, Make memantau baris baru, dan Twilio mengirim pesan WhatsApp berbasis template atau session."
            )
        },

        {
            "type": "h2",
            "text": "Langkah Konfigurasi"
        },

        {
            "type": "p",
            "text": "Berikut langkah umum yang harus diikuti:"
        },

        {
            "type": "ul",
            "class": "list-disc pl-6 space-y-1",
            "items": [
                "Buat Google Form dan hubungkan ke Google Sheets.",
                "Siapkan Twilio dengan WhatsApp sandbox atau sender bisnis.",
                "Bangun skenario Make.com: Watch Rows → Format Data → Twilio Send Message.",
                "Tambahkan deduplication untuk mencegah pengiriman ganda.",
                "Pastikan format nomor telepon mengikuti E.164 (contoh: +6281234567890).",
                "Gunakan template WhatsApp jika mengirim ke kontak baru."
            ]
        },

        {
            "type": "h2",
            "text": "Contoh Snippet: Google Apps Script → Twilio"
        },

        {
            "type": "pre",
            "lang": "javascript",
            "text": '''function onFormSubmit(e) {
  const TWILIO_ACCOUNT_SID = 'YOUR_SID';
  const TWILIO_AUTH_TOKEN = 'YOUR_TOKEN';
  const FROM = 'whatsapp:+14155238886'; // contoh sandbox Twilio
  const TO = 'whatsapp:+<recipient_number>';

  const payload = {
    From: FROM,
    To: TO,
    Body:
      'New Form Submission:\\n' +
      `Name: ${e.values[1]}\\n` +
      `Email: ${e.values[2]}\\n` +
      `Message: ${e.values[3]}`
  };

  const options = {
    method: 'post',
    payload: payload,
    headers: {
      Authorization: 'Basic ' + Utilities.base64Encode(TWILIO_ACCOUNT_SID + ':' + TWILIO_AUTH_TOKEN)
    }
  };

  UrlFetchApp.fetch('https://api.twilio.com/2010-04-01/Accounts/' + TWILIO_ACCOUNT_SID + '/Messages.json', options);
}'''
        },

        {
            "type": "h2",
            "text": "Pertimbangan & Batasan"
        },

        {
            "type": "p",
            "text": (
                "Beberapa hal yang harus diperhatikan:\n"
                "- Akun Twilio trial memiliki batasan jumlah pesan dan nomor tujuan.\n"
                "- Template WhatsApp diperlukan jika pesan dikirim ke kontak yang belum mengirim pesan ke Anda dalam 24 jam.\n"
                "- Pastikan pengguna telah memberikan izin / opt-in untuk notifikasi.\n"
                "- Gunakan deduplikasi agar tidak mengirim lebih dari satu notifikasi per jawaban."
            )
        },

        {
            "type": "h2",
            "text": "Kesimpulan"
        },

        {
            "type": "p",
            "text": (
                "Mengintegrasikan Google Forms dan WhatsApp via Twilio membuka peluang automasi real-time. "
                "Dengan alur yang tepat — Form → Sheet → Make → Twilio — kamu bisa membuat sistem notifikasi cerdas dashboard kepada pengguna atau tim."
            )
        }
    ],

    "is_featured": False,
    "tags": ["WhatsApp", "Google Forms", "Twilio", "Automation", "Notifications"],
    "category": "Automation & Notifications",
    "read_time": 6,
    "views": 0,
    "slug": "whatsapp-alerts-google-form-twilio"
}
