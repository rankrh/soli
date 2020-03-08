from django.http import HttpResponseRedirect
from ..forms.createCrop import CreateCropForm
from django.shortcuts import render


def createCrop(request):
    if request.method == "POST":
        createCropForm = CreateCropForm(request.POST)
        if createCropForm.is_valid():
            createCropForm.saveCrop(request)
            return HttpResponseRedirect("/aria/list-crops")
        else:
            return render(request, "aria/formValidationError.html", {'form': createCropForm})
    else:
        context = {'form':  CreateCropForm()}
        return render(request, "aria/createCrop.html", context)
