from django.db import models
from ..validation import cropchoices
from .crop import Crop


class GrowingStyle(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    growingStyle = models.CharField(choices=cropchoices.GROWING_STYLES, max_length=1)

    class Meta:
        db_table = "growingStyle"
        app_label = "aria"
