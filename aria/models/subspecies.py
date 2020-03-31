from django.db import models
from .species import Species


class Subspecies(models.Model):
    subspecies = models.CharField(max_length=30)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    class Meta:
        db_table = "subspecies"
        app_label = "aria"
        unique_together = (
            "subspecies", "species"
        )
