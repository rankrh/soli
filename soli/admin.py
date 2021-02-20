from django.contrib import admin

from farm.models.climate import Climate
from crop.models.crop import Crop
from farm.models.farm import Farm
from taxonomy.models.genus import Genus
from crop.models.cropCare import CropCare
from crop.models.harvest import Harvest
from crop.models.planting import Planting
from animal.models.animal import Animal
from plot.models.plot import Plot
from geometry.models.point import Point
from geometry.models.shape import Shape
from taxonomy.models.species import Species
from taxonomy.models.subspecies import Subspecies
from orchard.models.orchard import Orchard
from field.models.field import Field
from forest.models.forest import Forest
from pasture.models.pasture import Pasture
from silvopasture.models.silvopasture import Silvopasture
from garden.models.garden import Garden
from crop.models.plantingDate import PlantingDate

admin.site.register(Shape)
admin.site.register(Plot)
admin.site.register(Crop)
admin.site.register(Genus)
admin.site.register(Planting)
admin.site.register(CropCare)
admin.site.register(Harvest)
admin.site.register(Species)
admin.site.register(Subspecies)
admin.site.register(Point)
admin.site.register(Garden)
admin.site.register(Animal)
admin.site.register(Pasture)
admin.site.register(Orchard)
admin.site.register(Field)
admin.site.register(Silvopasture)
admin.site.register(Forest)
admin.site.register(Climate)
admin.site.register(Farm)
admin.site.register(PlantingDate)