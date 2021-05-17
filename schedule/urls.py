from django.urls import path

from schedule.views.calendar import Calendar

urlpatterns = [
    path("", Calendar.as_view(), name="calendar"),
]
