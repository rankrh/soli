from django.urls import path

from .views import *
from .views.create.plotCreator import addPlotDetails, createPlot

urlpatterns = [
    path("create/plot", createPlot, name="createPlot"),
    path("create/plot/ajax/details", createPlotAjax, name="createPlot"),
    path("create/plot/details", addPlotDetails, name="addPlotDetails"),
    path("create/ajax/plot", createPlotAjax, name="createPlotAjax"),
    path("create/ajax/delete-plots", deletePlotsAjax, name="deletePlotAjax"),
    path("create/plot/ajax/delete-plots", deletePlotsAjax, name="deletePlotAjax"),
]
