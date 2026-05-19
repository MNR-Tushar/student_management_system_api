from datetime import timedelta
from pathlib import Path
import os
from dotenv import load_dotenv
 
load_dotenv()
 
BASE_DIR = Path(__file__).resolve().parent.parent
 
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-fallback-key-change-in-production')
 
DEBUG = os.getenv('DEBUG', 'False') == 'True'
 
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'django_filters',
    'drf_spectacular',
    'student_info',
    'users',
    'teachers',
    'courses',
    'results',
    'attendance',
    'departments',
    'enrollments',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'students.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'students.wsgi.application'


# ─── PostgreSQL Database ───────────────────────────────────────────────────────
DATABASES = {
    'default': {
        'ENGINE':   os.getenv('DB_ENGINE', 'django.db.backends.postgresql'),
        'NAME':     os.getenv('DB_NAME', 'student_db'),
        'USER':     os.getenv('DB_USER', 'student_user'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'student123'),
        'HOST':     os.getenv('DB_HOST', 'db'),
        'PORT':     os.getenv('DB_PORT', '5432'),
    }
}


# ─── Redis Cache ───────────────────────────────────────────────────────────────
CACHES = {
    'default': {
        'BACKEND':  'django_redis.cache.RedisCache',
        'LOCATION': os.getenv('CACHE_LOCATION', 'redis://redis:6379/0'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'KEY_PREFIX': 'sms',          # student management system
        'TIMEOUT': 60 * 15,           # 15 minutes default cache timeout
    }
}


# Use Redis for Django sessions too
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'


# ─── Celery (Redis as broker) ──────────────────────────────────────────────────
CELERY_BROKER_URL        = os.getenv('REDIS_URL', 'redis://redis:6379/1')
CELERY_RESULT_BACKEND    = os.getenv('REDIS_URL', 'redis://redis:6379/1')
CELERY_ACCEPT_CONTENT    = ['json']
CELERY_TASK_SERIALIZER   = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE          = 'Asia/Dhaka'



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


AUTH_USER_MODEL = 'users.CustomUser'
 
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True
 
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
 
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
 

# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Student Management System API',
    'DESCRIPTION': (
        'A complete REST API for managing academic operations in a student management system.\n\n'
        'This API provides secure JWT-based authentication and role-friendly endpoints for managing:\n'
        '- User registration, login, logout, and token refresh\n'
        '- Student profiles and student records\n'
        '- Teacher profiles and teacher records\n'
        '- Departments and academic structures\n'
        '- Courses and course-related details\n'
        '- Enrollments connecting students to courses\n\n'
        'Common capabilities include pagination, filtering, search, and ordering on list endpoints.\n'
        'Use the Authorize button in Swagger with a Bearer token to test protected endpoints.'
    ),
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}


# JWT Configuration (Fixed - Using standard tokens, not sliding)
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',
}
