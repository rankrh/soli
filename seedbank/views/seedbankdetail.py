from crop.models.crop import Crop
from seedbank.models.seedbank import Seedbank
from soli.views.authenticatedPageView import AuthenticatedPageView


class SeedbankDetail(AuthenticatedPageView):
    def get(self, request):
        self.construct(request)

        self.context["seedbank"] = Seedbank.objects.filter(user=self.user)
        self.context["crops"] = Crop.objects.all()

        return self.render("seedbank.html")

    def post(self, request):
        self.construct(request)
