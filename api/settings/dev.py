from .base import *
from django.utils.translation import ugettext as _

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'test'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':     'savior',
        'USER':     'root',
        'PASSWORD': '',
        'HOST':     '',
        'PORT': ''
    }
}

SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.mysql'
}

STATIC_URL = '/static/'
MEDIA_ROOT = 'D:\Development\church-media'
MEDIA_URL = '/media/'

TIME_ZONE = 'Europe/Warsaw'