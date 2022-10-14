from django.db import models
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()

"""
Transaction
 
- value
- description
- title
 - category_id
- type (+ or -)
- user_id

Category
- name
 
"""

EXPENSE = 0
INCOME = 1

TRANSACTION_TYPE_CHOICES = (
    (EXPENSE, 'Expense'),
    (INCOME, 'Income')
)

class Transaction(models.Model):
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    description = models.CharField(max_length=200, blank=True, null=True)

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='transactions',
        blank=True,
        null=True
    )

    type = models.IntegerField(choices=TRANSACTION_TYPE_CHOICES)

    user = models.ForeignKey(
        USER_MODEL,
        on_delete=models.CASCADE,
        related_name='transactions'
    )

    def get_type_display(self):
        return TRANSACTION_TYPE_CHOICES[self.type][1]

    def __str__(self):
        return f"{self.amount} {self.description}"


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
