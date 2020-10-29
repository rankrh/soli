from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),


	# Create
	path("create/crop", views.createCrop, name="createCrop"),
	path("create/species", views.createSpecies, name="createSpecies"),
	path("create/ajax/genus", views.createGenus, name="createGenus"),
	
	# Display
	path("display/crops", views.displayCrops, name="displayCrops"),
]
