from aria.models.validation.grow import SUN
from django.db import models
from aria.models import Crop, Plant


class Grow(models.Model):
    class Meta:
        db_table = "grow"
        app_label = "aria"

    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    sun = models.CharField(
        null=True,
        choices=SUN,
        max_length=1,
        blank=False,
        default=None
    )

    soil = models.CharField(
        null=True,
        max_length=30
    )