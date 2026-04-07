from django.conf import settings

class ExperiencesData:
    '''
    employment type:
    - Full-time (Pekerjaan penuh waktu)
    - Part-time (Pekerjaan paruh waktu)
    - Self-employed (Pekerjaan mandiri)
    - Freelance (Pekerjaan lepas)
    - Contract (Pekerjaan berdasarkan kontrak)
    - Internship (Magang)
    - Apprenticeship (Pelatihan kerja atau magang kejuruan)
    - Seasonal (Pekerjaan musiman)
    
    location type:
    - On-site: Bekerja langsung di lokasi fisik (contoh: kantor).
    - Hybrid: Kombinasi antara bekerja dari lokasi fisik dan jarak jauh.
    - Remote: Sepenuhnya bekerja jarak jauh (contoh: dari rumah).
    '''
    
    employment_types = {
        "ft": "Full-time",
        "pt": "Part-time",
        "se": "Self-employed",
        "fr": "Freelance",
        "co": "Contract",
        "in": "Internship",
        "ap": "Apprenticeship",
        "sn": "Seasonal",
        "sc": "Scholarship"
    }
    
    location_types = {
        "on": "On-site",
        "hy": "Hybrid",
        "rm": "Remote"
    }
    
    experiences = [
	{
            "id": 17,
            "title": "Fullstack Developer (IT Solutions)",
            "company": "Kementerian Komunikasi dan Digital (Komdigi)",
            "logo": f"{settings.BASE_URL}/static/img/logo/komdigi.jpg", 
            "website": "https://www.komdigi.go.id",
            "period": {
                "start": {
		"month": "Jan", 
		"year": 2026
	        }, 
                "end": "Present" 
            },
            "employment_type": employment_types["pt"],
            "location_type": location_types["on"],
            "location": "Jakarta, Indonesia 🇮🇩",
            "is_current": True,
            "responsibilities": [
                "Developed and maintained internal web applications using Django/DRF and modern frontend workflows.",
                "Built REST APIs, authentication/authorization, and role-based access control for multi-user systems.",
                "Designed database schemas and optimized queries for reporting and operational dashboards.",
                "Implemented deployment and monitoring practices, improving reliability and maintainability."
            ]
        },
        {
            "id": 16,
            "title": "Fullstack Developer (Data & Platform)",
            "company": "Badan Pembinaan Ideologi Pancasila (BPIP)",
            "logo": f"{settings.BASE_URL}/static/img/logo/bpip.jpg", 
            "website": "https://bpip.go.id",
            "period": {
                "start": {
		"month": "Jul", 
		"year": 2025
		}, 
                "end": "Present" 
            },
            "employment_type": employment_types["co"],
            "location_type": location_types["rm"],
            "location": "Indonesia 🇮🇩",
            "is_current": True,
            "responsibilities": [
                "Delivered end-to-end solutions: backend services (Django/DRF), database, and admin dashboards.",
                "Built data ingestion and processing pipelines for structured/unstructured datasets.",
                "Created reporting modules and export tools (CSV/PDF) to support program evaluation.",
                "Produced technical documentation and ensured secure access patterns for internal users."
            ]
        },
        {
            "id": 15,
            "title": "Fullstack Developer (Information System)",
            "company": "Semarangkota", 
            "logo": f"{settings.BASE_URL}/static/img/logo/semarang.jpg", 
            "website": "https://semarangkota.go.id", 
            "period": {
                "start": {
		"month": "Oct", 
		"year": 2025
		}, 
                "end": "Present" 
            },
            "employment_type": employment_types["fr"],
            "location_type": location_types["on"],
            "location": "Indonesia 🇮🇩",
            "is_current": True,
            "responsibilities": [
                "Built social assistance information systems for beneficiary data management and verification workflows.",
                "Implemented backend modules: CRUD, validation rules, audit logging, and role-based permissions.",
                "Developed responsive UI components and dashboards for operational staff.",
                "Handled deployment, bugfixing, and post-release support to ensure smooth adoption."
            ]
        },
        {
            "id": 14,
            "title": "Fullstack Developer (IT Solutions)",
            "company": "Universitas 17 Agustus 1945 Semarang",
            "logo": f"{settings.BASE_URL}/static/img/logo/untagsmg.jpg", 
            "website": "https://untagsmg.ac.id",
            "period": {
                "start": {
		"month": "Jan", 
		"year": 2025
	     },
                "end": "Present"
            },
            "employment_type": employment_types["fr"],
            "location_type": location_types["hy"],
            "location": "Semarang, Indonesia 🇮🇩",
            "is_current": True,
            "responsibilities": [
                "Developed academic and administrative web systems (backend APIs + frontend UI) aligned to campus workflows.",
                "Implemented authentication, RBAC, and data integrity rules across student/staff modules.",
                "Optimized database design and performance for reporting and high-frequency transactions.",
                "Collaborated with stakeholders, delivered iterative releases, and maintained long-term system stability."
            ]
        }

        {
            "id": 13,
            "title": "Founder",
            "company": "Copilot ID",
            "logo": f"{settings.BASE_URL}/static/img/logo/copilot_id.webp",
            "website": "https://github.com/copilot-id",
            "period": {
                "start": {
                    "month": "Jan",
                    "year": 2023
                },
                "end": "Present"
            },
            "employment_type": employment_types["se"],
            "location_type": location_types["on"],
            "location": "Solo, Indonesia 🇮🇩",
            "is_current": True,
            "responsibilities": [
                "Collaborative Python Innovations and Learning for Optimal Technologies.",
                "Executed AI-driven projects using Django, TensorFlow, PyTorch, and modern web technologies.",
                "3+ years of Django experience across 15+ full-cycle projects including MTV architecture, ORM, REST APIs, authentication, testing, and debugging.",
                "Built and deployed 7+ Flask-based microservices with scalable routing and Jinja2 templating.",
                "Developed 8+ end-to-end neural network systems involving preprocessing, feature engineering, model tuning, evaluation, distributed training, and deployment.",
                "Applied a broad tech stack: Python, PHP, JavaScript, Django, Flask, React, Next.js, Node.js, WordPress, Material-UI, TypeScript, Laravel, TensorFlow, PyTorch, Keras, Scikit-learn, HTML/CSS, SQL/NoSQL, Git, DRF, Postman, GraphQL, Vercel, Netlify, and Cloudflare."
            ]
        },
        {
            "id": 12,
            "title": "Chief Secretary",
            "company": "IKA-PPIM 2021",
            "logo": f"{settings.BASE_URL}/static/img/logo/ikappim_21.webp",
            "website": "https://www.instagram.com/ikappim_21/",
            "period": {
                "start": {
                    "month": "Sep",
                    "year": 2021
                },
                "end": "Present"
            },
            "employment_type": employment_types["pt"],
            "location_type": location_types["rm"],
            "location": "Surakarta, Indonesia 🇮🇩",
            "is_current": True,
            "responsibilities": [
                "Managed data for over 200 alumni, including advanced filtering and data visualization.",
                "Prepared organizational documents and meeting notes.",
                "Designed user-friendly interfaces for alumni management."
            ]
        },
        {
            "id": 11,
            "title": "Machine Learning Mentor",
            "company": "Coding Camp powered by DBS Foundation",
            "logo": f"{settings.BASE_URL}/static/img/logo/coding_camp_dbs_foundation.webp",
            "website": "https://go.dbs.com/dbsfcodingcamp",
            "period": {
                "start": {
                    "month": "Feb",
                    "year": 2025
                },
                "end": {
                    "month": "Jul",
                    "year": 2025
                }
            },
            "employment_type": employment_types["pt"],
            "location_type": location_types["rm"],
            "location": "Bandung, Indonesia 🇮🇩",
            "is_current": False,
            "responsibilities": [
                "Led weekly mentoring sessions for 87 students, resulting in a 75% graduation rate and maintaining an average attendance of 84%.",
                "Provided 1.5 hours per week of personalized one-on-one sessions, addressing individual challenges and academic assignments to support student development.",
                "Conducted alternating weekly sessions on soft and technical skills (2 hours/week) for 50 participants, managing facilitator coordination, content preparation, session moderation, and cohort engagement monitoring.",
                "Participated in monthly 1.5-hour meetings and professional development sessions for mentors."
            ]
        },
        {
            "id": 10,
            "title": "Machine Learning Ops Cohort",
            "company": "Coding Camp powered by DBS Foundation",
            "logo": f"{settings.BASE_URL}/static/img/logo/coding_camp_dbs_foundation.webp",
            "website": "https://go.dbs.com/dbsfcodingcamp",
            "period": {
                "start": {
                    "month": "Dec",
                    "year": 2024
                },
                "end": {
                    "month": "Jan",
                    "year": 2025
                }
            },
            "employment_type": employment_types["sc"],
            "location_type": location_types["rm"],
            "location": "Bandung, Indonesia 🇮🇩",
            "is_current": False,
            "responsibilities": [
                "Acquired comprehensive knowledge of ML Ops to develop robust and scalable machine learning systems.",
                "Gained practical experience in deploying machine learning models in real-world production environments."
            ]
        },
        {
            "id": 9,
            "title": "Machine Learning Expert Cohort",
            "company": "Coding Camp powered by DBS Foundation",
            "logo": f"{settings.BASE_URL}/static/img/logo/coding_camp_dbs_foundation.webp",
            "website": "https://go.dbs.com/dbsfcodingcamp",
            "period": {
                "start": {
                    "month": "Oct",
                    "year": 2024
                },
                "end": {
                    "month": "Dec",
                    "year": 2024
                }
            },
            "employment_type": employment_types["sc"],
            "location_type": location_types["rm"],
            "location": "Bandung, Indonesia 🇮🇩",
            "is_current": False,
            "responsibilities": [
                "Developed machine learning systems for various projects, focusing on effective problem-solving.",
                "Built predictive models using k-Nearest Neighbor, Random Forest, and AdaBoost algorithms.",
                "Implemented sentiment analysis solutions utilizing Deep Learning and Support Vector Machines.",
                "Explored computer vision techniques for image recognition and object detection.",
                "Designed recommendation systems using content-based and collaborative filtering approaches."
            ]
        },
        {
            "id": 8,
            "title": "Machine Learning Intermediate Cohort",
            "company": "Coding Camp powered by DBS Foundation",
            "logo": f"{settings.BASE_URL}/static/img/logo/coding_camp_dbs_foundation.webp",
            "website": "https://go.dbs.com/dbsfcodingcamp",
            "period": {
                "start": {
                    "month": "Jul",
                    "year": 2024
                },
                "end": {
                    "month": "Sep",
                    "year": 2024
                }
            },
            "employment_type": employment_types["sc"],
            "location_type": location_types["rm"],
            "location": "Bandung, Indonesia 🇮🇩",
            "is_current": False,
            "responsibilities": [
                "Developed neural networks using TensorFlow and Keras for deep learning applications.",
                "Applied natural language processing techniques for text classification and sentiment analysis.",
                "Created deep learning models for time series and image classification tasks.",
                "Explored recommendation systems and reinforcement learning methodologies.",
                "Gained experience with generative AI and model deployment."
            ]
        },
        {
            "id": 7,
            "title": "Machine Learning Beginner Cohort",
            "company": "Coding Camp powered by DBS Foundation",
            "logo": f"{settings.BASE_URL}/static/img/logo/coding_camp_dbs_foundation.webp",
            "website": "https://go.dbs.com/dbsfcodingcamp",
            "period": {
                "start": {
                    "month": "Jan",
                    "year": 2024
                },
                "end": {
                    "month": "Jun",
                    "year": 2024
                }
            },
            "employment_type": employment_types["sc"],
            "location_type": location_types["rm"],
            "location": "Bandung, Indonesia 🇮🇩",
            "is_current": False,
            "responsibilities": [
                "Initiated data visualization projects using Google Sheets.",
                "Mastered Python fundamentals and object-oriented programming.",
                "Studied supervised and unsupervised machine learning algorithms."
            ]
        },
        {
            "id": 6,
            "title": "Assistant Squad Leader of Web Developer Intern",
            "company": "GAOTek Inc.",
            "logo": f"{settings.BASE_URL}/static/img/logo/gaotek_inc.webp",
            "website": "https://gaotek.com",
            "period": {
                "start": {
                    "month": "Apr",
                    "year": 2024
                },
                "end": {
                    "month": "May",
                    "year": 2024
                }
            },
            "employment_type": employment_types["in"],
            "location_type": location_types["rm"],
            "location": "New York, USA 🇺🇸",
            "is_current": False,
            "responsibilities": [
                "Supervised and coordinated a team of over 100 interns.",
                "Facilitated daily meetings and maintained team cohesion.",
                "Assisted interns in overcoming technical and project-related challenges."
            ]
        },
        {
            "id": 5,
            "title": "Main Team of Web Developer Intern",
            "company": "GAOTek Inc.",
            "logo": f"{settings.BASE_URL}/static/img/logo/gaotek_inc.webp",
            "website": "https://gaotek.com",
            "period": {
                "start": {
                    "month": "Apr",
                    "year": 2024
                },
                "end": {
                    "month": "May",
                    "year": 2024
                }
            },
            "employment_type": employment_types["in"],
            "location_type": location_types["rm"],
            "location": "New York, USA 🇺🇸",
            "is_current": False,
            "responsibilities": [
                "Collaborated with team members to plan projects and exchange ideas.",
                "Enhanced skills in Google Search Console, Analytics, and Tag Manager through multiple assignments.",
                "Submitted daily reports consistently throughout the internship period."
            ]
        },
        {
            "id": 4,
            "title": "Web Developer Intern",
            "company": "GAOTek Inc.",
            "logo": f"{settings.BASE_URL}/static/img/logo/gaotek_inc.webp",
            "website": "https://gaotek.com",
            "period": {
                "start": {
                    "month": "Feb",
                    "year": 2024
                },
                "end": {
                    "month": "Mar",
                    "year": 2024
                }
            },
            "employment_type": employment_types["in"],
            "location_type": location_types["rm"],
            "location": "New York, USA 🇺🇸",
            "is_current": False,
            "responsibilities": [
                "Participated in late-night team meetings to address technical issues and plan development tasks.",
                "Worked extensively with WooCommerce, adding over 30 products, creating a contact form, and developing more than 30 product pages.",
                "Completed over 7 tasks within two months, exceeding the average intern performance.",
                "Maintained a consistent record of daily reports throughout the internship."
            ]
        },
        {
            "id": 3,
            "title": "Machine Learning Intern",
            "company": "YoungDev",
            "logo": f"{settings.BASE_URL}/static/img/logo/youngdev.webp",
            "website": "https://youngdevinterns.net",
            "period": {
                "start": {
                    "month": "Apr",
                    "year": 2024
                },
                "end": {
                    "month": "May",
                    "year": 2024
                }
            },
            "employment_type": employment_types["in"],
            "location_type": location_types["rm"],
            "location": "Islamabad, Pakistan 🇵🇰",
            "is_current": False,
            "responsibilities": [
                "Developed predictive models using Python and Scikit-Learn.",
                "Implemented classification and regression models for various datasets."
            ]
        },
        {
            "id": 2,
            "title": "Machine Learning Intern",
            "company": "iNeuron.ai",
            "logo": f"{settings.BASE_URL}/static/img/logo/ineuron.webp",
            "website": "https://ineuron.ai",
            "period": {
                "start": {
                    "month": "Jan",
                    "year": 2024
                },
                "end": {
                    "month": "Jan",
                    "year": 2024
                }
            },
            "employment_type": employment_types["in"],
            "location_type": location_types["rm"],
            "location": "Karnataka, India 🇮🇳",
            "is_current": False,
            "responsibilities": [
                "Worked on a phishing domain detection project, integrating cybersecurity and machine learning.",
                "Applied machine learning techniques to enhance online security."
            ]
        },
        {
            "id": 1,
            "title": "Deputy of Da'wah",
            "company": "Imaarotu Syu'unith Tholabah",
            "logo": f"{settings.BASE_URL}/static/img/logo/ist.webp",
            "website": "https://istngruki.org",
            "period": {
                "start": {
                    "month": "Sep",
                    "year": 2019
                },
                "end": {
                    "month": "Sep",
                    "year": 2020
                }
            },
            "employment_type": employment_types["ft"],
            "location_type": location_types["on"],
            "location": "Surakarta, Indonesia 🇮🇩",
            "is_current": False,
            "responsibilities": [
                "Coordinated 50 boarding school students in community teaching initiatives.",
                "Collaborated in organizing competitions for over 500 students.",
                "Maintained and promoted discipline within the boarding school environment."
            ]
        }
    ]
