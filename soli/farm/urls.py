from django.urls import path

from farm.views.create.farmCreator import createFarm

urlpatterns = [
    path("create/plot", createFarm, name="createFarm"),

]
