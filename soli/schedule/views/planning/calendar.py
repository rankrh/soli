from django.shortcuts import render

from schedule.models.event import Event
from farm.models.farm import Farm
from crop.models.harvest import Harvest


def createCalendar(request):

    context = {
        "harvests": Harvest.objects.all(),
        "events": Event.objects.all(),
        "farms": Farm.objects.all(),
    }

    return render(request, "plot/planning/calendar.html", context)
