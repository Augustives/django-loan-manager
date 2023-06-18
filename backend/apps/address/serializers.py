from apps.address.models import Address
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "country",
            "state",
            "city",
            "street",
            "postal_code",
            "additional_info",
        ]
