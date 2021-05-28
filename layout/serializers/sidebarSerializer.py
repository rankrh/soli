from rest_framework import serializers

from layout.serializers.sidebarSectionSerializer import SidebarSectionSerializer


class SidebarSerializer(serializers.Serializer):
    sections = SidebarSectionSerializer(many=True, required=False)
