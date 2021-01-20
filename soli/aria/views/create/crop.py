from django.http import HttpResponseRedirect
from django.shortcuts import render

from aria.forms.crop import CropForm
from aria.forms.formSets.cropCare import CropCareFormSet, CropCareForm
from aria.forms.formSets.harvest import HarvestFormSet, HarvestForm
from aria.forms.formSets.planting import PlantingFormSet, PlantingForm


def createCrop(request):
    if request.method == "POST":
        createCropForm = CropForm(request.POST)
        plantingForm = PlantingForm(request.POST)
        careForm = CropCareForm(request.POST)
        harvestForm = HarvestForm(request.POST)

        if createCropForm.is_valid()\
                and plantingForm.is_valid()\
                and careForm.is_valid()\
                and harvestForm.is_valid():

            crop = createCropForm.saveCrop()
            plantingForm.savePlanting(crop)
            careForm.saveCare(crop)
            harvestForm.saveHarvest(crop)

        return HttpResponseRedirect("/aria/display/crops")

    else:
        context = {
            "cropForm": CropForm(),
            "plantingFormSet": PlantingFormSet(),
            "careFormSet": CropCareFormSet(),
            "harvestFormSet": HarvestFormSet()
        }
        return render(request, "aria/create/crop.html", context)
