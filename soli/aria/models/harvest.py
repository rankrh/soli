from aria.models.validation.harvest import CROP_TYPE
from django.core.validators import MinValueValidator
from django.db import models
from aria.models import Crop, Plant, Grow


class Harvest(models.Model):
    class Meta:
        db_table = "harvest"
        app_label = "aria"

    har_num = models.AutoField(primary_key=True)
    har_cr_num = models.ForeignKey(Crop, db_column="har_cr_num", on_delete=models.CASCADE)
    har_pl_num = models.ForeignKey(Plant, db_column="har_pl_num", on_delete=models.CASCADE)
    har_gr_num = models.ForeignKey(Grow, db_column="har_gr_num", on_delete=models.CASCADE)
    har_begin = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(0),
        ],
        blank=False,
        default=None
    )

    har_end = models.IntegerField(
        null=True,
        validators=[
            MinValueValidator(0),
        ],
        blank=False,
        default=None
    )

    har_variety = models.CharField(
        null=True,
        choices=CROP_TYPE,
        max_length=1,
        blank=False,
        default=None
    )
