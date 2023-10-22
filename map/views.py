from rest_framework import generics

from map.models import Methodology, Activity
from map.serializers import MethodologySerializer, ActivitySerializer


# Create your views here.
class MethodologyListCreate(generics.ListCreateAPIView):
    queryset = Methodology.objects.all()
    serializer_class = MethodologySerializer


class MethodologyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Methodology.objects.all()
    serializer_class = MethodologySerializer


class ActivityListCreate(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ActivityRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
