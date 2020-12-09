import json

from django.http import JsonResponse
from django.shortcuts import render

from aria.models import Plot
from aria.models.PlotDetailsList import PlotDetailsList
from aria.models.plotDetails import PlotDetails


def createPlot(request):
    plotDetailsList = PlotDetailsList()

    context = {"plots": plotDetailsList.getAllPlotDetails().jsonify()}
    return render(request, "aria/create/plot.html", context)


def createPlotAjax(request):
    response = {"errors": []}
    if request.is_ajax() and request.method == "POST":
        plotDetails = createNewPlot(request)
        try:
            response["plot"] = plotDetails.plot.id
        except:
            response["errors"] = plotDetails.plotForm.errors

    return JsonResponse(response)


def createNewPlot(request):
    plotDetails = PlotDetails(request)
    if plotDetails.isValidPlot():
        plotDetails.savePlotAndPoints()

    return plotDetails


def deletePlotsAjax(request):
    response = {"errors": []}

    if request.is_ajax() and request.method == "POST":
        plots = json.loads(request.POST["plots"])
        deleted, rows = Plot.objects.filter(pk__in=plots).delete()

        if deleted == 0:
            response["errors"] += f"Could not delete plots: {plots}"

    return JsonResponse(response)
