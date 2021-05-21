from django.db import models

KINGDOMS = (("P", "plantae"), ("A", "Animalae"), ("F", "Fungus"))


class Genus(models.Model):
    class Meta:
        db_table = "genus"
        app_label = "taxonomy"

    name = models.CharField(max_length=30, unique=True)
    kingdom = models.CharField(choices=KINGDOMS, max_length=1)

    def __str__(self):
        return f"{self.name.title()}"
