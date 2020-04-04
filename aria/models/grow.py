from aria.models.validation.grow import SUN
from django.db import models


class Grow(models.Model):
    grow = models.AutoField(primary_key=True)

    sun = models.CharField(
        null=True,
        choices=SUN,
        max_length = 1
    )

    soil = models.CharField(
        null=True,
        max_length = 30
    )