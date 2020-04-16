from aria.models import Genus, Species, Subspecies, Crop, Plant, Grow, Harvest
from aria.models.validation.crop import ORGANIC_CHOICES, HYBRID_CHOICES, TREATED_CHOICES
from aria.models.validation.grow import SUN
from aria.models.validation.harvest import CROP_TYPE
from django import forms
from django.forms import inlineformset_factory

from .templates.templates import createTextInput, createSelectInput, createTextArea, createRadioInput, createNumberInput


class CreateCropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = [
            "variety",
            "description",
            "company",
            "organic",
            "treated",
            "hybrid",
            "temperature",
            "depth",
            "germination"
        ]

        widgets = {
            "variety": createTextInput("Variety"),
            "description": createTextArea("Description"),
            "company": createTextInput("Company"),
            "organic": createRadioInput(choices=ORGANIC_CHOICES),
            "treated": createRadioInput(choices=TREATED_CHOICES),
            "hybrid": createRadioInput(choices=HYBRID_CHOICES),
            "temperature": createNumberInput(placeholder="Ideal Soil Temperature"),
            "depth": createNumberInput(placeholder="Depth"),
            "germination": createNumberInput(placeholder="Days to Germination")
        }

    def __init__(self, *args, **kwargs):
        super(CreateCropForm, self).__init__(*args, **kwargs)
        self.fields["species"] = forms.ModelChoiceField(
            queryset=Species.objects.all(),
            widget=createSelectInput("Crop species", ["font-italic"]),
        )
        self.fields["species"].empty_label = "Species"

    def saveCrop(self, request):
        crop = self.save(commit=False)
        crop.save()


def plantFormSet(plant=Plant()):
    formset = inlineformset_factory(
        Crop,
        Plant,
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

    plant = formset(instance=plant)
    if len(plant) == 1:
        plant = plant[0]
    return plant


def growFormSet(grow=Grow()):
    formset = inlineformset_factory(
        Crop,
        Grow,
        fields=[
            "sun",
            "soil"
        ],
        extra=1,
        can_delete=False,
        widgets={
            "sun": createRadioInput(choices=SUN),
            "soil": createTextInput(placeholder="Soil type")
        })

    grow = formset(instance=grow)
    if len(grow) == 1:
        grow = grow[0]
    return grow


def harvestFormSet(harvest=Harvest()):
    formset = inlineformset_factory(
        Crop,
        Harvest,
        fields=[
            "begin",
            "end",
            "variety"
        ],
        extra=1,
        can_delete=False,
        widgets={
            "begin": createNumberInput("Start Date", 1),
            "end": createNumberInput("End Date", 1),
            "variety": createRadioInput(choices=CROP_TYPE)
        }
    )

    harvest = formset(instance=harvest)
    if len(harvest) == 1:
        harvest = harvest[0]
    return harvest
