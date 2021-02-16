from django.forms import ModelForm, inlineformset_factory, ChoiceField

from aria.forms.templates.templates import createSelectInput, createNumberInput
from aria.models.crop import Crop
from aria.models.plantingDate import PlantingDate


class PlantingDateForm(ModelForm):
    beforeOrAfter = ChoiceField(
        choices=[
            (-1,  "Before"),
            (1, "After")
        ],
        required=False,
        widget=createSelectInput()
    )

    class Meta:
        model = PlantingDate
        fields = [
            "frost",
            "date",
            "location",
            "transplant"
        ]

        widgets = {
            "frost": createSelectInput(),
            "date": createNumberInput(None, minimum=0),
            "location": createSelectInput(attrs={"onchange": "updateLocation();"}),
            "transplant": createNumberInput("Weeks", minimum=0),
        }

    def getBeforeOrAfter(self):

        beforeOrAfter = self.cleaned_data["beforeOrAfter"]

        try:
            beforeOrAfter = int(beforeOrAfter)
        except:
            beforeOrAfter = 0

        return beforeOrAfter


    def savePlantingDate(self, crop):

        plantingDate = self.save(commit=False)
        plantingDate.crop = crop
        plantingDate.date *= self.getBeforeOrAfter()

        plantingDate.save()


PlantingDateFormSet = inlineformset_factory(Crop, PlantingDate, PlantingDateForm, extra=1)
