from django.db import models
from django.db.models import CASCADE

from aria.models.plot import Plot


class Garden(models.Model):
    class Meta:
        db_table = "garden"
        app_label = "aria"

    plot = models.ForeignKey(Plot, on_delete=CASCADE)

