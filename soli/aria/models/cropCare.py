from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from aria.models.crop import Crop
from aria.models.planting import Planting
from aria.models.validation.careValidation import SUN


class CropCare(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    sunMin = models.SmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(24)
        ]
    )

    sunMax = models.SmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(24)
        ]
    )

    soil = models.CharField(
        null=True,
        blank=True,
        max_length=30
    )

    water = models.SmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0)
        ]
    )

    frostHardy = models.BooleanField(
        null=True,
        blank=True
    )