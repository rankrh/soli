from django.urls import path

from farm.views.plotRemover import PlotRemover
from farm.views.farmCreator import FarmCreator
from farm.views.farmOverview import FarmOverview
from farm.views.plotCreator import PlotCreator

urlpatterns = [
    path("create", FarmCreator.as_view(), name="createFarm"),
    path("<slug:slug>", FarmOverview.as_view(), name="farmOverview"),
    path("<slug:slug>/plots", PlotCreator.as_view(), name="plotOverview"),
    path("<slug:slug>/plots/create", PlotCreator.as_view(), name="plotCreator"),
    path("<slug:slug>/plots/delete", PlotRemover.as_view(), name="plotCreator"),
]
