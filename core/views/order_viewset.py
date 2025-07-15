from rest_framework import viewsets
from core.models.order import Order
from core.serializers.order_serializer import OrderSerializer
from core.permissions import ReadAndPostOnlyForAuthenticatedOrFullAccessForSuperUser

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [ReadAndPostOnlyForAuthenticatedOrFullAccessForSuperUser]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
