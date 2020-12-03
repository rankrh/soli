from django.db import models
from .crop import Crop


class Polygon(models.Model):
    class Meta:
        db_table = "polygon"
        app_label = "aria"

    poly_num = models.AutoField(primary_key=True)
    poly_plt_num - models.Autofiel
    plt_cr_num = models.ForeignKey(Crop, null=True, on_delete=models.SET_NULL, db_column="plt_cr_num")
