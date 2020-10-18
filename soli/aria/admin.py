from django.contrib import admin
from .models import Crop, Genus, Species, Subspecies

admin.site.register(Crop)
admin.site.register(Species)
admin.site.register(Genus)
admin.site.register(Subspecies)