from apps.loan_proposal.models import LoanProposal
from django.contrib import admin


class LoanProposalAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "value")
    search_fields = ("id", "customer__name", "customer__cpf")


admin.site.register(LoanProposal, LoanProposalAdmin)
