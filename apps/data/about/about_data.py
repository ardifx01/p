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
            "username": "dhifff",
            "aka": "mnk",

            "image_url": f"{settings.BASE_URL}/static/img/pp.jpg",
            "personal_website": "https://mnkdigital.tech",
            "cv": "",
            "cv_latest": "",
            "cv_copy": "",

            "role": "Software Engineer",
            "is_active": cls.is_working_hours(),
            "is_open_to_work": False,
            "is_hiring": True,

            "short_description": (
                "A quiet space where backend systems, machine learning, "
                "and thoughtful engineering come together."
            ),

            "short_bio": (
                "I focus on building reliable backend systems and intelligent applications. "
                "My work blends machine learning, web engineering, and open-source, "
                "with an emphasis on clarity, performance, and long-term maintainability."
            ),

            "short_cta": "Explore the work behind the systems.",

            "long_description": (
                "I’m Nadhif—also known as Dhiff or Rim—a software engineer based in Central Java, Indonesia. "
                "My work centers on backend engineering, machine learning, and building systems that are "
                "designed to scale, operate reliably, and remain maintainable over time.\n\n"
                "At Copilot ID, I design and develop high-performance backend services and intelligent "
                "applications using Python, PHP, Go (Golang), and TypeScript, primarily with frameworks "
                "such as Django and Flask. I spend much of my time thinking about system architecture, "
                "data flow, performance trade-offs, and how software behaves in real production environments.\n\n"
                "I’ve worked across government, enterprise, and independent projects—collaborating with "
                "national ministries, local governments, companies, and international partners. These "
                "experiences have shaped a pragmatic approach to engineering: making informed technical "
                "decisions and delivering solutions that fit real operational needs.\n\n"
                "Alongside project work, I’m actively involved in mentoring and knowledge sharing. "
                "Through DBS Foundation’s Coding Camp, I’ve mentored over 50 developers, helping them "
                "build strong fundamentals and practical problem-solving skills. Looking ahead, "
                "I aim to grow Copilot ID, contribute to open-source communities, and apply AI where it "
                "creates clear, measurable value."
            ),

            "stories": [
                (
                    "I’m Nadhif—also known as Dhiff or Rim—a software engineer based in Central Java, Indonesia. "
                    "I focus on backend engineering and machine learning, building systems that prioritize "
                    "reliability, scalability, and long-term maintainability."
                ),
                (
                    "At Copilot ID, I design and build backend services and intelligent applications using "
                    "Python, PHP, Go (Golang), and TypeScript, primarily with Django and Flask. "
                    "My work often revolves around architecture, performance, and production readiness."
                ),
                (
                    "I’ve contributed to a wide range of government and public-sector projects in Indonesia, "
                    "including work involving national ministries and local governments, as well as "
                    "collaborations with companies and international partners."
                ),
                (
                    "Beyond engineering work, I’m actively involved in mentoring. Through DBS Foundation’s "
                    "Coding Camp, I’ve guided over 50 aspiring developers, helping them build strong Python "
                    "fundamentals and confidence in solving real problems."
                ),
                (
                    "I started coding during junior high school, learning independently through curiosity "
                    "and persistence while studying at Darul Ulum Elementary, SMP N 1 Batang, and "
                    "SMK N 1 Batang. That early foundation still shapes how I approach engineering today."
                ),
                (
                    "Looking ahead, my focus is on growing Copilot ID, contributing to open-source projects, "
                    "and applying AI to solve real-world problems with clarity, integrity, and measurable impact."
                ),
            ],

            "location": {
                "regency": "Batang",
                "residency": "Batang",
                "province": "Central Java",
                "prov": "Central Java",
                "country": "Indonesia",
                "flag": "🇮🇩",
            },

            "social_media": {
                "email": "nadhifkarim89@gmail.com",
                "github": "https://github.com/ardifx01",
                "linkedin": "",
                "follow_linkedin": "",
                "instagram": "https://www.instagram.com/karimm.js",
                "medium": "",
                "x": "https://x.com/el_2083",
                "website": "https://mnkdigital.tech",
            },

            "donate": [
                {
                    "github_sponsor": "#",
                    "donate_text": "Back me on GitHub Sponsors",
                },
                {
                    "sociabuzz": "#",
                    "donate_text": "Become a patron through Sociabuzz",
                },
                {
                    "buy_me_a_coffee": "#",
                    "donate_text": "Support my work with a coffee",
                },
                {
                    "saweria": "#",
                    "donate_text": "Support my journey on Saweria",
                },
            ],

            "skills": [
                "Python",
                "Django",
                "Flask",
                "Go (Golang)",
                "Machine Learning",
                "TensorFlow",
                "PyTorch",
                "Backend Architecture",
            ],
        }
