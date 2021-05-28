from rest_framework import serializers

from geometry.models.shape import Shape


class ShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shape
        fields = ("type", "area", "length")
