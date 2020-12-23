from aria.models.crop import Crop
from aria.models.plantingplan import PlantingPlan
from aria.models.validation.growValidation import SUN
from django.db import models


class GrowPlan(models.Model):
    class Meta:
        db_table = "growPlan"
        app_label = "aria"

    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    plant = models.ForeignKey(PlantingPlan, on_delete=models.CASCADE)
    sun = models.CharField(
        null=True,
        blank=True,
        choices=SUN,
        max_length=1,
        default=None
    )

    soil = models.CharField(
        null=True,
        blank=True,
        max_length=30
    )