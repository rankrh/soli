from django import forms
from ..models import Crop
from .templates.templates import createTextInput, createSelectInput, createNumberInput, createRadioInput


class CreateCropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = [
            "variety", "species", "height", "weight", "yieldKg", "gallonsPerWeek", "sunPerDay", "category",
            "daysToHarvest"
        ]
        widgets = {
            "variety": createTextInput('Crop variety'),
            "species": createSelectInput("Crop species"),
            "height": createNumberInput("Crop height", minimum=0),
            "weight": createNumberInput("Crop weight", minimum=0),
            "yieldKg": createNumberInput("Yield in kilograms", minimum=0),
            "gallonsPerWeek": createNumberInput("Gallons of water per week", minimum=0),
            "sunPerDay": createRadioInput("Hours of sun per day"),
            "category": createRadioInput(""),
            "daysToHarvest": createNumberInput("Days from planting to harvest", 0, 365)
        }
