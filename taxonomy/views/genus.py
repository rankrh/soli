from django.http import JsonResponse

from soli.views.administorPageView import AdministratorPageView
from taxonomy.forms.genusForm import CreateGenusForm


class Genus(AdministratorPageView):
    def get(self, request):
        self.construct(request)

    def post(self, request):
        self.construct(request)

        response = {"errors": []}
        if request.is_ajax():
            createGenusForm = CreateGenusForm(request.POST)
            if createGenusForm.is_valid():
                genus = createGenusForm.saveGenus(request)
                response["id"] = genus.id
                response["name"] = genus.name
            else:
                response["errors"].append(createGenusForm.errors)
        return JsonResponse(response)
