from aria.forms.genus import CreateGenusForm
from aria.forms.templates.templates import createTextInput
from aria.models import Species, Subspecies
from django.forms import inlineformset_factory
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
