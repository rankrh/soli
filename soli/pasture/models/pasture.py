from django.db import models
from django.db.models import CASCADE

from animal.models.animal import Animal
from plot.models.plot import Plot


class Pasture(models.Model):

    plot = models.ForeignKey(Plot, on_delete=CASCADE)
    stockRate = models.FloatField()
    livestock = models.ForeignKey(Animal, on_delete=CASCADE)
