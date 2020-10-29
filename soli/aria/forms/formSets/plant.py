from aria.forms.templates.templates import createNumberInput, createSelectInput
from aria.models import Crop, Plant
from django.forms import inlineformset_factory
from django import forms

plantFormSet = inlineformset_factory(
    Crop,
    Plant,
    fields=[
        "pl_pattern",
        "pl_spacing",
        "pl_frost",
        "pl_date",
        "pl_location"
    ],
    extra=1,
    can_delete=False,
    widgets={
        "pl_pattern": forms.RadioSelect(attrs={
            "name": "pattern",
            "id": "pattern"
        }),
        "pl_spacing": createNumberInput(),
        "pl_frost": createSelectInput(),
        "pl_date": createNumberInput(None, 0),
        "pl_location": forms.RadioSelect(attrs={
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
