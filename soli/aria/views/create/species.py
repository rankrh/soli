from aria.forms.genus import CreateGenusForm
from django.http import HttpResponseRedirect, JsonResponse
from aria.forms.species import CreateSpeciesForm, subspeciesFormSet
from django.shortcuts import render


def createSpecies(request):
    if request.method == "POST":
        createSpeciesForm = CreateSpeciesForm(request.POST)
        if createSpeciesForm.is_valid():
            createSpeciesForm.saveSpecies(request)
            return HttpResponseRedirect("/aria/create/crop")
        else:
            return render(request, "aria/formValidationError.html", {'form': createSpeciesForm})
    else:
        context = {
            'speciesForm': CreateSpeciesForm(),
            'subspecies': subspeciesFormSet(),
            'genusForm': CreateGenusForm()
        }
        return render(request, "aria/create/species.html", context)


def createGenus(request):

    response = {"errors": []}
    if request.is_ajax() and request.method == "POST":
        createGenusForm = CreateGenusForm(request.POST)
        if createGenusForm.is_valid():
            genus = createGenusForm.saveGenus(request)
            response["id"] = genus.id
            response["name"] = genus.name
        else:
            response["errors"].append(createGenusForm.errors)
    return JsonResponse(response)
