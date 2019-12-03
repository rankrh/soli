from django.contrib import admin
from .models import Crop, Genus, Species

admin.site.register(Crop)
admin.site.register(Species)
admin.site.register(Genus)