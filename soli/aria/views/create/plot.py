from django.http import JsonResponse
from django.shortcuts import render

from aria.forms.plot import PlotForm
from aria.models.Points import Points
from aria.models.plotDetails import PlotDetails, PlotDetailsList


def createPlot(request):
    context = {"plots": PlotDetailsList().getAllDetails()}
    return render(request, "aria/create/plot.html", context)


def createPlotAjax(request):
    response = {"errors": []}
    if request.is_ajax() and request.method == "POST":
        plotForm = PlotForm(request.POST)

        if plotForm.is_valid():
            plot = plotForm.savePlot()
            points = Points(request.POST, plot)
            points.savePoints()

            response["plt_num"] = plot.plt_num
        else:
            print(plotForm.errors)
            response["errors"] = plotForm.errors

    return JsonResponse(response)
