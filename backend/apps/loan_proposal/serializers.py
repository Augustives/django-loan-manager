from apps.customer.models import Customer
from apps.customer.serializers import CustomerSerializer
from apps.loan_proposal.models import LoanProposal
from apps.loan_proposal.tasks import process_loan_proposals
from rest_framework import serializers


class LoanProposalSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()

    class Meta:
        model = LoanProposal
        fields = [
            "id",
            "customer",
            "value",
            "status",
            "processed_at",
            "created_at",
        ]

    def create(self, validated_data):
        customer_data = validated_data.pop("customer")
        customer_serializer = CustomerSerializer(data=customer_data)
        customer_serializer.is_valid(raise_exception=True)
        customer: Customer = customer_serializer.save()

        loan_proposal = LoanProposal.objects.create(customer=customer, **validated_data)
        process_loan_proposals.delay(loan_proposal.id)

        return loan_proposal
