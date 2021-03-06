import os
import environ

from pathlib import Path


env = environ.Env(DEBUG=(bool, False))
root = environ.Path(__file__) - 3
env.read_env(root('.env'))

SITE_ID = 1
PROJECT_NAME = '1code'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')


ALLOWED_HOSTS = ['*']
AUTH_USER_MODEL = 'users.User'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_auth',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'storages',

    'users',
    'api_v1',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'backend.urls'


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


WSGI_APPLICATION = 'backend.wsgi.application'


DEFAULT_DATABASE = env.db('DATABASE_URL', default='psql://postgres:postgres@localhost:5432/onecode')
DEFAULT_DATABASE['DISABLE_SERVER_SIDE_CURSORS'] = True
DEFAULT_DATABASE['CONN_MAX_AGE'] = 600

DATABASES = {
    'default': DEFAULT_DATABASE,
}


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

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = ['http://localhost:3000',]
CORS_ALLOW_METHODS = ('GET', 'POST', 'OPTIONS', 'PATCH', 'PUT')


LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Asia/Yekaterinburg'
USE_I18N = True
USE_L10N = True
USE_TZ = True


AWS_S3_REGION_NAME = 'us-east-2'
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')

S3_PUBLIC_MIRROR_BASE_URL = env.str('S3_PUBLIC_MIRROR_BASE_URL', default='')

if S3_PUBLIC_MIRROR_BASE_URL:
    parsed_url = urlparse(S3_PUBLIC_MIRROR_BASE_URL)
    S3_CUSTOM_DOMAIN = f'{parsed_url.netloc}{parsed_url.path}'
else:
    S3_CUSTOM_DOMAIN = False

if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
    DEFAULT_FILE_STORAGE = 'backend.storages.MediaStorage'
    DEFAULT_PRIVATE_FILE_STORAGE = 'backend.storages.PrivateMediaStorage'
    MEDIAFILES_LOCATION = 'media'
    MEDIA_ROOT = f'/{MEDIAFILES_LOCATION}/'
    MEDIA_URL = urlunparse(('https', AWS_S3_HOST, f'{MEDIAFILES_LOCATION}/', '', '', ''))
else:
    DEFAULT_FILE_STORAGE = 'backend.storages.FileSystemStorage'
    DEFAULT_PRIVATE_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    MEDIAFILES_LOCATION = 'media'
    MEDIA_ROOT = 'media/'
    MEDIA_URL = '/media/'


STATIC_URL = env('STATIC_URL', default='/static/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (os.path.abspath(os.path.join(BASE_DIR, '../frontend/dist')),)

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
