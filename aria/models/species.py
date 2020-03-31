from django.db import models
from .genus import Genus


class Species(models.Model):
    species = models.CharField(max_length=30)
    common_name = models.CharField(max_length=30, null=True)
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE)

    class Meta:
        db_table = "species"
        app_label = "aria"
        unique_together = (
            "species", "genus"
        )

    def __str__(self):
        genus = str(self.genus.genus)
        return f"{genus.title()} {self.species}"
