from django.db import models
from django.db.models import CASCADE

from aria.models.crop import Crop


class Event(models.Model):

    date = models.DateField()
    crop = models.ForeignKey(Crop, on_delete=CASCADE)