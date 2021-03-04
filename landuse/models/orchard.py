from django.db import models
from django.db.models import CASCADE

from farm.models.plot import Plot


class Orchard(models.Model):

    class Meta:
        db_table = "orchard"
        app_label = "landuse"

    plot = models.ForeignKey(Plot, on_delete=CASCADE)


