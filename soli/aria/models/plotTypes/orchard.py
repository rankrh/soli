from django.db import models
from django.db.models import CASCADE

from aria.models.plotTypes.plotType import PlotType


class Orchard(models.Model):
    class Meta:
        db_table = "orchard"
        app_label = "aria"

    plot = models.ForeignKey(PlotType, on_delete=CASCADE)

