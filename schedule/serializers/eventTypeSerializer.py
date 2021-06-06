from rest_framework import serializers

from schedule.models.eventType import EventType


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ("name", "description")
