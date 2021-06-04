from rest_framework import serializers

from schedule.models.calendar import Calendar


class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = "owner"
