import os

from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", 'redis://127.0.0.1:6379')
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", 'redis://127.0.0.1:6379')

@celery.task()
def add():
    with open('data.txt', 'w') as f:
        f.write('test')
    return 'ok'