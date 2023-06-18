from apps.address.models import Address
from apps.address.serializers import AddressSerializer
from apps.customer.models import Customer
from rest_framework import serializers
from validate_docbr import CPF


class CustomerSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Customer
        fields = ["id", "name", "cpf", "address"]

    def validate_cpf(self, value):
        if not CPF().validate(value):
            raise serializers.ValidationError("Invalid CPF.")
        return value

    def create(self, validated_data):
        address_data = validated_data.pop("address")
        address_serializer = AddressSerializer(data=address_data)
        address_serializer.is_valid(raise_exception=True)
        address: Address = address_serializer.save()

        return Customer.objects.create(address=address, **validated_data)
