from django import forms
from django.forms import inlineformset_factory

from crop.models.crop import Crop
from crop.models.planting import Planting
from formTemplates.inputFields import createNumberInput, createSelectInput


class PlantingForm(forms.ModelForm):
    class Meta:
        model = Planting

        fields = [
            "soilTemperatureMin",
            "soilTemperatureMax",
            "germinationStart",
            "germinationEnd",
            "depth",
        ]

        widgets = {
            "temperatureMin": createNumberInput(),
            "temperatureMax": createNumberInput(),
            "germinationStart": createNumberInput(0),
            "germinationEnd": createNumberInput(0),
            "depth": createNumberInput(0),
        }

    def savePlanting(self, crop):
        planting = self.save(commit=False)
        planting.crop = crop

        planting.save()


PlantingFormSet = inlineformset_factory(Crop, Planting, PlantingForm, extra=1)
