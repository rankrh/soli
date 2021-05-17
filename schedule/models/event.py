from django.db import models
from django.db.models import CASCADE

from crop.models.crop import Crop
from schedule.models.calendar import Calendar


class Event(models.Model):
    class Meta:
        db_table = "event"
        app_label = "schedule"

    calendar = models.ForeignKey(Calendar, on_delete=CASCADE)
    date = models.DateField()
    crop = models.ForeignKey(Crop, on_delete=CASCADE)
