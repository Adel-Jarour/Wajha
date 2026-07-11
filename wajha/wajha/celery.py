import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wajha.settings')

app = Celery('wajha')

# Read config from Django settings, all Celery keys start with CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks.py in every INSTALLED_APP
app.autodiscover_tasks()
