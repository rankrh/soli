from django.db import models


class Genus(models.Model):
    class Meta:
        db_table = "genus"
        app_label = "taxonomy"

    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.name.title()}"
