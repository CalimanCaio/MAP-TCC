from rest_framework import serializers

from map.models import Methodology


class MethodologySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True, allow_null=True)

    class Meta:
        model = Methodology
        fields = ('id', 'title', 'description')
