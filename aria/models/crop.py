from django.db import models
from ..validation import cropchoices
from django.core.validators import MinValueValidator, MaxValueValidator
from .species import Species


class Crop(models.Model):
    crop = models.AutoField(primary_key=True)
    variety = models.CharField(max_length=50)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
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
    sunPerDay = models.CharField(choices=cropchoices.SUN, null=True, max_length=1, default=None)
    category = models.CharField(choices=cropchoices.CROP_TYPE, null=True, max_length=2, default=None)
    daysToHarvest = models.SmallIntegerField(validators=[MaxValueValidator(365)])

    class Meta:
        db_table = "crop"
        app_label = "aria"
        unique_together = (
            "crop", "species"
        )

    def __str__(self):
        return self.variety