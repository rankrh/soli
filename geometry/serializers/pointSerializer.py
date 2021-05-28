from rest_framework import serializers
from geometry.models.point import Point


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ["shape", "order", "set", "lat", "long"]
