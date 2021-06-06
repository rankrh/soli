from django import forms

from climate.models.climate import Climate
from formTemplates.inputFields import createSelectInput, createDateInput


class ClimateForm(forms.ModelForm):
    class Meta:
        model = Climate
        fields = [
            "zone",
        ]

        widgets = {
            "zone": createSelectInput(),
        }

    def setFrostDates(self):
        self.data = self.data.copy()

    def saveClimate(self, farm):

        climate = self.save(commit=False)
        climate.farm = farm

        climate.save()

        return climate
