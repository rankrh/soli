from farm.models.farm import Farm
from soli.views.authenticatedPageView import AuthenticatedPageView


class FarmOverview(AuthenticatedPageView):
    farm = None
    request = None
    context = {}

    def get(self, request, slug):

        self.construct(request)
        self.context["farm"] = Farm.objects.filter(slug=slug, owner=request.user).get()

        self.context["cards"] = ["map", "contact", "overview"]

        return self.render("farm_overview.html")
