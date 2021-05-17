from django.urls import path

from herd.views.herd import Herd

urlpatterns = [
    path("", Herd.as_view(), name="herd"),
]
