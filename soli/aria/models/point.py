from django.core.validators import MinValueValidator
from django.db import models
from .plot import Plot


class Point(models.Model):
    class Meta:
        db_table = "point"
        app_label = "aria"

    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    order = models.IntegerField(validators=[MinValueValidator(0)])
    set = models.IntegerField(validators=[MinValueValidator(0)])
    lat = models.FloatField()
    long = models.FloatField()
