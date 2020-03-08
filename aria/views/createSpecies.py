from django.http import HttpResponseRedirect
from ..forms.createSpecies import CreateSpeciesForm
from django.shortcuts import render


def createSpecies(request):
    if request.method == "POST":
        createSpeciesForm = CreateSpeciesForm(request.POST)
        if createSpeciesForm.is_valid():
            createSpeciesForm.saveSpecies(request)
            return HttpResponseRedirect("/aria/create-crop")
        else:
            return render(request, "aria/formValidationError.html", {'form': createSpeciesForm})
    else:
        context = {'form': CreateSpeciesForm()}
        return render(request, "aria/createSpecies.html", context)
