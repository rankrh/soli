from django.db import models
from .crop import Crop


class Plot(models.Model):
    class Meta:
        db_table = "plot"
        app_label = "aria"

    name = models.CharField(max_length=128, blank=True, default="Unnamed Plot")
    description = models.CharField(max_length=1024, blank=True, default="")
    area = models.FloatField(blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
