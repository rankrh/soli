from aria.models import Genus, Species
from django import forms
from .templates.templates import createTextInput, createSelectInput


class CreateSpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = ["species", "common_name"]
        widgets = {
            "species": createTextInput("Species"),
            "common_name": createTextInput("Subspecies")
        }

    def __init__(self, *args, **kwargs):
        super(CreateSpeciesForm, self).__init__(*args, **kwargs)
        self.fields["genus"] = forms.ModelChoiceField(
            queryset=Genus.objects.all().order_by("genus"),
            widget=createSelectInput(attrs={
                "placeholder": "Genus",
                "class": "font-italic",
            }))

        self.fields["genus"].empty_label = "Genus"

    def saveSpecies(self, request):
        species = self.save(commit=False)
        species.genus_id = request.POST["genus"]
        species.save()

