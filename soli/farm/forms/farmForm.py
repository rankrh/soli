from django import forms

from farm.models.farm import Farm
from formTemplates.inputFields import createImageUpload, createTextInput


class CreateFarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = [
            "name",
            "logo"
        ]

        widgets = {
            "name": createTextInput(placeholder="Farm Name", id="plot-name"),
            "logo": createImageUpload(id="plot-logo")
        }
