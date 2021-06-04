from rest_framework import serializers

from schedule.models.event import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "farmer",
            "calendar",
            "event_type",
            "start",
            "end",
            "name",
        )
