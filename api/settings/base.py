import os
import sys

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

INSTALLED_APPS = (
    'modeltranslation', # must be put before django.contrib.admin when using Django 1.7 or above

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'adminsortable2',
    'ckeditor',
    'geoposition',
    'events',
    'south',
    'taggit',

    'savior.apps.savior',
    'savior.apps.service',
    'savior.apps.menu',
    'savior.apps.event',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'savior.lib.context_processor.menu_processor.menu_processor',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "savior", "templates"),
)

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}

EVENTS_MAX_FUTURE_OCCURRENCES = 5

SECRET_KEY = 'z@_%ro12sga#f2px#3^v#x$haez7&ei%q1f@r*=*w7p))-r!=6'
TAGGIT_CASE_INSENSITIVE = True
USE_TZ = True

ROOT_URLCONF = 'api.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'api.wsgi.application'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, "savior", "static"),
)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

DEFAULT_CAROUSEL_LINK_TEXT = 'Learn more'

LANGUAGE_CODE = 'pl'

LANGUAGES = (
    ('pl', 'Polish'),
    ('en', 'English'),
)

LOCALE_PATHS = (
    os.path.join(PROJECT_PATH, 'locale'),
)

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'