from rest_framework.viewsets import ModelViewSet

from ..models import Category
from ..permissions import ReadOnlyForAuthenticatedOrFullAccessForSuperUser
from ..serializers import CategorySerializer

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [ReadOnlyForAuthenticatedOrFullAccessForSuperUser]

    def get_queryset(self):
        return Category.objects.all().order_by("id")