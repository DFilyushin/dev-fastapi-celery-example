import os
import time

from celery import Celery, shared_task

app = Celery("config", broker="redis://localhost:6379/0")
app.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379/0")
app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")


@app.task
def create_task(task_type):
    print(f"Создана задача {task_type} {time.time()}")
