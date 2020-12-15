from django.db import models

from aria.models.plotTypes.validation.plotTypes import TYPES


class PlotType(models.Model):

    type = models.CharField(
        choices=TYPES,
        max_length=1,
        blank=False,
        default=None
    )
