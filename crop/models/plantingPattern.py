from django.core.validators import MinValueValidator
from django.db import models

from crop.models.planting import Planting
from crop.models.validation.plantValidation import GROW_STYLE, ROW


class PlantingPattern(models.Model):
    class Meta:
        db_table = "plantingpattern"
        app_label = "crop"

    planting = models.ForeignKey(Planting)
    pattern = models.CharField(
        choices=GROW_STYLE, default=ROW, max_length=1, null=True, blank=True
    )
    rowSpacingMin = models.SmallIntegerField(
        null=True, blank=True, validators=[MinValueValidator(0)]
    )
    rowSpacingMax = models.SmallIntegerField(
        null=True, blank=True, validators=[MinValueValidator(0)]
    )

    interRowSpacingMin = models.SmallIntegerField(
        null=True, blank=True, validators=[MinValueValidator(0)]
    )

    interRowSpacingMax = models.SmallIntegerField(
        null=True, blank=True, validators=[MinValueValidator(0)]
    )
