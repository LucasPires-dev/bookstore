from rest_framework.viewsets import ModelViewSet

from ..models import Product
from ..permissions import ReadOnlyForAuthenticatedOrFullAccessForSuperUser
from ..serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    #permission_classes = [ReadOnlyForAuthenticatedOrFullAccessForSuperUser]

    def get_queryset(self):
        return Product.objects.all().order_by("id")