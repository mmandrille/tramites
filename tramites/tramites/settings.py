"""
Django settings for tramites project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eyf9r00nwbfn7av6%n!xffz(tg@v!a)-_(#n&zp07(j*8wce3%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'www.tramites.jujuy.gob.ar','tramites.jujuy.gob.ar']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #PlugIns Extras
    'tinymce',
    #Desarrollos personales
    'core.apps.CoreConfig',
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

ROOT_URLCONF = 'tramites.urls'

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

WSGI_APPLICATION = 'tramites.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/
LANGUAGE_CODE = 'es-AR'
TIME_ZONE = 'America/Argentina/Jujuy'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
#Configuraciones Propias
MEDIA_URL = 'archivos/'
MEDIA_ROOT = os.path.join(BASE_DIR, "archivos")
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_source"),
]

#Sistema de accesos:
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = '/'

#Configuracion de Mail
EMAIL_USE_TLS = True
EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_HOST_USER = 'tucorreo@dominio.com'
EMAIL_HOST_PASSWORD = 'tupassword'
#CREAR ARCHIVO credenciales.py solo para Sobre Escribir con las variables importadas
try:
    from .credenciales import *
except ImportError:
    pass

#Actualizar Statics, no solo nuevas
AWS_PRELOAD_METADATA = True

#Configuramos Tinymce
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,xhtmlxtras,paste,searchreplace",
    'theme': "advanced",
    "theme_advanced_buttons3_add" : "cite,abbr",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'width': '70%',
    'height': '600',
}