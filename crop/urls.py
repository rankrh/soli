from django.urls import path

from crop.views.create.cropCreator import createCrop

urlpatterns = [
    path("create/crop", createCrop, name="createCrop"),
]
