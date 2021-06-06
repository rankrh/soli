from django.db import models
from django.db.models import CASCADE

from climate.models.hardinessZone import HardinessZone
from schedule.models.event import Event


class Climate(models.Model):
    class Meta:
        db_table = "climate"
        app_label = "climate"

    zone = models.ForeignKey(
        HardinessZone, null=True, blank=True, on_delete=CASCADE, default=13
    )

    growing_season = models.ForeignKey(Event, on_delete=CASCADE, null=True, blank=True)
