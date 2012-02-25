import os
import sys

### FOR DEPLOYMENT: Need to change to path in deployment machine ###
_DJANGO_SITE_PATH = '/home/rahmad/workspace/django_site'

_APP_NAME = 'belajar_program'

sys.path.append(_DJANGO_SITE_PATH)
os.environ['DJANGO_SETTINGS_MODULE'] = _APP_NAME + '.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

