import os
from celery import Celery
from decouple import config


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerisproj.settings')

app = Celery('celerisproj')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()