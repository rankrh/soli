from django.shortcuts import render

from aria.models.crop import Crop
from aria.models.event import Event
from aria.models.harvest import Harvest


def createCalendar(request):

    context = {
        "harvests": Harvest.objects.all(),
        "events": Event.objects.all()
    }

    return render(request, "aria/planning/calendar.html", context)
