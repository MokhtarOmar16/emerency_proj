"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os 
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent.parent


ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "daphne",
    'chat',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'whitenoise.runserver_nostatic',
    'drf_spectacular',
    'drf_spectacular_websocket',
    'drf_spectacular_sidecar',
    'corsheaders',
    'rest_framework',
    "debug_toolbar",
    "social_django",
    'djoser',
    'emergency',
    'users',
    'channels',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Social
    
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

ROOT_URLCONF = 'project.urls'

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





# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50
}


# user update
AUTH_USER_MODEL = 'users.User'
AUTHENTICATION_BACKENDS = [
    'users.backends.EmailBackend',
    
    # Social
    "social_core.backends.google.GoogleOAuth2",
    
]


SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
        "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
}

SPECTACULAR_SETTINGS = {
    'DEFAULT_GENERATOR_CLASS': 'drf_spectacular_websocket.schemas.WsSchemaGenerator',
    'SWAGGER_UI_DIST': 'SIDECAR',
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    'SWAGGER_UI_SETTINGS': {
        'connectSocket': True,  # Automatically establish a WS connection when opening swagger
        'socketMaxMessages': 8,  # Max number of messages displayed in the log window in swagger
        'socketMessagesInitialOpened': False,  # Automatically open the log window when opening swagger
    },
    'TITLE': 'Emergency API',
    'DESCRIPTION': 'Emergency API is a REST API for emergency services.',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': 0,
}



DJOSER = {
    'TOKEN_MODEL': None, 
    'SERIALIZERS': {
    },
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": ["http://localhost:3000"],
}

CORS_ALLOWED_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True  
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    "http://192.168.1.5:8000",  

]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
# Social
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get("GOOGLE_CLIENT_ID")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get("GOOGLE_SECRET")
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
]
SOCIAL_AUTH_GOOGLE_OAUTH2_EXTRA_DATA = ["first_name", "last_name"]

SOCIAL_AUTH_PROTECTED_USER_FIELDS = [
    'first_name', 
    'last_name', 
    'username', 
    'password',
    'username'
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}


# WSGI_APPLICATION = 'project.wsgi.application'
ASGI_APPLICATION = 'project.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}
