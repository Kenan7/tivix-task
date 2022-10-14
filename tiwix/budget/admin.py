from django.contrib import admin
from tiwix.budget.models import Transaction, Category

admin.site.register(Transaction)
admin.site.register(Category)