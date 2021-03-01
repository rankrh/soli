from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

SUB_ZONES = (("a", "a"), ("b", "b"))
DEGREES_F = "°F"


class HardinessZone(models.Model):
    class Meta:
        db_table = "hardinesszone"
        app_label = "climate"

    zone = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(13)])
    subZone = models.CharField(choices=SUB_ZONES, max_length=1)
    lowRange = models.IntegerField(validators=[MinValueValidator(-65), MaxValueValidator(65)], null=True)
    highRange = models.IntegerField(validators=[MinValueValidator(-65), MaxValueValidator(65)], null=True)

    def __str__(self):

        if self.lowRange is not None and self.highRange is not None:
            tempRange = f"{self.lowRange}{DEGREES_F} to {self.highRange}{DEGREES_F}"
        elif self.lowRange is None:
            tempRange = f"<{self.highRange}{DEGREES_F}"
        else:
            tempRange = f">{self.lowRange}{DEGREES_F}"

        return f"{self.zone}{self.subZone} ({tempRange})"
