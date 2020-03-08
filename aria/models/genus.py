from django.db import models


class Genus(models.Model):
    genus = models.CharField(max_length=30)

    class Meta:
        db_table = "genus"
        app_label = "aria"

    def __str__(self):
        return f"{self.genus.title()}"
