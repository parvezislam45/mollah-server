import os
import sys

# Path to your project root (folder containing manage.py)
sys.path.append("/home/bigbazar")  

# Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "serverinventory.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
