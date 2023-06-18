import pytest
from apps.loan_proposal.models import LoanProposal
from apps.loan_proposal.tasks import process_loan_proposals


@pytest.mark.usefixtures("celery_app", "celery_worker")
@pytest.mark.django_db(transaction=True)
class TestLoanProposalTasks:
    def test_process_loan_proposals(self, loan_proposal):
        process_loan_proposals.delay(str(loan_proposal.id)).get()
        assert LoanProposal.objects.first().status == "Denied"

    @pytest.mark.usefixtures("loan_proposal")
    def test_process_loan_proposals_denys_half_and_approves_the_other_half_of_the_proposals(
        self,
        brazilian_customer,
    ):
        loan_proposals_data = [
            {"value": 146, "customer": brazilian_customer},
            {"value": 789, "customer": brazilian_customer},
            {"value": 45, "customer": brazilian_customer},
            {"value": 4823, "customer": brazilian_customer},
        ]

        for loan_proposal_data in loan_proposals_data:
            loan_proposal = LoanProposal.objects.create(**loan_proposal_data)
            process_loan_proposals.delay(str(loan_proposal.id)).get()

        assert LoanProposal.objects.filter(status="Denied").count() == 2
        assert LoanProposal.objects.filter(status="Approved").count() == 2
