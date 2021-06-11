from rest_framework import serializers

from crop.models.validation.plantValidation import GROW_STYLE


class CropFormSerializer(serializers.Serializer):
    patterns = GROW_STYLE
