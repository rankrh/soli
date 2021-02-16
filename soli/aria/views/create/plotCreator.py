import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from aria.models.farm import Farm
from aria.models.plotDetailsList import PlotDetailsList
from aria.models.plotDetails import PlotDetails
from aria.models.shape import Shape
from aria.models.validation.plotTypes import TYPES


class PlotCreator(View):

    page = ""
    template = ""
    user = None
    context = {}
    plotDetailsList = None
    farm = None

    def get(self, request):
        self.user = request.user
        self.page = request.path
        if self.user.id is not None:
            self.plotDetailsList = PlotDetailsList(request.user)
            self.farm = Farm.objects.filter(owner=request.user).first()
            self.template = "aria/create/plot.html"
            self.context = {
                "plots": self.plotDetailsList.getPlotDetailsForUser().jsonify(),
                "farm": self.farm,
                "plotTypes": self.plotTypes
            }

        else:

        return render(request, self.template, self.context)

    def post(self, request):
        pass


def createPlot(request):

    page = ""
    context = {}
    if request.user.id is not None:
        plotDetailsList = PlotDetailsList(request.user)
        farm = Farm.objects.filter(owner=request.user).first()

        if request.method == "GET":
            page = "aria/create/plot.html"
            context = {
                "plots": plotDetailsList.getParentPlots().jsonify(),
                "farm": farm
            }

        elif request.method == "POST":
            return addPlotDetails(request)

    return render(request, page, context)


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