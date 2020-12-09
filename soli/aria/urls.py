from django.urls import path
from .views import *

urlpatterns = [
	path("", index, name="index"),


	# Create
	path("create/crop", createCrop, name="createCrop"),
	path("create/species", createSpecies, name="createSpecies"),
	path("create/ajax/genus", createGenus, name="createGenus"),
	path("create/plot", createPlot, name="createPlot"),
	path("create/ajax/plot", createPlotAjax, name="createPlotAjax"),
	path("create/ajax/delete-plots", deletePlotsAjax, name="deletePlotAjax"),
	
	# Display
	path("display/crops", displayCrops, name="displayCrops"),
]
