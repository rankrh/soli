from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from crop.models.crop import Crop


class CropCare(models.Model):

    class Meta:
        db_table = "cropcare"
        app_label = "crop"

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
