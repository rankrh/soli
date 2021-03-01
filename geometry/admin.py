from django.contrib import admin

from geometry.models.point import Point
from geometry.models.shape import Shape

admin.site.register(Point)
admin.site.register(Shape)
