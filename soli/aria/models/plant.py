from aria.models import Crop
from aria.models.validation.plant import *
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Plant(models.Model):
    class Meta:
        db_table = "plant"
        app_label = "aria"

    pl_num = models.AutoField(primary_key=True)
    pl_cr_num = models.ForeignKey(Crop, db_column="pl_cr_num", on_delete=models.CASCADE)

    pl_pattern = models.CharField(
        choices=GROW_STYLE,
        max_length=1,
        blank=False,
        default=None
    )

    pl_spacing = models.SmallIntegerField(
        validators=[
            MinValueValidator(0)
        ]
    )

    pl_frost = models.CharField(
        choices=FROST,
        max_length=1,
        blank=False,
        default=None
    )

    pl_date = models.SmallIntegerField(
        default=1,
        validators=[
            MinValueValidator(-180),
            MaxValueValidator(180)
        ]
    )

    pl_location = models.CharField(
        choices=LOCATION,
        max_length=1,
        blank=False,
        default=None
    )

    pl_transplant = models.ForeignKey(
        "self",
        null=True,
        db_column="pl_transplant",
        on_delete=models.CASCADE)

    pl_temperature = models.SmallIntegerField(
        null=True,
        validators=[
            MinValueValidator(-50),
            MaxValueValidator(50)
        ]
    )

    pl_germination = models.SmallIntegerField(
        null=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(365)
        ]
    )

    pl_depth = models.SmallIntegerField(
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000)
        ]
    )
