from django.core.validators import MinValueValidator
from django.db import models


class Harvest(models.Model):
    harvest = models.AutoField(primary_key=True)

    begin = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(0),
        ]
    )

    end = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(0),
        ]
    )

