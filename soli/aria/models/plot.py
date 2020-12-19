from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

from aria.models.validation.plotTypes import TYPES, FOREST
from .shape import POLYGON, Shape


class Plot(models.Model):
    class Meta:
        db_table = "plot"
        app_label = "aria"

    name = models.CharField(max_length=128, blank=True, default="Unnamed Plot")
    owner = models.ForeignKey(User, on_delete=CASCADE)
    shape = models.ForeignKey(Shape, null=True, default=None, on_delete=CASCADE)
    description = models.CharField(max_length=1024, blank=True, default="")
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=CASCADE)
    type = models.CharField(
        choices=TYPES,
        max_length=1,
        blank=True,
        null=True,
        default=None
    )

    def save(self):

        if self.shape is None:
            self.shape = Shape(type=POLYGON)
            self.shape.save()

        super(Plot, self).save()

    def __str__(self):
        return self.name
