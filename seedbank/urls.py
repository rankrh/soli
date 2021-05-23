from django.urls import path

from seedbank.views.seedbankdetail import SeedbankDetail

urlpatterns = [
    path("", SeedbankDetail.as_view(), name="seedbank"),
]
