from django.db import models
from django.db.models import CASCADE

from aria.models.plotTypes.plotType import PlotType
from aria.models.livestock import Livestock


class Pasture(models.Model):
    class Meta:
        db_table = "pasture"
        app_label = "aria"

    plot = models.ForeignKey(PlotType, on_delete=CASCADE)
    stockrate = models.FloatField()
    livestock = models.ForeignKey(Livestock, on_delete=CASCADE)
