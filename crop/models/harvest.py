from django.core.validators import MinValueValidator
from django.db import models

from crop.models.crop import Crop
from crop.models.validation.harvestValidation import CROP_TYPE, FRUIT


class Harvest(models.Model):
    class Meta:
        db_table = "harvest"
        app_label = "crop"

    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    begin = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
        ],
        default=None,
    )

    end = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(0),
        ],
        default=None,
    )

    variety = models.CharField(
        null=True, blank=True, choices=CROP_TYPE, max_length=1, default=FRUIT
    )
