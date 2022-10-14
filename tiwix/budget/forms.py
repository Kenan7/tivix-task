from django.forms import ModelForm
from tiwix.budget.models import Transaction, Category


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
            'description',
            'category',
        ]


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]
