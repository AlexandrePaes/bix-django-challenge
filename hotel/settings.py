"""
Django settings for hotel project.

Generated by 'django-admin startproject' using Django 3.2.21.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
# from django.utils.translation import ugettext as _
from decouple import config, Csv
import dj_database_url
from dj_database_url import parse as dburl
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default="", cast=Csv())


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookings',
    'rest_framework',
    'django_celery_results',
    'django_celery_beat',
    'rest_framework.authtoken',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hotel.urls'

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

WSGI_APPLICATION = 'hotel.wsgi.application'


CORS_ALLOW_ALL_ORIGINS = True



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# DATABASES = {
#     'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
# }

#'default': os.environ.get(('DATABASE_URL'), default=default_dburl, cast=dburl),

# default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

    # Bix Production
    # 'default': {
    #     'ENGINE': os.environ.get('DB_DRIVER', 'django.db.backends.postgresql'),
    #     "HOST": os.environ.get("POSTGRES_HOST", "db"),
    #     "NAME": os.environ.get("POSTGRES_NAME", "postgres"),
    #     "USER": os.environ.get("POSTGRES_USER", "postgres"),
    #     "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "postgres"),
    #     "PORT": int(os.environ.get("POSTGRES_PORT", "5432")),
    # }

    # Bix Production 2
    # 'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = str(BASE_DIR / 'staticfiles')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# AUTH_USER_MODEL = 'users.CustomUser'

# from django.utils.translation import ugettext_lazy as _
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         # 'dj_rest_auth.jwt_auth.JWTCookieAuthentication',
#         'rest_framework_simplejwt.authentication.JWTAuthentication'
#     ),
# }

# REST_USE_JWT = True
# JWT_AUTH_COOKIE = 'hotel-auth'
# JWT_AUTH_REFRESH_COOKIE = 'hotel-refresh-token'

# JWT_AUTH = {
#     'JWT_SERIALIZER': 'bookings.serializers.JSONWebCustomTokenSerializer',
# }

# Último que funcionou sem bugs
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

# EMAIL_HOST = os.environ.get('EMAIL_HOST')
# EMAIL_PORT = os.environ.get('EMAIL_PORT')
# EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')


CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Manaus'

CELERY_RESULT_BACKEND = 'django-db'

# CELERY_BROKER_URL = 'amqp://guest:guest@localhost'

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'

# CELERY_TASK_SERIALIZER = 'json'

# CELERY_EMAIL_BACKEND = 'django_celery_email.backends.CeleryEmailBackend'
# CELERY_TASK_EMAIL_SENDER = 'django.core.mail.backends.smtp.EmailBackend'

#CELERY BEAT
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'

# CELERY_BEAT_SCHEDULE = {
#     'release_canceled_rooms': {
#         'task': 'hotel.tasks.send_user_email',
#         'task': 'hotel.tasks.liberar_quartos_cancelados',
#     },
# }

EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER='alexandrepaescontato@gmail.com'
EMAIL_HOST_PASSWORD='lxhgjgpmnwidqomi'
DEFAULT_FROM_EMAIL = 'Celery <alexandrepaescontato@gmail.com>'

# EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com') #,'your_email_host')
# EMAIL_PORT = os.environ.get('EMAIL_PORT', 587) #, 587)
# EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', True) #, True)
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'alexandrepaescontato@gmail.com') #, 'your_email@example.com')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'lxhgjgpmnwidqomi') #, 'your_email_password')