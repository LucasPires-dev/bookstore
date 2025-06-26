from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', include('order.urls')),
    path('products/', include('product.urls')),
    path('auth/', include('rest_framework.urls'))
]
