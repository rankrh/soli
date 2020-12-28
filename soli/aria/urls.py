from django.urls import path
from .views import *
from .views.create.farm import createFarm
from .views.create.plot import addPlotDetails
from .views.planning.calendar import createCalendar

urlpatterns = [
	path("", index, name="index"),

	# Create
	path("create/farm", createFarm, name="createFarm"),
	path("create/crop", createCrop, name="createCrop"),
	path("create/species", createSpecies, name="createSpecies"),
	path("create/ajax/genus", createGenus, name="createGenus"),
	path("create/plot", createPlot, name="createPlot"),
	path("create/plot/ajax/details", createPlotAjax, name="createPLot"),
	path("create/plot/details", addPlotDetails, name="addPlotDetails"),
	path("create/ajax/plot", createPlotAjax, name="createPlotAjax"),
	path("create/ajax/delete-plots", deletePlotsAjax, name="deletePlotAjax"),
	path("create/plot/ajax/delete-plots", deletePlotsAjax, name="deletePlotAjax"),

	# Display
	path("display/crops", displayCrops, name="displayCrops"),

	#Planning
	path("calendar", createCalendar, name="createCalendar"),
]
