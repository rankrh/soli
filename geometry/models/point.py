from django.core.validators import MinValueValidator
from django.db import models

from geometry.models.shape import Shape


class Point(models.Model):

    class Meta:
        db_table = "point"
        app_label = "geometry"

    shape = models.ForeignKey(Shape, blank=True, null=True, default=None, on_delete=models.CASCADE)
    order = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    set = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    lat = models.FloatField()
    long = models.FloatField()

    def getCoordinates(self):
        return (self.lat, self.long)
