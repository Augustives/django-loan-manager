import uuid

from django.db import models
from django.utils import timezone

from apps.customer.models import Customer
from apps.loan_proposal.constants import Status


class LoanProposal(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    processed_at = models.DateTimeField(null=False, blank=True, default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    value = models.DecimalField(
        null=False, blank=False, decimal_places=2, max_digits=12
    )
    status = models.CharField(
        null=False, blank=True, max_length=8, choices=Status.choices
    )
