from rest_framework import serializers
from farm.models.farm import Farm


class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = (
            "location",
            "description",
            "name",
            "logo",
            "climate",
            "year",
            "slug",
            "phone",
            "email",
            "address",
            "address2",
            "city",
            "state",
            "zip",
        )

    def create(self, validated_data):
        return Farm.objects.create(**validated_data)

    def update(self, farm, validated_data):
        farm.name = validated_data.get("name", farm.name)

        farm.save()
        return farm
