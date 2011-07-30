import os
import sys

#HERE = os.path.dirname(os.path.abspath(__file__))
#sys.path += [os.path.join(HERE, 'lbforum_site')]

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
