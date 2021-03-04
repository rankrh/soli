from django.urls import path

from farm.views.plot import addPlotDetails, createPlot, createPlotAjax, deletePlotsAjax

urlpatterns = [
    path("create/plot", createPlot, name="createPlot"),
    path("create/plot/ajax/details", createPlotAjax, name="createPlot"),
    path("create/plot/details", addPlotDetails, name="addPlotDetails"),
    path("create/ajax/plot", createPlotAjax, name="createPlotAjax"),
    path("create/ajax/delete-plots", deletePlotsAjax, name="deletePlotAjax"),
    path("create/plot/ajax/delete-plots", deletePlotsAjax, name="deletePlotAjax"),
]
