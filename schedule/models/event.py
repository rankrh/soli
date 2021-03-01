from django.db import models
from django.db.models import CASCADE

from crop.models.crop import Crop


class Event(models.Model):

    class Meta:
        db_table = "event"
        app_label = "schedule"

    date = models.DateField()
    crop = models.ForeignKey(Crop, on_delete=CASCADE)