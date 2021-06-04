from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from crop.models.crop import Crop


class Planting(models.Model):
    class Meta:
        db_table = "planting"
        app_label = "crop"

    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    soilTemperatureMin = models.SmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(-50), MaxValueValidator(100)],
    )

    soilTemperatureMax = models.SmallIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(-50), MaxValueValidator(100)],
    )

    germinationStart = models.SmallIntegerField(
        null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(365)]
    )

    germinationEnd = models.SmallIntegerField(
        null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(365)]
    )

    depth = models.FloatField(
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(1000)],
    )
