from django.shortcuts import render


def createGarden(request):

    context = {}
    return render(request, "aria/create/garden.html", context)