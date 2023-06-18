import pytest
from apps.customer.models import Customer


@pytest.fixture
def brazilian_customer_data(brazilian_address) -> dict:
    yield {"name": "Foo Bar", "cpf": "19596881035", "address": brazilian_address}


@pytest.fixture
def brazilian_customer(brazilian_customer_data) -> Customer:
    yield Customer.objects.create(**brazilian_customer_data)
