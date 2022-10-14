from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin

from tiwix.budget.api.serializers import TransactionSerializer, CategorySerializer
from tiwix.budget.models import Transaction, Category


class TransactionViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    # url_name = 'transactions'
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self, *args, **kwargs):
        assert isinstance(self.request.user.id, int)
        return self.queryset.filter(id=self.request.user.id)


class CategoryViewSet(
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
