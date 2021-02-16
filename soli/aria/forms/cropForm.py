from aria.models.validation.cropValidation import ORGANIC_CHOICES, HYBRID_CHOICES, TREATED_CHOICES
from django import forms

from .templates.templates import createTextInput, createSelectInput, createTextArea, createRadioInput, createNumberInput
from ..models.crop import Crop
from ..models.species import Species


class CropForm(forms.ModelForm):

    class Meta:
        model = Crop
        fields = [
            "name",
            "description",
            "company",
            "organic",
            "treated",
            "hybrid",
            "species"
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
        super(CropForm, self).__init__(*args, **kwargs)
        self.fields["species"] = forms.ModelChoiceField(
            queryset=Species.objects.all(),
            widget=createSelectInput("Crop species", ["font-italic"]),
        )
        self.fields["species"].empty_label = "Species"

    def saveCrop(self):
        crop = self.save(commit=False)
        crop.save()

        return crop
