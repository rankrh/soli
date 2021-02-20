from django.shortcuts import render

from farm.models.farm import Farm


def home(request):

    context = {
        "user": request.user,
        "farmList": Farm.objects.filter(owner=request.user)
    }

    return render(request, "account/home.html", context)
