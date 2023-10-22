from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView

from auth.serializers import UserSerializer


class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = ()

