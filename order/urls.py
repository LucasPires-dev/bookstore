from django.urls import path, include
from rest_framework.routers import DefaultRouter

from order import viewsets

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'', viewsets.OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]