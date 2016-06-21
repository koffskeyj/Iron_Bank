from django.contrib import admin
from banking.models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('business', 'amount', 'transaction_type', 'created', 'user')

admin.site.register(Transaction, TransactionAdmin)
