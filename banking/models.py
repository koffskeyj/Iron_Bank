from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    DEBIT = 'Debit'
    CREDIT = 'Credit'
    DEPOSIT = 'Deposit'
    WITHDRAWAL = 'Withdrawal'
    TRANSACTION_METHOD_CHOICES = ((DEBIT,'Debit'), (CREDIT, 'Credit'))
    TRANSACTION_TYPE_CHOICES = ((DEPOSIT, 'Deposit'), (WITHDRAWAL, 'Withdrawal'))

    business = models.CharField(max_length=30)
    amount = models.FloatField()
    transaction_method = models.CharField(max_length=15, choices=TRANSACTION_METHOD_CHOICES, default=DEBIT)
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE_CHOICES, default=DEPOSIT)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business
