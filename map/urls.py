from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from custom_auth.views import CreateUserView
from map.views import MethodologyList

urlpatterns = [
    path('methodologies/', MethodologyList.as_view(), name='methodology-list'),
]
