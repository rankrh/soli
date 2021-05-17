import json

from django.shortcuts import render

from farm.models.farm import Farm
from farm.models.plot import Plot
from farm.models.plotDetailsList import PlotDetailsList
from geometry.models.point import Point
from geometry.models.shape import Shape, POLYGON
from soli.views.authenticatedPageView import AuthenticatedPageView


def savePlotDetails(plot, points, shape):
    shape.save()
    for point in points:
        point.save()
    plot.save()


class PlotCreator(AuthenticatedPageView):
    context = {}
    params = {}

    def get(self, request, slug):

        self.construct(request)

        farm = Farm.objects.filter(slug=slug, owner=request.user).get()
        plots = PlotDetailsList(request.user, farm=farm)

        self.context["farm"] = farm
        self.context["plots"] = plots.getParentPlots().jsonify()

        return self.render("plotOverview.html")

    def post(self, request, slug):
        self.params = request.POST
        farm = Farm.objects.filter(
            slug=slug, owner=request.user, id=self.params["farm"]
        ).get()

        if self.plotExists():
            plot = Plot.objects.filter(id=self.params["plot"]).get()
            points, shape = self.updatePlotBoundaries(plot)
        else:
            points, shape = self.createPlotBoundaries()
            plot = Plot(owner=request.user, farm=farm, shape=shape)

        savePlotDetails(plot, points, shape)
        self.context["plot"] = plot

        return render(self.request, "plotSidebarDetail.html", self.context)

    def plotExists(self):
        return "plot" in self.params

    def updatePlotBoundaries(self, plot):
        plot.shape.delete()
        points, shape = self.createPlotBoundaries()
        plot.shape = shape
        return points, shape

    def createPlotBoundaries(self):
        shape = Shape(type=POLYGON, area=self.params["area"])
        vertexes = []
        points1 = json.loads(self.params["points"])[0]
        for point in points1:
            vertexes.append(Point(shape=shape, lat=point["lat"], long=point["lng"]))
        points = vertexes
        return points, shape
