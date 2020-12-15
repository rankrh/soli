import json

from django.http import JsonResponse
from django.shortcuts import render

from aria.models.plotDetailsList import PlotDetailsList
from aria.models.plotDetails import PlotDetails
from aria.models.shape import Shape


def createPlot(request):
    plotDetailsList = PlotDetailsList()

    context = {"plots": plotDetailsList.getAllPlotDetails().jsonify()}
    return render(request, "aria/create/plot.html", context)


def addPlotDetails(request):
    plotDetailsList = PlotDetailsList()

    context = {"plots": plotDetailsList.getAllPlotDetails().jsonify()}

    return render(request, "aria/create/plotdetails.html", context)


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
        deleted, rows = Shape.objects.filter(plot__in=plots).delete()

        if deleted == 0:
            response["errors"] += f"Could not delete plots: {plots}"

    return JsonResponse(response)
