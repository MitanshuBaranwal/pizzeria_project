from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzeria_project.settings')

app = Celery('pizzeria_project')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')

# Use Redis as the message broker
app.conf.broker_url = 'redis://localhost:6379/0'  # Replace with your Redis server details

# Load task modules from all registered Django app configs.
app.config_from_object(settings, namespace='CELERY')

# Discover tasks in all installed apps
app.autodiscover_tasks()
@app.task(bind= True)
def debug_task(self):
    print(f'Request: {self.request!r}')
