from django.urls import path

from schedule.views.calendarView import CalendarView

urlpatterns = [
    path("", CalendarView.as_view(), name="calendar"),
]
