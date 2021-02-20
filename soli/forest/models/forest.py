from django.db import models
from django.db.models import CASCADE

from plot.models.plot import Plot


class Forest(models.Model):
    plot = models.ForeignKey(Plot, on_delete=CASCADE)
