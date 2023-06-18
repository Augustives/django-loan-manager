from typing import Generator

import pytest
from apps.loan_proposal.models import LoanProposal


@pytest.fixture
def loan_proposal_data(brazilian_customer) -> dict:
    yield {"value": 100, "customer": brazilian_customer}


@pytest.fixture
def loan_proposal(loan_proposal_data) -> LoanProposal:
    yield LoanProposal.objects.create(**loan_proposal_data)


@pytest.fixture
def loan_proposal_post_request_data(brazilian_address_data, brazilian_customer_data):
    yield {
        "value": 100,
        "customer": {**brazilian_customer_data, "address": brazilian_address_data},
    }
