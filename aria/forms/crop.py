from aria.models.validation.plant import GROW_STYLE
from django import forms
from ..models import Crop, Species, Plant, Grow, Harvest
from .templates.templates import createTextInput, createSelectInput, createTextArea, createNumberInput
from django.forms import inlineformset_factory


class CropForm(forms.Form):
    variety = forms.CharField(widget=createTextInput('Crop variety'))
    species = forms.ModelChoiceField(
            queryset=Species.objects.all(),
            widget=createSelectInput("Crop species", ["font-italic"]),
        )
    description = forms.CharField(widget=createTextArea("Description"))
    germination = forms.IntegerField(widget=createNumberInput("Days to Germination"))
    depth = forms.IntegerField(widget=createNumberInput("Seed depth"))
    temperature = forms.IntegerField(widget=createNumberInput("Ideal temperature"))
    pattern = forms.ChoiceField(widget=createSelectInput("Sowing Pattern", GROW_STYLE))
    spacing = forms.IntegerField(widget=createNumberInput("Spacing"))
    maturity = forms.IntegerField(widget=createNumberInput("Days to Maturity"))

    def saveCrop(self, request):
        crop = self.save(commit=False)
        crop.species_id = request.POST["species"]
        crop.save()


