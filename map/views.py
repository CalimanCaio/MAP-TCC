from rest_framework import generics

from map.models import Methodology, Activity, Project
from map.serializers import MethodologySerializer, ActivitySerializer, ProjectSerializer


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


class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
