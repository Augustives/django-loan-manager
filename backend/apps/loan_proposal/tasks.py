from apps.loan_proposal.constants import Status
from apps.loan_proposal.models import LoanProposal
from celery import shared_task
from django.utils import timezone


@shared_task
def process_loan_proposals(loan_proposal_id):
    loan_proposal: LoanProposal = LoanProposal.objects.get(id=loan_proposal_id)
    loan_proposals_count = LoanProposal.objects.count()

    # Approves half of the proposals and deny the other half,
    # first two are denys becuse it starts at 0
    if loan_proposals_count != 0 and loan_proposals_count % 2 == 0:
        loan_proposal.status = Status.APPROVED
    else:
        loan_proposal.status = Status.DENIED

    loan_proposal.processed_at = timezone.now()

    loan_proposal.save(update_fields=["status", "processed_at"])
