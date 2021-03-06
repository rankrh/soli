import json

from django.http import JsonResponse
from django.shortcuts import render

from farm.models.farm import Farm
from geometry.models.shape import Shape
from farm.models.plotDetails import PlotDetails
from farm.models.plotDetailsList import PlotDetailsList
from farm.models.validation.plotTypes import TYPES


def createPlot(request):
    page = ""
    context = {}
    if request.user.id is not None:
        plotDetailsList = PlotDetailsList(request.user)
        farm = Farm.objects.filter(farmer=request.user).first()

        if request.method == "GET":
            page = "plot/create/plot.html"
            context = {
                "plots": plotDetailsList.getParentPlots().jsonify(),
                "plot": farm,
            }

        elif request.method == "POST":
            return addPlotDetails(request)

    return render(request, page, context)


def addPlotDetails(request):
    if request.user.id is not None:
        plotDetailsList = PlotDetailsList(farmer=request.user)

        context = {
            "plots": plotDetailsList.getPlotDetailsForUser().jsonify(),
            "plotTypes": TYPES,
        }
    else:
        context = {}

    return render(request, "plot/create/plotdetails.html", context)


def createPlotAjax(request):
    response = {"errors": []}
    if request.user and request.is_ajax() and request.method == "POST":
        plotDetails = createNewPlot(request)
        response["plot"] = plotDetails.plot.id

        if "returnPage" in request.POST:
            context = {"child": plotDetails.plot}

            return render(request, request.POST["returnPage"] + ".html", context)
        else:
            return JsonResponse(response)


def createNewPlot(request):
    plotDetails = PlotDetails(request=request)
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
