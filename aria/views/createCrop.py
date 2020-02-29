from django.http import HttpResponse
from ..forms.createCrop import CreateCropForm
from django.shortcuts import render

def createCrop(request):

    createCropForm = CreateCropForm()
    context = {'form': createCropForm}

    return render(request, "aria/createCrop.html", context)