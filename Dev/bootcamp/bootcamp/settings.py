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

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-oy89dwyz7o+&db$sk!xrlfi#g3x5y-*-riqf5fjh(n7h%e$^d('

# SECURITY WARNING: don't run with debug turned on in production!


# DEBUG = True
# ALLOWED_HOSTS =  []

DEBUG = False
ALLOWED_HOSTS =  ['*']
# ALLOWED_HOSTS =  ['localhost', '127.0.0.1']



# Application definition
INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',                            # customized (added)
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    # 'errortemplates',                                         # custom error templates
    # apps
    'products',                                                 # app#1
    'manufacturer',                                             # app#2
    #'accounts',                                                # app#5
    'profiles',                                                 # app#3
    'emails',                                                   # app#4
    'orders',                                                   # app#5
    'crispy_forms',                                             # crispy_forms for temapltes
    'paypal.standard.ipn',                                      # paypal gateaway
]


# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/accounts/login-success/'
LOGOUT_URL = '/logout/'


# Add to test email:
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Application definition
AUTH_USER_MODEL = 'accounts.CustomUser'
AUTHENTICATION_BACKENDS = ['accounts.backends.EmailBackend']
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
]

ROOT_URLCONF = 'bootcamp.urls'

#TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                # os.path.join(BASE_DIR, 'products/templates'),                             # additional path in order to avoid app/'some_template.html'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'bootcamp.context_processors.products',                                         # custom context for products app
                'bootcamp.context_processors.footer_app_name',                                  # custom context for products app (manual APP_NAME_1)
                'bootcamp.context_processors.root',                                             # custom context for getting path to a webpage
                # 'bootcamp.context_processors.appname',                                        # custom context for products app
                # 'products.context_processors.appname',                                        # custom context for getting app_name
                # 'products.context_processors.context_appname',
                # 'bootcamp.context_processors.context_appname',
                # 'bootcamp.context_processors.resolver_context_processor',
                # 'products.context_processors.resolver_context_processor',
                'bootcamp.context_processors.detailed_method',
                #'bootcamp.context_processors.get_app_from_urls'                                # custom app_info_1 grabbed from urls.py
                
            ],
        },
    },
]

WSGI_APPLICATION = 'bootcamp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# STATICFILES_DIRS = [
#    os.path.join('/var/www/static/'),
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


PRODUCTS_GROUP = 'THE PRODUCT STORE'
PRODUCTS_TAGLINE = 'The latest incomes of products/manufacturers/prices/updates'

# setup as automated in context processors
# ROOT_PAGE = 'root url'
# ROOT_TAGLINE = 'root tagline'


MAIN_PAGE = 'BOOTCAMP/MAIN PAGE'
MAIN_PAGE_TAGLINE = 'bootcamp main page tagline'


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


METHOD = 'METHODS'

#django-paypal settings
PAYPAL_RECEIVER_EMAIL = 'andriyproniyk@gmail.com'
PAYPAL_TEST = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
CRISPY_FORMS_TEMPLATE_PACK = 'bootstrap4'


