from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from .species import Species


class Crop(models.Model):
    class Meta:
        db_table = "crop"
        app_label = "aria"
        unique_together = ["cr_num", "cr_sp_num"]

    cr_num = models.AutoField(primary_key=True)
    cr_variety = models.CharField(max_length=50)
    cr_sp_num = models.ForeignKey(Species, db_column="cr_sp_num", null=True, on_delete=models.CASCADE)
    cr_description = models.TextField(null=True)
    cr_company = models.CharField(null=True, max_length=30)
    cr_organic = models.BooleanField(null=True)
    cr_treated = models.BooleanField(null=True)
    cr_hybrid = models.BooleanField(null=True)

    def __str__(self):
        return self.cr_variety
