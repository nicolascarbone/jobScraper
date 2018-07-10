from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simplify.settings')

# app = Celery('crowdtime', include=['main.tasks'])

# broker='rabbit://guest:guest@172.18.0.2:5672/0',
app = Celery('simplify')
# , include=['vendors.crawlers']
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
# WARNING: UTC time configuration
# app.conf.beat_schedule = {
#     'send-reminder-every-friday': {
#         'task': 'main.tasks.send_timesheet_submit_reminder_weekly',
#         'schedule': crontab(hour='21',day_of_week='fri')
#     },
#     'send-reminder-every-end-of-month': {
#         'task': 'main.tasks.send_timesheet_submit_reminder_monthly',
#         'schedule': crontab(hour='21',day_of_week='mon-fri')
#     },
# }


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
