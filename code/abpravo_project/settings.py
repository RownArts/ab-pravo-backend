"""
Django settings for abpravo_project project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&$3@9t(d&%vh@9!cn#0*wxtlrvb0o*+z@^_ydl1cs13*he-4y3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'api.ab-pravo.ru', ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # THIRD_PARTY
    'rest_framework',
    'adminsortable2',
    'sorl.thumbnail',
    'sorl_thumbnail_serializer',
    'ckeditor',
    'ckeditor_uploader',
    'corsheaders',
    'django_filters',
    'nested_admin',
    # "rest_framework_recaptcha",
    # "drf_recaptcha",
    'django_extensions',
    # 'phonenumber_field',
    'django_cleanup.apps.CleanupConfig',
    'storages',
    # APPS
    'apps.core',
    'apps.gallery',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # DEFAULT DJANGO
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'abpravo_project.urls'

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

WSGI_APPLICATION = 'abpravo_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = 'media/'
MEDIA_URL = 'media/'
CKEDITOR_UPLOAD_PATH = "ckeditor_uploads"


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


CACHETIME_CUSTOM = 30  # в секундах

# CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "https://ab-pravo.ru",
    "https://www.ab-pravo.ru",
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]
CSRF_TRUSTED_ORIGINS = [
    'ab-pravo.ru',
    'localhost',
    '127.0.0.1',
]


STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = 'custom_storages.StaticStorage'
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

AWS_S3_ENDPOINT_URL = 'https://storage.yandexcloud.net'
# AWS_S3_OBJECT_PARAMETERS = {
#     'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
#     'CacheControl': 'max-age=94608000',
# }
AWS_S3_FILE_OVERWRITE = False
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_DEFAULT_ACL = 'public-read'

########    AMAZON S3 SETTINGS   ##########
AWS_STORAGE_BUCKET_NAME = 'cdn.ab-pravo.ru'
AWS_S3_REGION_NAME = 'ru-central1'  # e.g. us-east-2
AWS_ACCESS_KEY_ID = 'PSKICBYGrpugSQ2kqJpw'
AWS_SECRET_ACCESS_KEY = '5bMh2pKsW75-tSNzSjArB4AKNtyKxRoeRbbn9Abj'
AWS_S3_SECURE_URLS = True
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_CUSTOM_DOMAIN = '%s.website.yandexcloud.net' % AWS_STORAGE_BUCKET_NAME
AWS_S3_CUSTOM_DOMAIN = 'cdn.ab-pravo.ru'


EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'server@ab-pravo.ru'
EMAIL_HOST_PASSWORD = 'VWgoHaQGhE;Vn3NbN=pjghwj'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
