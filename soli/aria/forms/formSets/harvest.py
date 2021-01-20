from aria.forms.templates.templates import createNumberInput, createRadioInput, createSelectInput
from aria.models.crop import Crop
from aria.models.harvest import Harvest
from django.forms import inlineformset_factory, ModelForm


class HarvestForm(ModelForm):
    class Meta:
        model = Harvest

        fields = [
            "begin",
            "end",
            "variety"
        ]

        widgets = {
            "begin": createNumberInput(1),
            "end": createNumberInput(1),
            "variety": createSelectInput()
        }

    def saveHarvest(self, crop):
        harvest = self.save(commit=False)
        harvest.crop = crop

        harvest.save()


HarvestFormSet = inlineformset_factory(Crop, Harvest, HarvestForm, extra=1)
