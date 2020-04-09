from django.db import models
from .plot import Plot


class CropPosition(models.Model):
    class Meta:
        db_table = "cropPosition"
        app_label = "aria"

    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    X = models.FloatField()
    Y = models.FloatField()


