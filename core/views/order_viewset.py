from rest_framework.viewsets import ModelViewSet

from ..models import Order
from ..permissions import ReadOnlyForAuthenticatedOrFullAccessForSuperUser
from ..serializers import OrderSerializer


class OrderViewSet(ModelViewSet):

    serializer_class = OrderSerializer
    permission_classes = [ReadOnlyForAuthenticatedOrFullAccessForSuperUser]
    queryset = Order.objects.all().order_by("id")