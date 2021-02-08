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
            "rowSpacing",
            "interRowSpacing",
            "frost",
            "date",
            "location",
            "temperature",
            "germination",
            "depth",
            "transplant"
        ]

        widgets = {
            "pattern": createSelectInput(),
            "rowSpacing": createNumberInput(placeholder="Space between rows"),
            "interRowSpacing": createNumberInput(placeholder="Space between plants"),
            "frost": createSelectInput(),
            "date": createNumberInput(None, 0),
            "location": createSelectInput(),
            "temperature": createNumberInput("Ideal soil temperature"),
            "germination": createNumberInput("Days to germination", 0),
            "depth": createNumberInput("Seed depth", 0),
            "transplant": createNumberInput("Weeks", 0)

        }

    def savePlanting(self, crop):

        planting = self.save(commit=False)
        planting.crop = crop

        planting.save()


PlantingFormSet = inlineformset_factory(Crop, Planting, PlantingForm, extra=1)
