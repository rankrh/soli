from django.forms import inlineformset_factory, ModelForm

from crop.models.crop import Crop
from crop.models.harvest import Harvest
from formTemplates.inputFields import createNumberInput, createSelectInput


class HarvestForm(ModelForm):
    class Meta:
        model = Harvest

        fields = [
            "begin",
            "end",
            "variety"
        ]

        widgets = {
            "begin": createNumberInput(minimum=1),
            "end": createNumberInput(minimum=1),
            "variety": createSelectInput()
        }

    def saveHarvest(self, crop):
        harvest = self.save(commit=False)
        harvest.crop = crop

        harvest.save()


HarvestFormSet = inlineformset_factory(Crop, Harvest, HarvestForm, extra=1)
