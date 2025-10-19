from django.conf import settings

class EducationData:
    education = [
        {
            "degree": "Senior High School",
            "years": "2020-2022",
            "institution": "SMK NEGERI 1 BATANG",
            "website": "https://smkn1batang.sch.id/",
            "logo": f"{settings.BASE_URL}/static/img/logo/smk.jpg",
            "is_last": False,
            "location": {
                "regency": "Batang",
                "province": "Central Java",
                "prov": "Central Java",
                "country": "Indonesia",
                "flag": "🇮🇩",
                "map_url": "https://maps.app.goo.gl/tKZiWHBbMrLyNJSg7"
            },
            "achievements": [
                "Actively participated in outdoor and community-based activities, fostering teamwork and resilience.",
                "Contributing to nature-based programs and environmental engagement."
            ]
        },
        {
            "degree": "Junior High School",
            "years": "2017-2020",
            "institution": "SMP NEGERI 1 BATANG",
            "website": "https://smpn1-batang.blogspot.com",
            "logo": f"{settings.BASE_URL}/static/img/logo/smp.jpg",
            "is_last": False,
            "location": {
                "regency": "Batang",
                "province": "Central Java",
                "prov": "Central Java",
                "country": "Indonesia",
                "flag": "🇮🇩",
                "map_url": "https://maps.app.goo.gl/oTVvy5nU3GztYn5UA"
            },
              "achievements": [
                "Initiated web development journey by building foundational projects using HTML, CSS, and PHP."
            ]
        },        
    ]
