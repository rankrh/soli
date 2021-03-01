from django.http import HttpResponseRedirect
from django.shortcuts import render

from crop.forms.cropCareForm import CropCareFormSet
from crop.forms.cropForm import CropForm
from crop.forms.harvestForm import HarvestFormSet
from crop.forms.plantingDateForm import PlantingDateFormSet
from crop.forms.plantingForm import PlantingFormSet


def createCrop(request):
    if request.method == "POST":
        createCropForm = CropForm(request.POST)
        plantingForms = PlantingFormSet(request.POST)
        plantingDateForms = PlantingDateFormSet(request.POST)
        careForms = CropCareFormSet(request.POST)
        harvestForms = HarvestFormSet(request.POST)

        if createCropForm.is_valid() \
                and plantingForms.is_valid() \
                and plantingDateForms.is_valid() \
                and careForms.is_valid() \
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

        return HttpResponseRedirect("/plot/display/crops")

    else:
        context = {
            "cropForm": CropForm(),
            "plantingFormSet": PlantingFormSet(),
            "plantingDateFormSet": PlantingDateFormSet(),
            "careFormSet": CropCareFormSet(),
            "harvestFormSet": HarvestFormSet()
        }

        return render(request, "plot/create/crop.html", context)
