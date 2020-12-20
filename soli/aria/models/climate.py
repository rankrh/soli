from django.db import models


class Climate(models.Model):

    name = models.CharField(max_length=128)
    zone = models.CharField(max_length=2)
    firstFrost = models.DateField()
    lastFrost = models.DateField()
