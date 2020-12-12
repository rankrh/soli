from django.core.validators import MinValueValidator
from django.db import models

from . import Shape


class Point(models.Model):
    class Meta:
        db_table = "point"
        app_label = "aria"

    shape = models.ForeignKey(Shape,  null=True, default=None, on_delete=models.CASCADE)
    order = models.IntegerField(validators=[MinValueValidator(0)])
    set = models.IntegerField(validators=[MinValueValidator(0)])
    lat = models.FloatField()
    long = models.FloatField()
