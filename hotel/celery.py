from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
# from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel.settings')

app = Celery('hotel')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# CELERY_BEAT_SCHEDULE config
app.conf.beat_schedule = {
    'enviar_confirmacao_reserva': {
        'task': 'bookings.tasks.send_user_email',
        'task': 'bookings.liberar_quartos_cancelados',
        'schedule': crontab(minute='1', hour='*'),
    },
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')



# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')


# CELERY_EMAIL_BACKEND = 'django_celery_email.backends.CeleryEmailBackend'
# CELERY_TASK_EMAIL_SENDER = 'django.core.mail.backends.smtp.EmailBackend'
