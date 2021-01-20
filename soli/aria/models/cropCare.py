from django.core.validators import MinValueValidator
from django.db import models

from aria.models.crop import Crop
from aria.models.planting import Planting
from aria.models.validation.careValidation import SUN


class CropCare(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    plant = models.ForeignKey(Planting, on_delete=models.CASCADE)
    sun = models.CharField(
        choices=SUN,
        max_length=1,
        default=None
    )

    soil = models.CharField(
        null=True,
        blank=True,
        max_length=30
    )

    water = models.SmallIntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )