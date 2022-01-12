import logging

from celery import Celery

app = Celery("tasks", broker="pyamqp://guest@worker//")

@app.task
def send_message(message: str) -> None:
    logging.info(message)
