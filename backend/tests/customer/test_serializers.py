import pytest
from apps.customer.serializers import CustomerSerializer


class TestCustomerSerializer:
    @pytest.mark.parametrize(
        "cpf,expected_validation",
        [
            ("82199845036", True),
            ("12549231015", True),
            ("128972580204", False),
            ("6505245308", False),
        ],
    )
    def test_cpf_validation(self, cpf, expected_validation, brazilian_address_data):
        serializer = CustomerSerializer(
            data={"name": "Foo Bar", "cpf": cpf, "address": brazilian_address_data}
        )
        assert serializer.is_valid() == expected_validation
