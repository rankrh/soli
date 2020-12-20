from django.db import models
from .species import Species


class Crop(models.Model):
    class Meta:
        db_table = "crop"
        app_label = "aria"
        unique_together = ["id", "species"]

    name = models.CharField(max_length=50)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    company = models.CharField(null=True, max_length=30)
    organic = models.BooleanField(null=True)
    treated = models.BooleanField(null=True)
    hybrid = models.BooleanField(null=True)

    def __str__(self):
        return self.name
