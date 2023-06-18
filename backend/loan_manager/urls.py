from django.contrib import admin
from django.urls import path

from apps.loan_proposal.views import LoanProposalAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("loan-proposals/", LoanProposalAPIView.as_view(), name="loan-proposals"),
]
