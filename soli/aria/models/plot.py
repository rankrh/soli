from django.db import models
from .crop import Crop


class Plot(models.Model):
    class Meta:
        db_table = "plot"
        app_label = "aria"

    plt_num = models.AutoField(primary_key=True)
    plt_name = models.CharField(max_length=128, blank=True, default="Unnamed Plot")
    plt_description = models.CharField(max_length=1024, blank=True, default="")
    plt_area = models.FloatField(blank=True, null=True)
    plt_parent_num = models.ForeignKey(
        'self', blank=True, null=True, on_delete=models.CASCADE, db_column="plt_parent_num"
    )
    plt_cr_num = models.ForeignKey(Crop, blank=True, null=True, on_delete=models.SET_NULL, db_column="plt_cr_num")
