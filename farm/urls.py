from django.urls import path

from farm.views.farmApi import FarmApi
from farm.views.plotRemover import PlotRemover
from farm.views.farmCreator import FarmCreator
from farm.views.farmOverview import FarmOverview
from farm.views.plotCreator import PlotCreator

urlpatterns = [
    path("", FarmApi.as_view(), name="my-farms"),
    path("/<slug:slug>", FarmApi.as_view(), name="my-farms"),
    path("old/create", FarmCreator.as_view(), name="createFarm"),
    path("old/<slug:slug>", FarmOverview.as_view(), name="farmOverview"),
    path("old/<slug:slug>/plots", PlotCreator.as_view(), name="plotOverview"),
    path("old/<slug:slug>/plots/create", PlotCreator.as_view(), name="plotCreator"),
    path("old/<slug:slug>/plots/delete", PlotRemover.as_view(), name="plotCreator"),
]
