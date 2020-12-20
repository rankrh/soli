from django.shortcuts import render

from aria.models import plotDetailsList
from aria.models.crop import Crop
from aria.models.event import Event
from aria.models.farm import Farm
from aria.models.harvest import Harvest
from aria.models.plotDetailsList import PlotDetailsList


def createCalendar(request):

    context = {
        "harvests": Harvest.objects.all(),
        "events": Event.objects.all(),
        "farms": Farm.objects.all(),
    }

    return render(request, "aria/planning/calendar.html", context)
