from django.urls import path
from .views import *
from .views.create.farmCreator import createFarm
from .views.create.plotCreator import PlotCreator
from .views.planning.calendar import createCalendar

urlpatterns = [
	path("", index, name="index"),

	# Create
	path("create/farm", createFarm, name="createFarm"),
	path("create/crop", createCrop, name="createCrop"),
	path("create/species", createSpecies, name="createSpecies"),
	path("create/ajax/genus", createGenus, name="createGenus"),
	path("create/plot", PlotCreator.as_view(), name="createPlot"),
	path("create/plot/ajax/details", createPlotAjax, name="createPlot"),
	path("create/plot/details", PlotCreator.as_view(), name="addPlotDetails"),
	path("create/ajax/plot", createPlotAjax, name="createPlotAjax"),
	path("create/ajax/delete-plots", deletePlotsAjax, name="deletePlotAjax"),
	path("create/plot/ajax/delete-plots", deletePlotsAjax, name="deletePlotAjax"),

	# Display
	path("display/crops", displayCrops, name="displayCrops"),

	#Planning
	path("calendar", createCalendar, name="createCalendar"),
]
