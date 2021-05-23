from datetime import datetime

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

from crop.models.crop import Crop


class Seedbank(models.Model):
    class Meta:
        db_table = "seedbank"
        app_label = "seedbank"
        unique_together = ["user", "crop", "year"]

    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    year = models.IntegerField(default=datetime.now().year)

    def __str__(self):
        return f"{self.crop.__str__()} ({self.year})"
