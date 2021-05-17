from django.http import HttpResponseRedirect

from crop.forms.cropCareForm import CropCareFormSet
from crop.forms.cropForm import CropForm
from crop.forms.harvestForm import HarvestFormSet
from crop.forms.plantingDateForm import PlantingDateFormSet
from crop.forms.plantingForm import PlantingFormSet
from soli.views.authenticatedPageView import AuthenticatedPageView


class CropCreator(AuthenticatedPageView):
    def post(self, request):
        createCropForm = CropForm(request.POST)
        plantingForms = PlantingFormSet(request.POST)
        plantingDateForms = PlantingDateFormSet(request.POST)
        careForms = CropCareFormSet(request.POST)
        harvestForms = HarvestFormSet(request.POST)

        if (
            createCropForm.is_valid()
            and plantingForms.is_valid()
            and plantingDateForms.is_valid()
            and careForms.is_valid()
            and harvestForms.is_valid()
        ):

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

        return HttpResponseRedirect("")

    def get(self, request):
        self.construct(request)

        self.context["cropForm"] = CropForm()
        self.context["plantingFormSet"] = PlantingFormSet()
        self.context["plantingDateFormSet"] = PlantingDateFormSet()
        self.context["careFormSet"] = CropCareFormSet()
        self.context["harvestFormSet"] = HarvestFormSet()

        return self.render("create_crop.html")
