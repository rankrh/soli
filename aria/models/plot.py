from django.db import models
from .crop import Crop


class Plot(models.Model):
    plotId = models.AutoField(primary_key=True)
    garden = models.ForeignKey('self', on_delete=models.CASCADE, db_column="garden")
    crop = models.ForeignKey(Crop, null=True, on_delete=models.SET_NULL)
    area = models.FloatField()

    class Meta:
        db_table = "plot"
        app_label = "aria"
