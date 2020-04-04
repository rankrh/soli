from django import forms
from ..models import Crop, Species
from .templates.templates import createTextInput, createSelectInput, createTextArea


class CreateCropForm(forms.ModelForm):

    class Meta:
        model = Crop
        fields = [
            "variety", "description"
        ]
        widgets = {
            "variety": createTextInput('Crop variety'),
            "description": createTextArea("Description")
        }

    def __init__(self, *args, **kwargs):
        super(CreateCropForm, self).__init__(*args, **kwargs)
        self.fields["species"] = forms.ModelChoiceField(
            queryset=Species.objects.all(),
            widget=createSelectInput("Crop species", ["font-italic"]),
        )

    def saveCrop(self, request):
        crop = self.save(commit=False)
        crop.species_id = request.POST["species"]
        crop.save()
