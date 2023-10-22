from rest_framework import generics

from map.models import Methodology
from map.serializers import MethodologySerializer


# Create your views here.
class MethodologyListCreate(generics.ListCreateAPIView):
    queryset = Methodology.objects.all()
    serializer_class = MethodologySerializer


class MethodologyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Methodology.objects.all()
    serializer_class = MethodologySerializer
