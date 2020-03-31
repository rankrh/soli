from aria.forms.createGenus import CreateGenusForm
from django.http import HttpResponseRedirect, JsonResponse
from aria.forms.createSpecies import CreateSpeciesForm
from django.shortcuts import render


def createSpecies(request):
    if request.method == "POST":
        createSpeciesForm = CreateSpeciesForm(request.POST)
        if createSpeciesForm.is_valid():
            createSpeciesForm.saveSpecies(request)
            return HttpResponseRedirect("/aria/list/crop")
        else:
            return render(request, "aria/formValidationError.html", {'form': createSpeciesForm})
    else:
        context = {
            'speciesForm': CreateSpeciesForm(),
            'genusForm': CreateGenusForm()
        }
        return render(request, "aria/create/species.html", context)


def createSpeciesAjax(request):

    response = {"errors": []}
    if request.is_ajax() and request.method == "POST":
        createGenusForm = CreateGenusForm(request.POST)
        if createGenusForm.is_valid():
            genus = createGenusForm.saveGenus(request)
            response["id"] =  genus.id
            response["genus"] = genus.genus
        else:
            response["errors"].append("This genus already exists")
    return JsonResponse(response)
