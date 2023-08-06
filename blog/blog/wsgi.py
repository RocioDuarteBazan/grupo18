"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
# add your proyect directory to the sys.path
project_home = '/home/informatorio/grupo18/'
if project_home not in sys.path:
    sys.path.insert(0, project_home)
#set environment variable to tell django where your settings.py is
# os.environ['DJANGO_SETTINGS_MODULE´] = 'blog.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
# serve django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
