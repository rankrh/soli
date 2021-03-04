from farm.models.farm import Farm
from farm.models.plotDetailsList import PlotDetailsList
from soli.views.authenticatedPageView import AuthenticatedPageView


class FarmOverview(AuthenticatedPageView):
    farm = None
    request = None
    context = {}

    def get(self, request, slug):

        self.construct(request)

        self.context["farm"] = Farm.objects.filter(slug=slug, owner=request.user).get()

        return self.renderPage("farmOverview.html")
