from .base import *
from django.utils.translation import ugettext as _

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'test'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'savior',
        'USER': 'root',
        'PASSWORD': 'root',
        'PORT': ''
    }
}

SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.mysql'
}

STATIC_ROOT = 'C:\Development\kosciolzbawiciela.pl\church-static'
STATIC_URL = '/static/'
MEDIA_ROOT = 'C:\Development\kosciolzbawiciela.pl\church-media'
MEDIA_URL = '/media/'

CKEDITOR_UPLOAD_PATH = 'ckeditor/'

TIME_ZONE = 'Europe/Warsaw'