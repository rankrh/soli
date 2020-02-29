from django.shortcuts import render
from ..models.crop import Crop


def listCrops(request):
    crops = Crop.objects.all()
    context = {"crops": crops}

    return render(request, "aria/listCrops.html", context)
