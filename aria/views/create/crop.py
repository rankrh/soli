from django.http import HttpResponseRedirect
from aria.forms.crop import CropForm
from django.shortcuts import render


def createCrop(request):
    if request.method == "POST":
        createCropForm = CropForm(request.POST)
        if createCropForm.is_valid():
            createCropForm.saveCrop(request)
            return HttpResponseRedirect("/aria/display/crops")
        else:
            return render(request, "aria/formValidationError.html", {'cropForm': createCropForm})
    else:
        context = {
            'cropForm':  CropForm(),
        }
        return render(request, "aria/create/crop.html", context)
