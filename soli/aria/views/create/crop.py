from django.http import HttpResponseRedirect
from aria.forms.crop import CreateCropForm
from django.shortcuts import render


def createCrop(request):

    if request.method == "POST":
        createCropForm = CreateCropForm(request.POST)
        if createCropForm.is_valid():
            createCropForm.saveCrop(request)
            return HttpResponseRedirect("/aria/display/crops")
        else:
            print(createCropForm.errors)
            return render(request, "aria/formValidationError.html", {'cropForm': createCropForm})
    else:
        context = {
            'cropForm':  CreateCropForm(),
        }
        return render(request, "aria/create/crop.html", context)
