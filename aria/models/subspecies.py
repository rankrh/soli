from django.db import models
from .species import Species


class Subspecies(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    subspecies = models.CharField(max_length=30)

    class Meta:
        db_table = "subspecies"
        app_label = "aria"
        unique_together = (
            "subspecies", "species"
        )
