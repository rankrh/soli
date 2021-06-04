from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from schedule.models.calendar import Calendar
from schedule.models.eventType import EventType


class Event(models.Model):
    class Meta:
        db_table = "event"
        app_label = "schedule"

    farmer = models.ForeignKey(User, on_delete=CASCADE, null=True)
    calendar = models.ForeignKey(Calendar, on_delete=CASCADE)
    event_type = models.ForeignKey(EventType, on_delete=CASCADE, null=True)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=64)
