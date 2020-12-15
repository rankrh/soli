from django.db import models
from django.db.models import CASCADE

from aria.models.species import Species


class Livestock(models.Model):
    class Meta:
        db_table = "livestock"
        app_label = "aria"

    species = models.ForeignKey(Species, on_delete=CASCADE)

