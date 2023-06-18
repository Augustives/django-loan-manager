from apps.loan_proposal.serializers import LoanProposalSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class LoanProposalAPIView(APIView):
    def post(self, request):
        loan_proposal_serializer = LoanProposalSerializer(data=request.data)
        if loan_proposal_serializer.is_valid():
            loan_proposal_serializer.save()
            return Response(
                loan_proposal_serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            loan_proposal_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
