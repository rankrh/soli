from django.shortcuts import render

from aria.views.create.plotDetails import PlotDetails

def createPlot(request):

    context = {"plots": [PlotDetails(1)]}
    return render(request, "aria/create/plot.html", context)
