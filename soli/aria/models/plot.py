from django.db import models
from django.db.models import CASCADE

from .plotTypes.plotType import PlotType
from .shape import POLYGON, Shape


class Plot(models.Model):
    class Meta:
        db_table = "plot"
        app_label = "aria"

    name = models.CharField(max_length=128, blank=True, default="Unnamed Plot")
    shape = models.ForeignKey(Shape, null=True, default=None, on_delete=CASCADE)
    description = models.CharField(max_length=1024, blank=True, default="")
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=CASCADE)
    type = models.ForeignKey(PlotType, blank=True, null=True, on_delete=CASCADE)

    def save(self):

        if self.shape is None:
            self.shape = Shape(type=POLYGON)
            self.shape.save()

        super(Plot, self).save()
