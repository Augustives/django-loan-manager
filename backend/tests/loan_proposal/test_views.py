from unittest.mock import ANY

import pytest
from rest_framework.test import APIClient


@pytest.mark.usefixtures("celery_app", "celery_worker")
@pytest.mark.django_db(transaction=True)
class TestLoanProposalViews:
    def test_loan_proposal_is_created_with_customer_and_address_in_a_post(
        self,
        loan_proposal_post_request_data,
    ):
        response = APIClient().post(
            "/loan-proposals/",
            loan_proposal_post_request_data,
            format="json",
        )

        assert response.json() == {
            "id": ANY,
            "customer": {
                "id": ANY,
                "name": "Foo Bar",
                "cpf": "19596881035",
                "address": {
                    "id": ANY,
                    "country": "BR",
                    "state": "SC",
                    "city": "Florianópolis",
                    "street": "Rua XYZ",
                    "postal_code": "885412369",
                    "additional_info": "",
                },
            },
            "value": "100.00",
            "status": "",
            "processed_at": ANY,
            "created_at": ANY,
        }
