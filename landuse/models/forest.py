from django.db import models
from django.db.models import CASCADE

from plot.models.plot import Plot


class Forest(models.Model):

    class Meta:
        db_table = "forest"
        app_label = "landuse"

    plot = models.ForeignKey(Plot, on_delete=CASCADE)
