import django, os
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'utils.settings')

def pytest_configure():
    settings.DEBUG = False
    django.setup()