from aria.models.validation.grow import SUN
from django.db import models
from aria.models import Crop, Plant


class Grow(models.Model):
    class Meta:
        db_table = "grow"
        app_label = "aria"

    gr_num = models.AutoField(primary_key=True)
    gr_cr_num = models.ForeignKey(Crop, db_column="gr_cr_num", on_delete=models.CASCADE)
    gr_pl_num = models.ForeignKey(Plant, db_column="gr_pl_num", on_delete=models.CASCADE)
    gr_sun = models.CharField(
        null=True,
        choices=SUN,
        max_length=1,
        blank=False,
        default=None
    )

    gr_soil = models.CharField(
        null=True,
        max_length=30
    )