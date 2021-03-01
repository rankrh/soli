from django.db import models
from django.db.models import CASCADE

from climate.models.hardinessZone import HardinessZone


class Climate(models.Model):

    class Meta:
        db_table = "climate"
        app_label = "climate"

    zone = models.ForeignKey(
        HardinessZone,
        null=False,
        blank=False,
        on_delete=CASCADE,
        default=13)

    firstFrost = models.DateField()
    lastFrost = models.DateField()
