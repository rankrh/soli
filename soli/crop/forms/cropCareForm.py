from django.forms import inlineformset_factory, ModelForm

from crop.models.crop import Crop
from crop.models.cropCare import CropCare
from formTemplates.inputFields import createTextInput, createNumberInput


class CropCareForm(ModelForm):
    class Meta:
        model = CropCare

        fields = [
            "sunMin",
            "sunMax",
            "soil",
            "water"
        ]

        widgets = {
            "sunMin": createNumberInput(minimum=0, maximum=24),
            "sunMax": createNumberInput(minimum=0, maximum=24),
            "soil": createTextInput(placeholder="Soil type"),
            "water": createNumberInput(placeholder="Inches of water", minimum=0)
        }

    def saveCare(self, crop):
        care = self.save(commit=False)
        care.crop = crop

        care.save()


CropCareFormSet = inlineformset_factory(Crop, CropCare, CropCareForm, extra=1)
