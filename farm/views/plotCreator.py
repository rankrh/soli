from farm.models.farm import Farm
from farm.models.plotDetailsList import PlotDetailsList
from soli.views.authenticatedPageView import AuthenticatedPageView


class PlotCreator(AuthenticatedPageView):

    context = {}

    def get(self, request, slug):

        self.construct(request)

        farm = Farm.objects.filter(slug=slug, owner=request.user).get()
        plots = PlotDetailsList(request.user).getParentPlots().jsonify()

        self.context["farm"] = farm
        self.context["plots"] = plots

        return self.renderPage("plotOverview.html")

    def post(self):
        pass
