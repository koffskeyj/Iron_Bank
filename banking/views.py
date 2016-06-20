from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from banking.models import Transaction
import datetime

class IndexView(TemplateView):
    template_name = "index.html"


class CreateUserView(CreateView):

    model = User
    form_class = UserCreationForm
    success_url = "/login"

class TransactionView(LoginRequiredMixin, ListView):

     def get_queryset(self):
         return Transaction.objects.filter(user=self.request.user).filter(created__lte=datetime.datetime.today(), created__gt=datetime.datetime.today()-datetime.timedelta(days=30))

     def get_context_data(self):
         context = super().get_context_data()
         balance = 0
         transactions = Transaction.objects.filter(user=self.request.user)
         for transaction in transactions:
             if transaction.transaction_method == "Credit":
                balance += transaction.amount
             if transaction.transaction_method == "Debit":
                balance -= transaction.amount
         context['balance'] = balance
         return context

     class Meta:
         ordering = ["-created"]
