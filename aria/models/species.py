from django.db import models
from .genus import Genus


class Species(models.Model):
    species = models.CharField(max_length=30)
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE)

    class Meta:
        db_table = "species"
        app_label = "aria"
