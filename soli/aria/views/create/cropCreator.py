from django.http import HttpResponseRedirect
from django.shortcuts import render

from aria.forms.cropForm import CropForm
from aria.forms.cropCareForm import CropCareFormSet
from aria.forms.harvestForm import HarvestFormSet
from aria.forms.plantingForm import PlantingFormSet
from aria.forms.plantingDateForm import PlantingDateFormSet


def createCrop(request):
    if request.method == "POST":
        createCropForm = CropForm(request.POST)
        plantingForms = PlantingFormSet(request.POST)
        plantingDateForms = PlantingDateFormSet(request.POST)
        careForms = CropCareFormSet(request.POST)
        harvestForms = HarvestFormSet(request.POST)

        if createCropForm.is_valid()\
                and plantingForms.is_valid()\
                and plantingDateForms.is_valid()\
                and careForms.is_valid()\
                and harvestForms.is_valid():

            crop = createCropForm.saveCrop()
            for plantingForm in plantingForms:
                plantingForm.savePlanting(crop)

            for plantingDateForm in plantingDateForms:
                plantingDateForm.savePlantingDate(crop)

            plantingForm.savePlanting(crop)
            plantingDateForm.savePlantingDate(crop)
            for careForm in careForms:
                careForm.saveCare(crop)

            for harvestForm in harvestForms:
                harvestForm.saveHarvest(crop)
        else:
            print(createCropForm.errors)
            print(plantingForms.errors)
            print(plantingDateForms.errors)
            print(careForms.errors)
            print(harvestForms.errors)

        return HttpResponseRedirect("/aria/display/crops")

    else:
        context = {
            "cropForm": CropForm(),
            "plantingFormSet": PlantingFormSet(),
            "plantingDateFormSet": PlantingDateFormSet(),
            "careFormSet": CropCareFormSet(),
            "harvestFormSet": HarvestFormSet()
        }

        return render(request, "aria/create/crop.html", context)
