from aria.models import Genus, Species, Subspecies
from django import forms
from django.forms import inlineformset_factory

from .templates.templates import createTextInput, createSelectInput


class CreateSpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = ["sp_name", "sp_common_name"]
        widgets = {
            "sp_name": createTextInput("Species"),
            "sp_common_name": createTextInput("Common Name")
        }

    def __init__(self, *args, **kwargs):
        super(CreateSpeciesForm, self).__init__(*args, **kwargs)
        self.fields["ge_num"] = forms.ModelChoiceField(
            queryset=Genus.objects.all().order_by("ge_name"),
            widget=createSelectInput("Genus", ["font-italic"]))

        self.fields["ge_num"].empty_label = "Genus"

    def saveSpecies(self, request):
        species = self.save(commit=False)
        species.sp_ge_num = Genus(ge_num=request.POST["ge_num"])
        species.save()


def subspeciesFormSet(species=Species()):
    formset = inlineformset_factory(
        Species,
        Subspecies,
        fields=["sub_name"],
        extra=1,
        can_delete=False,
        widgets={
            "sub_name": createTextInput("Subspecies")
        })

    subspecies = formset(instance=species)
    if len(subspecies) == 1:
        subspecies = subspecies[0]
    return subspecies
