from django.db import models
from django.db.models import CASCADE

from plot.models.plot import Plot


class Silvopasture(models.Model):
    class Meta:
        db_table = "silvopasture"
        app_label = "plot"

    plot = models.ForeignKey(Plot, on_delete=CASCADE)

