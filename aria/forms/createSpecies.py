from aria.models import Genus, Species
from django import forms
from .templates.templates import createTextInput, createSelectInput


class CreateSpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = ["species"]
        widgets = {"species": createTextInput("Species Name")}

    def __init__(self, *args, **kwargs):
        super(CreateSpeciesForm, self).__init__(*args, **kwargs)
        self.fields["genus"] = forms.ModelChoiceField(
            queryset=Genus.objects.all(),
            widget=createSelectInput(attrs={
                "placeholder": "Crop genus",
                "class": "font-italic"
            }),
        )

    def saveSpecies(self, request):
        species = self.save(commit=False)
        species.genus_id = request.POST["genus"]
        species.save()

