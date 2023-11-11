from rest_framework import serializers

from map.models import Methodology, Activity, Project


class MethodologySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, allow_null=True)

    class Meta:
        model = Methodology
        fields = ('id', 'title')


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, allow_null=True)
    methodology_id = serializers.IntegerField(required=True)

    class Meta:
        model = Activity
        fields = ('id', 'title', 'methodology_id')


class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, allow_null=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'activities')
