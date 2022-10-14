from rest_framework import serializers

from tiwix.budget.models import Transaction, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id',
            'title',
            'amount',
            'description',
            'type',
            'category',
            'user'
        ]

    def get_type(self, obj):
        return obj.get_type_display()
