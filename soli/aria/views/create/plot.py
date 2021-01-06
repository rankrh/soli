import json

from django.http import JsonResponse
from django.shortcuts import render

from aria.models.farm import Farm
from aria.models.plotDetailsList import PlotDetailsList
from aria.models.plotDetails import PlotDetails
from aria.models.shape import Shape
from aria.models.validation.plotTypes import TYPES


def createPlot(request):
    if request.user:
        current_user = request.user
        plotDetailsList = PlotDetailsList(current_user)
        farm = Farm.objects.filter(owner=current_user).first()

        context = {
            "plots": plotDetailsList.getParentPlots().jsonify(),
            "farm": farm
            }
    else:
        context = {}

    return render(request, "aria/create/plot.html", context)


def addPlotDetails(request):
    if request.user.id is not None:
        plotDetailsList = PlotDetailsList(owner=request.user)

        context = {
            "plots": plotDetailsList.getPlotDetailsForUser().jsonify(),
            "plotTypes": TYPES
        }
    else:
        context = {}

    return render(request, "aria/create/plotdetails.html", context)


def createPlotAjax(request):
    response = {"errors": []}
    if request.user and request.is_ajax() and request.method == "POST":
        plotDetails = createNewPlot(request)
        response["plot"] = plotDetails.plot.id

        if "returnPage" in request.POST:
            context = {
                "child": plotDetails.plot
            }

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
