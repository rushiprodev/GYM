"""
Django settings for GYM project.
"""

import os
from pathlib import Path
import dj_database_url
import django_heroku
import dotenv

# 📦 Load environment variables from .env
dotenv.load_dotenv()

# 📁 Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Secret Key (use environment variable)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-default-key')

# ✅ Use DEBUG=True only in development
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# 🌍 Allowed Hosts
ALLOWED_HOSTS = ['*']  # You can limit to your Render domain in production

# 📦 Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registrations',
]

# ⚙️ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Serves static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'GYM.urls'

# 🖼 Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'GYM.wsgi.application'

# 🔗 Database configuration: SQLite (local) or PostgreSQL (Render)
if os.getenv("RENDER", "").upper() == "TRUE":
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# 🔐 Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌐 Localization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 🗂 Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# 🗝 Auto Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ GHL Secret
GHL_SECRET = os.getenv("GHL_SECRET", "rushigym123")

# 🚀 Render/Heroku deployment settings
django_heroku.settings(locals())

