from django.db import models

MARKER = "M"
LINE = "L"
POLYGON = "P"

shapes = [
    (MARKER, "Marker"),
    (LINE, "Line"),
    (POLYGON, "Polygon")
]


class Shape(models.Model):

    class Meta:
        db_table = "shape"
        app_label = "geometry"

    type = models.CharField(
        null=True,
        choices=shapes,
        max_length=1,
        blank=False,
        default=None
    )

    area = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
