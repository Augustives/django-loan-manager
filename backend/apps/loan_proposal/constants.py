from django.db.models import TextChoices


class Status(TextChoices):
    APPROVED = "Approved"
    DENIED = "Denied"
