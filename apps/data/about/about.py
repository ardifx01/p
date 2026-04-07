from django.conf import settings
from datetime import datetime
import pytz

class AboutData:
    @staticmethod
    def is_working_hours():
        jakarta_tz = pytz.timezone("Asia/Jakarta")
        now = datetime.now(jakarta_tz)
        is_weekday = now.weekday() < 5
        is_work_hour = 15 <= now.hour < 20
        return is_weekday and is_work_hour
    @classmethod
    def get_about_data(cls):
        return {
            "name": "Muhammad Nadhif",
            "first_name": "Muhammad Nadhif",
            "last_name": "Karim",
            "username": "ardifx01", # GitHub username 
            "aka": "mnk",

            "image_url": f"{settings.BASE_URL}/static/img/pp.jpg", 
            "personal_website": "https://mnkdigital.tech",
            "cv": "#", 
            "cv_latest": "#", 
            "cv_copy": "#", 
            "role": "Fullstack Programmer", 
            "is_active": cls.is_working_hours(),
            "is_open_to_work": False,
            "is_hiring": True, 
            "short_description": "a quiet space where machine learning, open-source, and reflections converge.",
            "short_bio_old": "I explore through code, share with empathy, and reflect on every challenge. My work weaves machine learning, web creation, and open-source. This site archives the curious, the technical, and the quietly thoughtful.",
            "short_bio": "I explore through code, share with empathy, and reflect on every challenge. My work weaves machine learning, web creation, and open source. I thrive on collaborating with teams to develop smart, user centered AI and web solutions that blend function with clarity.",
            "short_cta": "Stay a while and see what lives beyond the code.",
            "long_description": "I'm a machine learning engineer and web developer, building AI apps and slick websites that solve real problems. I've mentored 50+ coders at DBS Foundation's Coding Camp and guided 100+ interns at GAOTek Inc. I've shipped 30+ projects using TensorFlow, PyTorch, and more. I'm all in on using AI to tackle big challenges fast, growing Copilot ID, and dropping value in open-source communities.", 
            "stories": [
                "I’m Nadhif, known as Dhiff or Rim — a software developer passionate about machine learning, backend engineering, and web development, based in Central Java, Indonesia. At Copilot ID, I focus on building intelligent systems and high-performance applications using Python, PHP, Go (Golang), TypeScript, and backend frameworks like Django and Flask. Every project I work on blends technical precision with creative problem-solving.", 
                "Over the years, I’ve had the privilege of contributing to various government projects, including work for the Ministry of Communication and Information Technology (Kominfo), the Agency for Pancasila Ideology Education (BPIP), the Ministry of Law and Human Rights (Kemenkumham), and several municipal governments across Indonesia. I’ve also collaborated with individual clients, companies, and international partners, delivering scalable and impactful digital solutions.",
                "At Copilot ID, I continue to grow as both a developer and mentor. I’ve guided more than 50 aspiring programmers through DBS Foundation’s Coding Camp, helping them build solid Python fundamentals and professional confidence. So far, I’ve completed over 100 projects—from AI models and automation tools to full-stack web applications—using technologies like TensorFlow, PyTorch, and modern backend stacks.", 
                "started coding during junior high school while studying at Darul Ulum Elementary, SMP N 1 Batang, and SMK N 1 Batang, teaching myself programming through curiosity and persistence.",
                "Looking ahead, my vision is to expand Copilot ID, contribute actively to open-source communities, and harness AI to solve real-world problems with innovation, integrity, and measurable impact. I’m driven to build technology that fosters sustainable progress."
                "If you have a forward-thinking idea or want to explore what’s possible through technology, I’d love to connect and create something transformative together."
            ],
            "location": {
                "regency": "Batang",
                "residency": "Batang",
                "province": "Central Java",
                "prov": "Central Java",
                "country": "Indonesia",
                "flag": "🇮🇩"
            },
            "social_media": {
                "email": "nadhifkarim89@gmail.com",
                "github": "https://github.com/ardifx01",
                "linkedin": "#",
                "follow_linkedin": "#",
                "instagram": "https://www.instagram.com/karimm.js",
                "medium": "#",
                "x": "https://x.com/el_2083",
                "website": "https://mnkdigital.tech",
            },
            "donate": [
                {
                    "github_sponsor": "#",
                    "donate_text": "Back me on GitHub Sponsors"
                },
                {
                    "sociabuzz": "#",
                    "donate_text": "Become a patron through Sociabuzz"
                },
                {
                    "buy_me_a_coffee": "#",
                    "donate_text": "Support my work with a coffee"
                },
                {
                    "saweria": "#",
                    "donate_text": "Support my journey on Saweria"
                },
            ],
            "skills": [
                "Python",
                "Django",
                "TensorFlow",
                "PyTorch",
                "Flask"
            ],
        }
