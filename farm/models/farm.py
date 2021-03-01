from datetime import date, datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

from climate.models.climate import Climate
from geometry.models.point import Point

YEAR_CHOICES = [(year, year) for year in range(1900, date.today().year + 1)]


class Farm(models.Model):

    class Meta:
        db_table = "farm"
        app_label = "farm"

    owner = models.ForeignKey(User, on_delete=CASCADE)
    location = models.ForeignKey(Point, on_delete=CASCADE)
    description = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=128)
    logo = models.ImageField(null=True, blank=True)
    climate = models.ForeignKey(Climate, on_delete=CASCADE)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year)

    def __str__(self):

        established = f"(est. {self.year})" if self.year is not None else ""
        return f"{self.name} {established}"