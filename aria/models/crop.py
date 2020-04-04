from django.db import models
from .species import Species
from .plant import Plant
from .grow import Grow
from .harvest import Harvest


class Crop(models.Model):
    crop = models.AutoField(primary_key=True)
    variety = models.CharField(max_length=50)
    species = models.ForeignKey(Species, null=True, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, null=True, on_delete=models.CASCADE)
    grow = models.ForeignKey(Grow, null=True, on_delete=models.CASCADE)
    harvest = models.ForeignKey(Harvest, null=True, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    company = models.CharField(null=True, max_length=30)
    organic = models.BooleanField(null=True)
    treated = models.BooleanField(null=True)
    hybrid = models.BooleanField(null=True)

    class Meta:
        db_table = "crop"
        app_label = "aria"
        unique_together = (
            "crop", "species"
        )

    def __str__(self):
        return self.variety
