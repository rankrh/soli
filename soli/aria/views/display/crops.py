from django.shortcuts import render
from aria.models.crop import Crop


def displayCrops(request):
    crops = Crop.objects.all()
    context = {"crops": crops}

    return render(request, "aria/list/crop.html", context)
