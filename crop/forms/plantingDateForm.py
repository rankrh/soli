from django.forms import ModelForm, inlineformset_factory, ChoiceField

from crop.models.crop import Crop
from crop.models.plantingDate import PlantingDate
from formTemplates.inputFields import createSelectInput, createNumberInput


class PlantingDateForm(ModelForm):
    beforeOrAfter = ChoiceField(
        choices=[(-1, "Before"), (1, "After")],
        required=False,
        widget=createSelectInput(),
    )

    class Meta:
        model = PlantingDate
        fields = ["frost", "date", "location", "transplant"]

        widgets = {
            "frost": createSelectInput(),
            "date": createNumberInput(None, minimum=0),
            "location": createSelectInput(attrs={"onchange": "updateLocation();"}),
            "transplant": createNumberInput("Weeks", minimum=0),
        }

    def getBeforeOrAfter(self):

        beforeOrAfter = self.cleaned_data["beforeOrAfter"]

        beforeOrAfter = int(beforeOrAfter)

        return beforeOrAfter

    def savePlantingDate(self, crop):

        plantingDate = self.save(commit=False)
        plantingDate.date *= self.getBeforeOrAfter()

        plantingDate.save()
