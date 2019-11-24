from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from aria.validation import cropchoices


class Crop(models.Model):
    crop = models.AutoField(primary_key=True)
    name = models.CharField(max_length=309)
    species = models.CharField(max_length=30)
    genus = models.CharField(max_length=30)
    height = models.SmallIntegerField(
        null=True,
        validators=[MinValueValidator(1, "All crops must have a height greater than zero centimeters")]
    )
    weight = models.SmallIntegerField(
        null=True,
        validators=[MinValueValidator(1, "All crops must have a weight greater than zero centimeters")]
    )
    yieldKg = models.SmallIntegerField(
        validators=[MinValueValidator(1, "All crops must have a yield of more than one kg")],
        db_column="yield"
    )
    gallonsPerWeek = models.FloatField()
    sunPerDay = models.CharField(choices=cropchoices.SUN, null=True, max_length=1)
    category = models.CharField(choices=cropchoices.CROP_TYPE, null=True, max_length=2)
    daysToHarvest = models.SmallIntegerField(validators=[MaxValueValidator(365)])

    class Meta:
        db_table = "crop"


class GrowingStyle(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    growingStyle = models.CharField(choices=cropchoices.GROWING_STYLES, max_length=1)

    class Meta:
        db_table = "growingStyle"


class CropType(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    cropType = models.CharField(choices=cropchoices.CROP_TYPE, max_length=1)

    class Meta:
        db_table = "cropType"


class Plot(models.Model):
    plotId = models.AutoField(primary_key=True)
    garden = models.ForeignKey('self', on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, null=True, on_delete=models.SET_NULL)
    area = models.FloatField()

    class Meta:
        db_table = "plot"


class CropPosition(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    X = models.FloatField()
    Y = models.FloatField()

    class Meta:
        db_table = "cropPosition"


class PlotCoordinate(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    X = models.FloatField()
    Y = models.FloatField()

    class Meta:
        db_table = "plotCoordinate"
