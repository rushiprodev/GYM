# 🏋️‍♂️ GYM Registration System (Django)

A Django-based backend application for managing online, offline, and yoga class registrations.  
Built with scalability in mind and ready for deployment on **Render** with a PostgreSQL cloud database.

---

## 🚀 Features

- Online, Offline, and Yoga class registration via webhooks
- API ready for integration with platforms like GoHighLevel
- PostgreSQL cloud database support (via Render)
- Environment variable management with `.env`
- Production-ready settings with Whitenoise and gunicorn
- Secure token verification via `GHL_SECRET`

---

## 🧱 Project Structure

```bash
GYM/
├── registrations/          # App: Webhook handlers and models
├── GYM/                    # Django project settings
├── manage.py
├── .env                    # Environment config (excluded from Git)
├── requirements.txt        # Python dependencies
├── render.yaml             # Render deployment settings
└── README.md
