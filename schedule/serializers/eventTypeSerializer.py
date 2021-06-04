from rest_framework import serializers

from schedule.models.eventType import EventType


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ("name", "description")
