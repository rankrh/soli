from aria.forms.templates.templates import createRadioInput, createTextInput, createNumberInput, createSelectInput
from aria.models.crop import Crop
from aria.models.cropCare import CropCare
from aria.models.validation.careValidation import SUN
from django.forms import inlineformset_factory, ModelForm


class CropCareForm(ModelForm):
    class Meta:
        model = CropCare

        fields = [
            "sun",
            "soil",
            "water"
        ]

        widgets = {
            "sun": createSelectInput(),
            "soil": createTextInput(placeholder="Soil type"),
            "water": createNumberInput(placeholder="Inches of water", minimum=0)
        }

        def saveCare(self, crop):
            care = self.save(commit=False)
            care.crop = crop

            care.save()


CropCareFormSet = inlineformset_factory(Crop, CropCare, CropCareForm, extra=1)
