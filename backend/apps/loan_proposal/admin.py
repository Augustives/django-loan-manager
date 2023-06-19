from apps.loan_proposal.models import LoanProposal
from django.contrib import admin


class LoanProposalAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "value", "status")
    list_filter = ["status"]
    search_fields = ("id", "customer__name", "customer__cpf", "status")


admin.site.register(LoanProposal, LoanProposalAdmin)
