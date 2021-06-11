from django.urls import path

from crop.views.cropDetails import CropDetails
from crop.views.cropCreator import CropCreator
from taxonomy.views.genus import Genus
from taxonomy.views.species import Species
from crop.views.cropForm import CropForm

urlpatterns = [
    path("add", CropForm.as_view(), name="addCrops"),
    path("", CropDetails.as_view(), name="listCrops"),
    path("create", CropCreator.as_view(), name="addCrop"),
    path("species/create", Species.as_view(), name="addSpecies"),
    path("genus/create", Genus.as_view(), name="addGenus"),
]
