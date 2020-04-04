from aria.models.validation.plant import *
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Plant(models.Model):

    germination = models.SmallIntegerField(
        null=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(365)
        ]
    )

    depth = models.SmallIntegerField(
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(1000)
        ]
    )

    pattern = models.CharField(
        null=True,
        choices=GROW_STYLE,
        max_length=1

    )

    spacing = models.SmallIntegerField(
        null=True,
        validators=[
            MinValueValidator(0)
        ]
    )

    temperature = models.SmallIntegerField(
        null=True,
        validators=[
            MinValueValidator(-50),
            MaxValueValidator(50)
        ]
    )

    frost = models.CharField(
        null=True,
        choices=FROST,
        max_length = 1
    )

    date = models.SmallIntegerField(
        null=True,
        validators=[
            MinValueValidator(-180),
            MaxValueValidator(180)
        ]
    )

    location = models.CharField(
        null=True,
        choices=LOCATION,
        max_length=1
    )

    transplant = models.ForeignKey(
        "self",
        on_delete=models.CASCADE)
