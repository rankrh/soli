from soli.views.authenticatedPageView import AuthenticatedPageView
from taxonomy.models.species import Species


class SeedbankDetail(AuthenticatedPageView):
    def get(self, request):
        self.construct(request)

        self.context["species"] = Species.objects.filter(
            crop__seedbank__user=self.user, crop__seedbank__quantity__gt=0
        ).distinct()
        self.context["seedbank_table_columns"] = ["Year", "Company", "Quantity"]

        return self.render("seedbank.html")

    def post(self, request):
        self.construct(request)
