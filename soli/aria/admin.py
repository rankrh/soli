from django.contrib import admin

from .models.climate import Climate
from .models.crop import Crop
from .models.farm import Farm
from .models.genus import Genus
from .models.growplan import GrowPlan
from .models.harvestplan import HarvestPlan
from .models.livestock import Livestock
from .models.plantingplan import PlantingPlan
from .models.plot import Plot
from .models.point import Point
from .models.shape import Shape
from .models.species import Species
from .models.subspecies import Subspecies
from .models.orchard import Orchard
from .models.field import Field
from .models.forest import Forest
from .models.pasture import Pasture
from .models.silvopasture import Silvopasture
from .models.garden import Garden

admin.site.register(Shape)
admin.site.register(Plot)
admin.site.register(Crop)
admin.site.register(Genus)
admin.site.register(PlantingPlan)
admin.site.register(GrowPlan)
admin.site.register(HarvestPlan)
admin.site.register(Species)
admin.site.register(Subspecies)
admin.site.register(Point)
admin.site.register(Garden)
admin.site.register(Livestock)
admin.site.register(Pasture)
admin.site.register(Orchard)
admin.site.register(Field)
admin.site.register(Silvopasture)
admin.site.register(Forest)
admin.site.register(Climate)
admin.site.register(Farm)
