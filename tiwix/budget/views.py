from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from tiwix.budget.models import Transaction, Category, EXPENSE, INCOME
from tiwix.budget.forms import TransactionForm


class BudgetTransactionsListView(ListView):
    model = Transaction
    template_name = 'budget/home.html'
    context_object_name = 'transactions'
    queryset = Transaction.objects.all()


class BudgetExpenseCreateView(CreateView):
    template_name = 'budget/expense_create.html'
    form_class = TransactionForm
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {'type': EXPENSE}
        return kwargs