from apps.customer.models import Customer
from django.contrib import admin


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "cpf")
    search_fields = ("id", "name", "cpf")


admin.site.register(Customer, CustomerAdmin)
