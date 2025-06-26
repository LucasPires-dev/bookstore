from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product import viewsets

router = DefaultRouter()
router.register(r'all', viewsets.ProductViewSet, basename='product')
router.register(r'categories', viewsets.CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls)),
]