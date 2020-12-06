import json

from django.http import JsonResponse
from django.shortcuts import render

from aria.forms.plot import PlotForm, initialValues
from aria.models.plotDetails import PlotDetails


def createPlot(request):
    context = {"plots": [PlotDetails(1).jsonify(), PlotDetails(2).jsonify()]}
    return render(request, "aria/create/plot.html", context)


def createPlotAjax(request):
    response = {"errors": []}
    if request.is_ajax() and request.method == "POST":
        plotForm = PlotForm(request.POST, initial=initialValues)
        if plotForm.is_valid():
            plot = plotForm.savePlot()
        else:
            print(plotForm.errors)
            response["errors"] = plotForm.errors

    return JsonResponse(response)
