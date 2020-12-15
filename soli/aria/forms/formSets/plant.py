from aria.forms.templates.templates import createNumberInput, createSelectInput
from django.forms import inlineformset_factory
from django import forms

from aria.models.crop import Crop
from aria.models.planting import Planting

plantFormSet = inlineformset_factory(
    Crop,
    Planting,
    fields=[
        "pattern",
        "spacing",
        "frost",
        "date",
        "location"
    ],
    extra=1,
    can_delete=False,
    widgets={
        "pattern": forms.RadioSelect(attrs={
            "name": "pattern",
            "id": "pattern"
        }),
        "spacing": createNumberInput(),
        "frost": createSelectInput(),
        "date": createNumberInput(None, 0),
        "location": forms.RadioSelect(attrs={
            "onchange": "togglePattern();",
            "name": "location",
            "id": "location"
        })
    })


class PlantFormSet(plantFormSet):

    def __init__(self, *args, **kwargs):
        super(PlantFormSet, self).__init__(*args, **kwargs)

        for form in self.forms:
            form.empty_permitted = False
