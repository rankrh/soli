from aria.forms.formSets.grow import GrowFormSet
from aria.forms.formSets.harvest import HarvestFormSet
from aria.forms.formSets.plant import PlantFormSet
from aria.models.validation.cropValidation import ORGANIC_CHOICES, HYBRID_CHOICES, TREATED_CHOICES
from django import forms

from .templates.templates import createTextInput, createSelectInput, createTextArea, createRadioInput, createNumberInput
from ..models.crop import Crop
from ..models.species import Species


class CreateCropForm(forms.ModelForm):
    plant = PlantFormSet()
    grow = GrowFormSet()
    harvest = HarvestFormSet()

    class Meta:
        model = Crop
        fields = [
            "name",
            "description",
            "company",
            "organic",
            "treated",
            "hybrid"
        ]

        widgets = {
            "name": createTextInput("Name"),
            "description": createTextArea("Description"),
            "company": createTextInput("Company"),
            "organic": createRadioInput(choices=ORGANIC_CHOICES),
            "treated": createRadioInput(choices=TREATED_CHOICES),
            "hybrid": createRadioInput(choices=HYBRID_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super(CreateCropForm, self).__init__(*args, **kwargs)
        self.fields["species"] = forms.ModelChoiceField(
            queryset=Species.objects.all(),
            widget=createSelectInput("Crop species", ["font-italic"]),
        )
        self.fields["species"].empty_label = "Species"

    def saveCrop(self, request):
        crop = self.save(commit=False)
        crop.save()
