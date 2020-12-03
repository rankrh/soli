from django.core.validators import MinValueValidator
from django.db import models
from .plot import Plot


class Point(models.Model):
    class Meta:
        db_table = "point"
        app_label = "aria"

    pt_num = models.AutoField(primary_key=True)
    pt_plt_num = models.ForeignKey(Plot, db_column="pt_plt_num")
    pt_order = models.IntegerField(validators=[MinValueValidator(0)])
    pt_lat = models.FormField()
    pt_long = models.FloatField()