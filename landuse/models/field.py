from django.db import models
from django.db.models import CASCADE

from plot.models.plot import Plot


class Field(models.Model):

    class Meta:
        db_table = "field"
        app_label = "landuse"

    plot = models.ForeignKey(Plot, on_delete=CASCADE)
