from django.db import models
from .crop import Crop


class Plot(models.Model):
    class Meta:
        db_table = "plot"
        app_label = "aria"

    garden = models.ForeignKey('self', on_delete=models.CASCADE, db_column="garden")
    crop = models.ForeignKey(Crop, null=True, on_delete=models.SET_NULL)
    area = models.FloatField()
