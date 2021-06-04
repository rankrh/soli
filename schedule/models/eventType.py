from django.db import models
from django.db.models import CASCADE
from schedule.models.calendar import Calendar


class EventType(models.Model):
    class Meta:
        db_table = "eventtype"
        app_label = "schedule"

    name = models.CharField(max_length=32)
    description = models.CharField(max_length=512)
