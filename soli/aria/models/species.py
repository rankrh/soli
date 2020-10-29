from django.db import models
from .genus import Genus


class Species(models.Model):

    sp_num = models.AutoField(primary_key=True)
    sp_name = models.CharField(max_length=30)
    sp_common_name = models.CharField(max_length=30, null=True)
    sp_ge_num = models.ForeignKey(Genus, on_delete=models.CASCADE, db_column="sp_ge_num", )

    class Meta:
        db_table = "species"
        app_label = "aria"
        unique_together = (
            "sp_num", "sp_ge_num"
        )

    def __str__(self):
        genus = str(self.sp_ge_num.ge_name)
        latinName = f"{genus.title()} {self.sp_name}"

        if self.sp_common_name:
            fullName = f"{self.sp_common_name} ({latinName})"
        else:
            fullName = latinName
        return fullName
