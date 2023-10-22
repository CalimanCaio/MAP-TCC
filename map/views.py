from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from map.models import Methodology
from map.serializers import MethodologySerializer


# Create your views here.
class MethodologyList(generics.ListCreateAPIView):
    queryset = Methodology.objects.all()
    serializer_class = MethodologySerializer
