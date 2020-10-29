from aria.forms.formSets.grow import GrowFormSet
from aria.forms.formSets.harvest import HarvestFormSet
from aria.forms.formSets.plant import PlantFormSet
from aria.models import Species, Crop
from aria.models.validation.crop import ORGANIC_CHOICES, HYBRID_CHOICES, TREATED_CHOICES
from django import forms

from .templates.templates import createTextInput, createSelectInput, createTextArea, createRadioInput, createNumberInput


class CreateCropForm(forms.ModelForm):
    plant = PlantFormSet()
    grow = GrowFormSet()
    harvest = HarvestFormSet()

    class Meta:
        model = Crop
        fields = [
            "cr_variety",
            "cr_description",
            "cr_company",
            "cr_organic",
            "cr_treated",
            "cr_hybrid"
        ]

        widgets = {
            "cr_variety": createTextInput("Variety"),
            "cr_description": createTextArea("Description"),
            "cr_company": createTextInput("Company"),
            "cr_organic": createRadioInput(choices=ORGANIC_CHOICES),
            "cr_treated": createRadioInput(choices=TREATED_CHOICES),
            "cr_hybrid": createRadioInput(choices=HYBRID_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super(CreateCropForm, self).__init__(*args, **kwargs)
        self.fields["cr_sp_num"] = forms.ModelChoiceField(
            queryset=Species.objects.all(),
            widget=createSelectInput("Crop species", ["font-italic"]),
        )
        self.fields["cr_sp_num"].empty_label = "Species"

    def saveCrop(self, request):
        crop = self.save(commit=False)
        crop.save()
