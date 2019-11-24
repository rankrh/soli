from django.db import models
from ..validation import cropchoices
from .crop import Crop


class CropType(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    cropType = models.CharField(choices=cropchoices.CROP_TYPE, max_length=2)

    class Meta:
        db_table = "cropType"
        app_label = "aria"
