"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_NAME = os.path.basename(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xdj62#or8x5&ek@*ak+bdd0d1egw$4z1vl!i&p=p$g2vufue)+'
# シークレットキーを設定ファイル外から読み込む場合はpip install django_environした後　
# $ export SECRET_KEY = 'xdj62#or8x5&ek@*ak+bdd0d1egw$4z1vl!i&p=p$g2vufue)+'
# import environ
# env = enviorn.Env()
# SECRET_KEY = env('SECRET_KEY')

# exportしたくない場合は.envファイルにSECRET_KEY = 'xdj62#or8x5&ek@*ak+bdd0d1egw$4z1vl!i&p=p$g2vufue)+'を書いておき
# import environ
# env = enviorn.Env()
# env.read_env(os.path.join(BASE_DIR, '.env'))
# SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    'shop.apps.ShopConfig',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': 'test',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'ATOMIC_REQUESTS': True,
        'OPTIONS':{
            'sql_mode': 'TRADITIONAL,NO_AUTO_VALUE_ON_ZERO',
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

LOGGING = {
    'version': 1,
    # 既存のログ設定を無効化しない
    'disable_existing_loggers': False,
    # ログフォーマット
    'formatters': {
        # 本番用
        'production': {
            'format': '%(asctime)s [%(levelname)s] %(process)d %(thread)d '
                      '%(pathname)s:%(lineno)d %(message)s'
        },
        # 開発用
        'develop':{
            'format': '%(asctime)s [%(levelname)s] %(pathname)s:%(lineno)d ' 
                      '%(message)s'
        }
    },
    # ハンドラ
    'handlers': {
        # ファイル出力用ハンドラ
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/{}.log'.format(PROJECT_NAME),
            'formatter': 'production',
        },
        # コンソール出力用ハンドラ
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'production',
        },
    },
    # ロガー
    'loggers': {
        # 自作アプリ全般のログを拾うロガー
        '': {
            'handlers': ['file'], # 開発時は['console']
            'level': 'INFO', # 開発時は'DEBUG'
            'propagate': False,
        },
        # Django本体がだすログ全般を拾うロガー
        'django': {
            'handlers': ['file'], # 開発時は['console']
            'level': 'INFO',
            'propagate': False,
        },
        # 開発用：発行されるSQL文を出力するための設定
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        }
    },
}

SECURE_SSL_REDIRECT = True

AUTH_USER_MODEL = 'accounts.CustomUser'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/{}/media'.format(PROJECT_NAME)
#PaaSにDjangoサイトをデプロイする際にWhiteNoiseを利用する場合は下記を使う
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = '/var/www/{}/static'.format(PROJECT_NAME)
