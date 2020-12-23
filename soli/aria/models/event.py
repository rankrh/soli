from django.db import models
from django.db.models import CASCADE

from aria.models.crop import Crop


class Event(models.Model):

    startDate = models.DateField()
    endDate = models.DateField()
    details = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
