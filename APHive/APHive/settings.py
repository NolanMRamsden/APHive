
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b9af6qnoe8hd&oxdxtor6jj6g41-qkma^)4g9p^fg*pwrk9-s%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'APHive/templates/APHive'),
    os.path.join(BASE_DIR, 'apis/templates/apis'),
    os.path.join(BASE_DIR, 'members/templates/members'),
    os.path.join(BASE_DIR, 'reviews/templates/reviews'),
    os.path.join(BASE_DIR, 'endpoints/templates/APHive'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members',
    'apis',
    'reviews',
    'endpoints',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'APHive.urls'

WSGI_APPLICATION = 'APHive.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "APHive/static"),
    os.path.join(BASE_DIR, "apis/static"),
    os.path.join(BASE_DIR, "members/static"),
    os.path.join(BASE_DIR, "reviews/static"),
    os.path.join(BASE_DIR, "endpoints/static"),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

