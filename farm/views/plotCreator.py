import json

from django.shortcuts import render

from farm.models.farm import Farm
from farm.models.plot import Plot
from farm.models.plotDetailsList import PlotDetailsList
from soli.views.authenticatedPageView import AuthenticatedPageView


class PlotCreator(AuthenticatedPageView):
    context = {}
    params = {}

    def get(self, request, slug):

        self.construct(request)

        farm = Farm.objects.filter(slug=slug, farmer=request.user).get()
        plots = PlotDetailsList(request.user, farm=farm)

        self.context["farm"] = farm
        self.context["plots"] = plots.getParentPlots().jsonify()

        return self.render("plot_overview.html")

    def post(self, request, slug):
        self.params = request.POST
        farm = Farm.objects.filter(
            slug=slug, farmer=request.user, id=self.params["farm"]
        ).get()

        area = self.params["area"]
        vertexes = json.loads(self.params["points"])[0]

        if "plot" in self.params:
            plot = Plot.objects.filter(
                id=self.params["plot"], farmer=request.user
            ).get()
            plot.name = self.params["name"]
            plot.description = self.params["description"]
        else:
            plot = Plot(farmer=request.user, farm=farm)

        plot.update_boundaries(area, vertexes)
        plot.save()
        self.context["plot"] = plot

        return render(self.request, "plot_sidebar_detail.html", self.context)
