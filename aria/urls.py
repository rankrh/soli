from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("create-crop", views.createCrop, name="createCrop"),
	path("list-crops", views.listCrops, name="listCrops")
]
