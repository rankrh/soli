from aria.models.crop import Crop
from aria.models.planting import Planting
from aria.models.validation.growValidation import SUN
from django.db import models


class Grow(models.Model):
    class Meta:
        db_table = "grow"
        app_label = "aria"

    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    plant = models.ForeignKey(Planting, on_delete=models.CASCADE)
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