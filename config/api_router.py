from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from tiwix.users.api.views import UserViewSet
from tiwix.budget.api.views import TransactionViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("budget/transactions", TransactionViewSet, basename="transactions")


app_name = "api"
urlpatterns = router.urls
