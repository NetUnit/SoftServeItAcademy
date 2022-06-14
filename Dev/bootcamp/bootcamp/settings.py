"""
Django settings for bootcamp project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import logging
import datetime
import dotenv

AUTH_PROVIDERS = (
    'google',
    'facebook',
    'twitter',
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# reading key-value pairs from a .env file & set them as environment variables.
# helps in the development of applications following the 12-factor principles.
DOT_ENV = os.path.join(BASE_DIR, ".env")
if os.path.isfile(DOT_ENV):
    dotenv.load_dotenv(DOT_ENV)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-oy89dwyz7o+&db$sk!xrlfi#g3x5y-*-riqf5fjh(n7h%e$^d('


# SECURITY WARNING: don't run with debug turned on in production!
# disable for rendering error temaplates
DEBUG = True

# DEBUG = False
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS =  ['localhost', '127.0.0.1']
# ALLOWED_HOSTS =  []

# Application definition
INSTALLED_APPS = [
    'rest_framework',
    'whitenoise.runserver_nostatic',  # customized (added)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',  # app#1 - auth
    'errortemplates',  # custom error templates
    'products',  # app#2
    'manufacturer',  # app#3
    'orders',  # app#4
    'profiles',  # app#5
    'emails',  # app#6
    'crispy_forms',  # crispy_forms for templates
    'paypal.standard.ipn',  # paypal gateaway
    # *** api authentication *** #
    'rest_framework.authtoken',
    'rest_framework_jwt',
    'oauth2_provider',
    'social_django'
]

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/accounts/login-success/'
LOGOUT_URL = '/logout/'

# Add to test email:
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Application definition
AUTH_USER_MODEL = 'accounts.CustomUser'
AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'accounts.backends.EmailBackend',
    # 'facebook_login.auth_backends.FacebookAuthBackend',
    # 'oauth2_provider.backends.GoogleOAuth2'
    ]

# AUTH_USER_MODEL = 'accounts.MyAccountManager'
# ACCOUNT_USER_MODEL_USERNAME_FIELD = 'email'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',               # customized (added)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'bootcamp.middleware.CustomExceptionMiddleware',
    # 'bootcamp.middleware.SimpleMiddleware',
]

ROOT_URLCONF = 'bootcamp.urls'

# TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # setup other roots to specified template sources
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            # os.path.join(BASE_DIR, 'products/templates'),  # additional path
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # sets the request variable in the context
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'bootcamp.context_processors.footer_app_name',  # custom context for each app
                'bootcamp.context_processors.root',  # custom context for getting path to a webpage
            ],
        },
    },
]

WSGI_APPLICATION = 'bootcamp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'panda_hardware',
        'USER': 'postgres',
        'PASSWORD': '7875',
        'HOST': 'localhost',
        'PORT': '5432',
    }
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

# instantating a Python logging instance
LOGGER = logging.getLogger(__name__)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            # The -12s % -8s control spacing between the different format specifications
            'format': 'PACKAGE: %(name)-15s LEVEL: %(levelname)-9s MESSAGE: %(message)s'
        },
        'file': {
            # adding timestamp value to debug.log journal
            'format': '%(asctime)s %(name)-15s %(levelname)-9s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': os.path.join(BASE_DIR, 'debug.log')
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
            'propagate': False
        },
        'bootcamp': {  # Specific logger for your app
            'class': 'logging.StreamHandler',
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # handles any exceptions that occur due to
        # Cross-Site Request Forgery (CSRF) attacks
        'django.request': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
}


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',  # won't require auth at all
        # 'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly' #-- won't require auth but read only methods
    ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        # 'accounts.backends.JWTAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
    )
}


# *** JWT Authentication SETTINGS *** #
# additional settings that you can override similar to
# how you'd do it with Django REST framework
JWT_AUTH = {
    'JWT_ENCODE_HANDLER':
    'rest_framework_jwt.utils.jwt_encode_handler',

    'JWT_DECODE_HANDLER':
    'rest_framework_jwt.utils.jwt_decode_handler',

    'JWT_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_payload_handler',

    'JWT_PAYLOAD_GET_USER_ID_HANDLER':
    'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

    'JWT_RESPONSE_PAYLOAD_HANDLER':
    'rest_framework_jwt.utils.jwt_response_payload_handler',

    'JWT_SECRET_KEY': SECRET_KEY,
    'JWT_GET_USER_SECRET_KEY': None,
    'JWT_PUBLIC_KEY': None,
    'JWT_PRIVATE_KEY': None,
    'JWT_ALGORITHM': 'HS256',
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LEEWAY': 0,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
    'JWT_AUDIENCE': None,
    'JWT_ISSUER': None,
    'JWT_ALLOW_REFRESH': False,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_AUTH_COOKIE': None,
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# in the case of a BASE_DIR
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_URL = '/static/'

# STATICFILES_DIRS setting should not contain the STATIC_ROOT setting.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'),
    # os.path.join('/staticfiles/')
]

# *** Django & app realted files *** #
# Cloud storages: Cloudfront, Google Cloud Storage, django-storages, Whitenoise
STATIC_ROOT = os.path.join(BASE_DIR, 'cdn_test/static/')
# allows to load static files and use them like this:
# {% load static %}
# <img src="{% static "images/hi.jpg" %}" alt="Hi!"

# *** User uploaded files *** #
# any file field upload by deafault
MEDIA_ROOT = os.path.join(BASE_DIR, 'cdn_test/')
PROTECTED_MEDIA = os.path.join(BASE_DIR, 'cdn_test/')

MEDIA_URL = '/media/'

# creates folders for different static roots
if DEBUG:
    os.makedirs(STATIC_ROOT, exist_ok=True),
    os.makedirs(MEDIA_ROOT, exist_ok=True),
    os.makedirs(PROTECTED_MEDIA, exist_ok=True),

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


PRODUCTS_GROUP = 'THE PRODUCT STORE'
PRODUCTS_TAGLINE = 'The latest incomes of products/manufacturers/prices/updates'

# setup as automated in context processors
MAIN_PAGE = 'BOOTCAMP/MAIN PAGE'
MAIN_PAGE_TAGLINE = 'bootcamp main page tagline'
COMPANY_NAME_TAGLINE = 'Panda Hardware LLC'

APP_NAME_1 = 'PRODUCTS'
APP_NAME_1_TAGLINE = 'products tagline'

APP_NAME_2 = 'ACCOUNTS'
APP_NAME_2_TAGLINE = 'accounts tagline'

APP_NAME_3 = 'PROFILES'
APP_NAME_3_TAGLINE = 'profiles tagline'

APP_NAME_4 = 'MANUFACTURERS'
APP_NAME_4_TAGLINE = 'manufacturers tagline'

APP_NAME_5 = 'ORDERS'
APP_NAME_5_TAGLINE = 'orders tagline'

# django-paypal settings
PAYPAL_RECEIVER_EMAIL = 'myXbox@bigmir.net'
PAYPAL_TEST = True

CRISPY_FORMS_TEMPLATE_PACK = 'bootstrap4'
