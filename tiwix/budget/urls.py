from django.urls import path

from tiwix.budget.views import BudgetExpenseCreateView

app_name = "budget"
urlpatterns = [
    path('expenses/add/', BudgetExpenseCreateView.as_view(), name='expense-create'),
]