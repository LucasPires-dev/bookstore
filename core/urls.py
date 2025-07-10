from django.urls import include, path
from rest_framework import routers
from core import views

router = routers.SimpleRouter()
router.register(r"order", views.OrderViewSet, basename="order")
router.register(r"product", views.ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
]