import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings.dev'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
