from rest_framework import serializers


class SidebarSubsectionSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True, max_length=32)
    id = serializers.CharField(read_only=True, max_length=16)
    icon = serializers.CharField(read_only=True, max_length=32)
    url = serializers.CharField(read_only=True, max_length=64)
    url_params = serializers.ListField(
        allow_empty=True, read_only=True, required=False, max_length=64
    )
    subsection_name = serializers.CharField(read_only=True, max_length=32)
