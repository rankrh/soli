from django.db import models
from .genus import Genus


class Species(models.Model):

    class Meta:
        db_table = "species"
        app_label = "taxonomy"
        unique_together = (
            "id", "genus"
        )

    name = models.CharField(max_length=30)
    common_name = models.CharField(max_length=30, null=True)
    genus = models.ForeignKey(Genus, on_delete=models.CASCADE)

    def __str__(self):
        genus = str(self.genus.name)
        latinName = f"{genus.title()} {self.name}"

        if self.common_name:
            fullName = f"{self.common_name} ({latinName})"
        else:
            fullName = latinName

        return fullName
