from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    DEPOSIT = 'Deposit'
    WITHDRAWAL = 'Withdrawal'
    TRANSACTION_TYPE_CHOICES = ((DEPOSIT, 'Deposit'), (WITHDRAWAL, 'Withdrawal'))

    business = models.CharField(max_length=30)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=15, choices=TRANSACTION_TYPE_CHOICES, default=DEPOSIT)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business


    class Meta:
        ordering = ['-created']
