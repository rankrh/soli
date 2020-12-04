import json

from django.shortcuts import render

from aria.models.plotDetails import PlotDetails


def createPlot(request):

    context = {"plots": [PlotDetails(1).jsonify(), PlotDetails(2).jsonify()]}
    return render(request, "aria/create/plot.html", context)
