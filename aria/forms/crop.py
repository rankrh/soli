from django import forms
from ..models import Crop, Species
from .templates.templates import createTextInput, createSelectInput, createNumberInput, createRadioInput


class CreateCropForm(forms.ModelForm):

    class Meta:
        model = Crop
        fields = [
            "variety", "height", "weight", "yieldKg", "gallonsPerWeek", "sunPerDay", "category",
            "daysToHarvest"
        ]
        widgets = {
            "variety": createTextInput('Crop variety'),
            "height": createNumberInput("Crop height", minimum=0),
            "weight": createNumberInput("Crop weight", minimum=0),
            "yieldKg": createNumberInput("Yield in kilograms", minimum=0),
            "gallonsPerWeek": createNumberInput("Gallons of water per week", minimum=0),
            "sunPerDay": createRadioInput("Hours of sun per day"),
            "category": createRadioInput(""),
            "daysToHarvest": createNumberInput("Days from planting to harvest", 0, 365)
        }

    def __init__(self, *args, **kwargs):
        super(CreateCropForm, self).__init__(*args, **kwargs)
        self.fields["species"] = forms.ModelChoiceField(
            queryset=Species.objects.all(),
            widget=createSelectInput(attrs={
                "placeholder": "Crop species",
                "class": "font-italic"
            }),
        )

    def saveCrop(self, request):
        crop = self.save(commit=False)
        crop.species_id = request.POST["species"]
        crop.save()
