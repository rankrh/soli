from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from crop.models.crop import Crop
from crop.models.validation.plantValidation import GROW_STYLE, ROW


class Planting(models.Model):

    class Meta:
        db_table = "planting"
        app_label = "crop"

    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)

    pattern = models.CharField(
        choices=GROW_STYLE,
        default=ROW,
        max_length=1,
        blank=True,
        null=True
    )

    rowSpacingMin = models.SmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0)
        ]
    )

    rowSpacingMax = models.SmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0)
        ]
    )

    interRowSpacingMin = models.SmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0)
        ]
    )

    interRowSpacingMax = models.SmallIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0)
        ]
    )

    soilTemperatureMin = models.SmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(-50),
            MaxValueValidator(100)
        ]
    )

    soilTemperatureMax = models.SmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(-50),
            MaxValueValidator(100)
        ]
    )

    germinationStart = models.SmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(365)
        ]
    )

    germinationEnd = models.SmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(365)
        ]
    )

    depth = models.FloatField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000)
        ]
    )
