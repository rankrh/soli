from django.db import models
from django.db.models import CASCADE

from aria.models.livestock import Livestock
from aria.models.plot import Plot


class Pasture(models.Model):
    class Meta:
        db_table = "pasture"
        app_label = "aria"

    plot = models.ForeignKey(Plot, on_delete=CASCADE)
    stockrate = models.FloatField()
    livestock = models.ForeignKey(Livestock, on_delete=CASCADE)
