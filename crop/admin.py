from django.contrib import admin

from crop.models.crop import Crop
from crop.models.cropCare import CropCare
from crop.models.harvest import Harvest
from crop.models.planting import Planting
from crop.models.plantingDate import PlantingDate

admin.site.register(Crop)
admin.site.register(Planting)
admin.site.register(CropCare)
admin.site.register(Harvest)
admin.site.register(PlantingDate)