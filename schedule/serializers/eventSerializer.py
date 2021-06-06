from rest_framework import serializers

from schedule.models.event import Event
from schedule.models.eventType import EventType
from schedule.serializers.eventTypeSerializer import EventTypeSerializer


class EventSerializer(serializers.ModelSerializer):

    event_type = EventTypeSerializer()

    class Meta:
        model = Event
        fields = (
            "calendar",
            "event_type",
            "start",
            "end",
            "name",
        )
