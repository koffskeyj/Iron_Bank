from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, FormView
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


class CreateTransactionView(CreateView):

    model = Transaction
    fields = ["business", "amount", "transaction_type"]
    success_url = "/"

    def form_valid(self, form):
        transaction = form.save(commit=False)
        transaction.user = self.request.user
        return super().form_valid(form)


class CreateTransferView(LoginRequiredMixin, CreateView):

    model = Transaction
    template_name = "transfer.html"
    fields = ['amount', 'user']


class TransactionView(LoginRequiredMixin, ListView):

     def get_queryset(self):
         return Transaction.objects.filter(user=self.request.user).filter(created__lte=datetime.datetime.today(), created__gt=datetime.datetime.today()-datetime.timedelta(days=30))

     def get_context_data(self):
         context = super().get_context_data()
         balance = 0
         transactions = Transaction.objects.filter(user=self.request.user)
         for transaction in transactions:
             if transaction.transaction_type == "Deposit":
                balance += transaction.amount
             if transaction.transaction_type == "Withdrawal":
                balance -= transaction.amount
         context['balance'] = balance
         
         return context


class TransactionDetailedView(LoginRequiredMixin, DetailView):
    model = Transaction
    template_name = 'banking/detail_list.html'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
