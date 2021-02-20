from django.urls import path

from taxonomy.views.create.speciesCreator import createSpecies, createGenus

urlpatterns = [
    path("create/species", createSpecies, name="createSpecies"),
    path("create/ajax/genus", createGenus, name="createGenus"),
]