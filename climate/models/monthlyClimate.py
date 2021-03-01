from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CASCADE

from climate.models.climate import Climate

MONTHS = (
    (1, 'January'),
    (2, 'February'),
    (3, 'March'),
    (4, 'April'),
    (5, 'May'),
    (6, 'June'),
    (7, 'July'),
    (8, 'August'),
    (9, 'September'),
    (10, 'October'),
    (11, 'November'),
    (12, 'December')
)


class MonthlyClimate(models.Model):

    class Meta:
        db_table = "monthlyclimate"
        app_label = "climate"

    climate = models.ForeignKey(Climate, on_delete=CASCADE)
    month = models.IntegerField(choices=MONTHS)
    dailyLow = models.IntegerField(validators=[MinValueValidator(-100), MaxValueValidator(100)])
    dailyHigh = models.IntegerField(validators=[MinValueValidator(-100), MaxValueValidator(100)])
    rain = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])