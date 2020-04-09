from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .species import Species


class Crop(models.Model):
    class Meta:
        db_table = "crop"
        app_label = "aria"
        unique_together = ["id", "species"]

    variety = models.CharField(max_length=50)
    species = models.ForeignKey(Species, null=True, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    company = models.CharField(null=True, max_length=30)
    organic = models.BooleanField(null=True)
    treated = models.BooleanField(null=True)
    hybrid = models.BooleanField(null=True)
    temperature = models.SmallIntegerField(
        null=True,
        validators=[
            MinValueValidator(-50),
            MaxValueValidator(50)
        ]
    )
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

    def __str__(self):
        return self.variety
