from django.urls import path

from farm.views.farmCreator import FarmCreator
from farm.views.farmDisplay import FarmDisplay

urlpatterns = [
    path("create", FarmCreator.as_view()),
    path("details", FarmDisplay.as_view())

]
