from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from core.views import UserCreateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/", include("core.urls")),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
    path('api/users/register/', UserCreateAPIView.as_view(), name="register")
]
