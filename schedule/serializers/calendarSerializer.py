from rest_framework import serializers

from schedule.models.calendar import Calendar
from schedule.models.event import Event
from schedule.serializers.eventSerializer import EventSerializer


class CalendarSerializer(serializers.ModelSerializer):

    events = serializers.SerializerMethodField("_serialize_events")

    def _serialize_events(self, calendar):
        events = Event.objects.filter(calendar=calendar)

        return EventSerializer(events, many=True).data

    class Meta:
        model = Calendar
        fields = ("id", "farmer", "events")
