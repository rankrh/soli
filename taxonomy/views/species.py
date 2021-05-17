from soli.views.administorPageView import AdministratorPageView
from taxonomy.forms.genusForm import CreateGenusForm
from taxonomy.forms.speciesForm import CreateSpeciesForm, subspeciesFormSet


class Species(AdministratorPageView):
    def get(self, request):
        self.construct(request)
        self.context = {
            **self.context,
            **{
                "speciesForm": CreateSpeciesForm(),
                "subspecies": subspeciesFormSet(),
                "genusForm": CreateGenusForm(),
            },
        }

        return self.render("species.html")

    def post(self, request):
        self.construct(request)

        createSpeciesForm = CreateSpeciesForm(request.POST)
        if createSpeciesForm.is_valid():
            createSpeciesForm.saveSpecies(request)
            return self.redirect("/admin/crop/")
