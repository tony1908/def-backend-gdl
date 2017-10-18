"""
WSGI config for apiDamificados project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settingsEnv = "apiDamificados.settings." + os.environ.get('DJANGO_ENV')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", settingsEnv)

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apiDamificados.settings.development")

application = get_wsgi_application()
