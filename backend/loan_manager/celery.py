import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "loan_manager.settings")
app = Celery(
    "loan_manager",
    broker=os.environ.get("CELERY_BROKER_TRANSPORT_URL"),
    backend="rpc://",
    broker_connection_retry_on_startup=True,
)
app.conf.update(
    CELERY_ACCEPT_CONTENT=["application/json"],
    CELERY_TASK_SERIALIZER="json",
    CELERY_RESULT_SERIALIZER="json",
)
app.autodiscover_tasks(["apps"])
