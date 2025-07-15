from django.urls import include, path
from rest_framework import routers
from core import views

router = routers.SimpleRouter()
router.register(r"orders", views.OrderViewSet, basename="order")
router.register(r"products", views.ProductViewSet, basename="product")
router.register(r"categories", views.CategoryViewSet, basename="categories")

urlpatterns = [
    path("", include(router.urls)),
]