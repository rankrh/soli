from aria.forms.templates.templates import createNumberInput, createSelectInput
from django.forms import inlineformset_factory
from django import forms

from aria.models.crop import Crop
from aria.models.planting import Planting


class PlantingForm(forms.ModelForm):
    class Meta:
        model = Planting

        fields = [
            "pattern",
            "rowSpacingMin",
            "rowSpacingMax",
            "interRowSpacingMin",
            "interRowSpacingMax",
            "soilTemperatureMin",
            "soilTemperatureMax",
            "germinationStart",
            "germinationEnd",
            "depth"
        ]

        widgets = {
            "pattern": createSelectInput(),
            "rowSpacingMin": createNumberInput(),
            "rowSpacingMax": createNumberInput(),
            "interRowSpacingMin": createNumberInput(),
            "interRowSpacingMax": createNumberInput(),
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
