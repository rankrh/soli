from django.db import models
from django.db.models import CASCADE

from plot.models.plot import Plot


class Garden(models.Model):

    class Meta:
        db_table = "landuse"
        app_label = "garden"

    plot = models.ForeignKey(Plot, on_delete=CASCADE)
