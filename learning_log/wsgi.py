"""
WSGI config for learning_log project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')

application = Cling(get_wsgi_application())

# We modified wsgi.py for Heroku, because Heroku needs a slightly different
# setup than what we've been using. We import Cling, which helps serve static
# files correctly, and use it to launch the application. This code will work
# locally as well, so we don't need to put it in an if block.
