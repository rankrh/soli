from django.db import models
from django.db.models import CASCADE

from taxonomy.models.species import Species


class Animal(models.Model):
    species = models.ForeignKey(Species, on_delete=CASCADE)
