from django import forms

from aria.forms.templates.templates import createImageUpload, createTextInput
from aria.models.farm import Farm


class CreateFarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = [
            "name",
            "logo"
        ]

        widgets = {
            "name": createTextInput(placeholder="Farm Name", id="farm-name"),
            "logo": createImageUpload(id="farm-logo")
        }
