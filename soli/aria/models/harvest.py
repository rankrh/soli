from aria.models.crop import Crop
from aria.models.cropCare import CropCare
from aria.models.planting import Planting
from aria.models.validation.harvestValidation import CROP_TYPE
from django.core.validators import MinValueValidator
from django.db import models


class Harvest(models.Model):
    class Meta:
        db_table = "harvest"
        app_label = "aria"

    crop = models.ForeignKey(Crop,on_delete=models.CASCADE)
    begin = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(0),
        ],
        blank=False,
        default=None
    )

    end = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(0),
        ],
        blank=False,
        default=None
    )

    variety = models.CharField(
        null=True,
        choices=CROP_TYPE,
        max_length=1,
        blank=False,
        default=None
    )
