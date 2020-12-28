from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

from aria.models.climate import Climate
from aria.models.point import Point


class Farm(models.Model):

    owner = models.OneToOneField(User, on_delete=CASCADE)
    location = models.ForeignKey(Point, null=True, blank=True, on_delete=CASCADE)
    name = models.CharField(max_length=128)
    logo = models.ImageField(null=True, blank=True)
    climate = models.ForeignKey(Climate, null=True, blank=True, on_delete=CASCADE)
