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
            "first_name": "Muhammad",
            "last_name": "Nadhif",
            "username": "ardifx01", # GitHub username
            "aka": "karim",
            "image_url": f"{settings.BASE_URL}/static/img/pp.jpg",
            "personal_website": "https://mnkdigital.tech",
            "cv": "#",
            "cv_latest": "#",
            "cv_copy": "#",
            "role": "Fullstack Programmer",
            "is_active": cls.is_working_hours(),
            "is_open_to_work": True,
            "is_hiring": False,
            "short_description": "a quiet space where machine learning, open-source, and reflections converge.",
            "short_bio_old": "I explore through code, share with empathy, and reflect on every challenge. My work weaves machine learning, web creation, and open-source. This site archives the curious, the technical, and the quietly thoughtful.",
            "short_bio": "I explore through code, share with empathy, and reflect on every challenge. My work weaves machine learning, web creation, and open source. I thrive on collaborating with teams to develop smart, user centered AI and web solutions that blend function with clarity.",
            "short_cta": "Stay a while and see what lives beyond the code.",
            "long_description": "I'm a machine learning engineer and web developer, building AI apps and slick websites that solve real problems. I've memorized nearly 30 Juz of the Quran, which has wired me for grit, focus, and discipline. I've mentored 50+ coders at DBS Foundation's Coding Camp and guided 100+ interns at GAOTek Inc. I've shipped 30+ projects using TensorFlow, PyTorch, and more. I'm all in on using AI to tackle big challenges fast, growing Copilot ID, and dropping value in open-source communities.",
            "stories": [
                "I am Nadhif, known as karim or pabloesdoger:D. A Python developer with a passion for machine learning and web development from Central Java, Indonesia, I lead Copilot ID—my creative hub for building intelligent systems and web applications with Django, Flask, and ML tools with PyTorch and TensorFlow, crafting each project with purpose.",
                "Professionally, I have had the privilege of guiding over 50 aspiring coders at DBS Foundation’s Coding Camp, nurturing their growth in Python and essential soft skills. At GAOTek Inc., I mentored more than 100 interns, helping them navigate their early steps in the tech world. To date, I have delivered over 30 projects, spanning AI models to full-stack web applications, leveraging tools like TensorFlow, PyTorch, and beyond.",
                "I previously attended Darul Ulum Elementary School, then continued my junior high school at SMP N 1 Batang, then continued my vocational high school at SMK N 1 Batang. I learned coding autodidactically from junior high school.",
                "Looking forward, my vision is to elevate Copilot ID, contribute meaningfully to open-source communities, and harness AI to address impactful challenges with precision and integrity. I am committed to fostering innovation that drives sustainable progress.",
                "If you have a visionary idea or wish to explore the possibilities of technology, I’d be delighted to connect and create something transformative together.🚀"
            ],
            "location": {
                "regency": "Batang",
                "residency": "Batang Residency",
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
                "instagram": "https://instagram.com/karimm.js",
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
