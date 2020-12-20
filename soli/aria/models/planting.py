from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from aria.models.crop import Crop
from aria.models.validation.plantValidation import GROW_STYLE, FROST, LOCATION


class Planting(models.Model):
    class Meta:
        db_table = "plant"
        app_label = "aria"

    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)

    pattern = models.CharField(
        choices=GROW_STYLE,
        max_length=1,
        blank=False,
        default=None
    )

    spacing = models.SmallIntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

    frost = models.CharField(
        choices=FROST,
        max_length=1,
        blank=False,
        default=None
    )

    date = models.SmallIntegerField(
        default=1,
        validators=[
            MinValueValidator(-180),
            MaxValueValidator(180)
        ]
    )

    location = models.CharField(
        choices=LOCATION,
        max_length=1,
        blank=False,
        default=None
    )

    transplant = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        db_column="pl_transplant",
        on_delete=models.CASCADE)

    temperature = models.SmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(-50),
            MaxValueValidator(50)
        ]
    )

    germination = models.SmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(365)
        ]
    )

    depth = models.SmallIntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000)
        ]
    )
