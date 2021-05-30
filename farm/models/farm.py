from datetime import date, datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE
from django.utils.text import slugify

from climate.models.climate import Climate
from geometry.models.point import Point

YEAR_CHOICES = [(year, year) for year in range(1900, date.today().year + 1)]


class Farm(models.Model):
    class Meta:
        db_table = "farm"
        app_label = "farm"
        unique_together = ["owner", "name"]

    owner = models.ForeignKey(User, on_delete=CASCADE)
    location = models.ForeignKey(Point, on_delete=CASCADE, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=128, default=f"My Farm")
    logo = models.ImageField(null=True, blank=True, upload_to="logos")
    climate = models.ForeignKey(Climate, on_delete=CASCADE, blank=True, null=True)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.now().year)
    slug = models.SlugField(unique=False)
    phone = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    address2 = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):

        established = f"(est. {self.year})" if self.year is not None else ""
        return f"{self.name} {established}"
