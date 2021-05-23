from django.db import models

from taxonomy.models.species import Species


class Crop(models.Model):
    class Meta:
        db_table = "crop"
        app_label = "crop"
        unique_together = ["id", "species"]

    name = models.CharField(max_length=50)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    organic = models.BooleanField(blank=True, null=True)
    treated = models.BooleanField(blank=True, null=True)
    hybrid = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.species.common_name}"
