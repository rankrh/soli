from django.db import models

from . import Shape, Plot
from .shape import POLYGON


class Plot(models.Model):
    class Meta:
        db_table = "garden"
        app_label = "aria"

    plot = models.ForeignKey(Plot)