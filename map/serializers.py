from rest_framework import serializers

from map.models import Methodology, Activity


class MethodologySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, allow_null=True)

    class Meta:
        model = Methodology
        fields = ('id', 'title', 'description')


class ActivitySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, allow_null=True)
    methodology_id = serializers.IntegerField(required=True)

    class Meta:
        model = Activity
        fields = ('id', 'title', 'description', 'methodology_id')
