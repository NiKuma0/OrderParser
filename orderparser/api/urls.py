from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import DealViewSet, UserViewSet

router = SimpleRouter()

router.register(r"order", DealViewSet)
router.register(r"user", UserViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
