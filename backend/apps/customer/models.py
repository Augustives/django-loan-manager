import uuid

from apps.address.models import Address
from django.db import models


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    cpf = models.CharField(null=False, blank=False, max_length=11)
    address = models.ForeignKey(
        Address, verbose_name="Addresses", on_delete=models.PROTECT
    )
