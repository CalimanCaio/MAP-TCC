from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from custom_auth.views import CreateUserView

urlpatterns = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', CreateUserView.as_view(), name='register'),
]