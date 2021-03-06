from django import forms
from django.forms import inlineformset_factory

from formTemplates.inputFields import createTextInput, createSelectInput, createTextArea
from taxonomy.models.genus import Genus
from taxonomy.models.species import Species
from taxonomy.models.subspecies import Subspecies


class CreateSpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = ["name", "common_name", "description"]
        widgets = {
            "name": createTextInput("Species"),
            "common_name": createTextInput("Common Name"),
            "description": createTextArea("Description"),
        }

    def __init__(self, *args, **kwargs):
        super(CreateSpeciesForm, self).__init__(*args, **kwargs)
        self.fields["genus"] = forms.ModelChoiceField(
            queryset=Genus.objects.all().order_by("name"),
            widget=createSelectInput("Genus", ["font-italic"]),
        )

        self.fields["genus"].empty_label = "Genus"

    def saveSpecies(self, request):
        species = self.save(commit=False)
        species.genus = Genus(id=request.POST["genus"])
        species.save()


def subspeciesFormSet(species=Species()):
    formset = inlineformset_factory(
        Species,
        Subspecies,
        fields=["name"],
        extra=1,
        can_delete=False,
        widgets={"name": createTextInput("Subspecies")},
    )

    subspecies = formset(instance=species)
    if len(subspecies) == 1:
        subspecies = subspecies[0]
    return subspecies
