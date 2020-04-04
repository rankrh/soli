from aria.models import Genus, Species, Subspecies
from django import forms
from django.forms import inlineformset_factory

from .templates.templates import createTextInput, createSelectInput


class CreateSpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = ["species", "common_name"]
        widgets = {
            "species": createTextInput("Species"),
            "common_name": createTextInput("Common Name")
        }

    def __init__(self, *args, **kwargs):
        super(CreateSpeciesForm, self).__init__(*args, **kwargs)
        self.fields["genus"] = forms.ModelChoiceField(
            queryset=Genus.objects.all().order_by("genus"),
            widget=createSelectInput("Genus", ["font-italic"]))

        self.fields["genus"].empty_label = "Genus"

    def saveSpecies(self, request):
        species = self.save(commit=False)
        species.genus_id = request.POST["genus"]
        species.save()


def subspeciesFormSet(species=Species()):
    formset = inlineformset_factory(
        Species,
        Subspecies,
        fields=["subspecies"],
        extra=1,
        can_delete=False,
        widgets={
            "subspecies": createTextInput("Subspecies")
        })

    subspecies = formset(instance=species)
    if len(subspecies) == 1:
        subspecies = subspecies[0]
    return subspecies
