import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "laboratory_work_3.settings")

application = get_wsgi_application()
