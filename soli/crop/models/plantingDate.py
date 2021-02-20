from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from crop.models.crop import Crop
from crop.models.validation.plantValidation import FROST, LOCATION, INSIDE, LAST_FROST


class PlantingDate(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)

    frost = models.CharField(
        choices=FROST,
        max_length=1,
        blank=False,
        null=True,
        default=LAST_FROST
    )

    date = models.SmallIntegerField(
        default=1,
        blank=True,
        null=True,
        validators=[
            MinValueValidator(-180),
            MaxValueValidator(180)
        ]
    )

    location = models.CharField(
        choices=LOCATION,
        max_length=1,
        blank=False,
        null=True,
        default=INSIDE
    )

    transplant = models.SmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(52)
        ]
    )
