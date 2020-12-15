from django.db import models
from django.db.models import CASCADE

from aria.models.plotTypes.plotType import PlotType


class Field(models.Model):
    class Meta:
        db_table = "field"
        app_label = "aria"

    plot = models.ForeignKey(PlotType, on_delete=CASCADE)

