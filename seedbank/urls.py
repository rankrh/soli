from django.urls import path

from seedbank.views.seedbank import Seedbank

urlpatterns = [
    path("", Seedbank.as_view(), name="seedbank"),
]
