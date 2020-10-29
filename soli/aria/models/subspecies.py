from django.db import models
from .species import Species


class Subspecies(models.Model):

    sub_num = models.AutoField(primary_key=True)
    sub_sp_num = models.ForeignKey(Species, on_delete=models.CASCADE, db_column="sub_sp_num")
    sub_name = models.CharField(max_length=30)

    class Meta:
        db_table = "subspecies"
        app_label = "aria"
        unique_together = (
            "sub_num", "sub_sp_num"
        )
