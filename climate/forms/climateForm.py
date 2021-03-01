from django import forms

from climate.models.climate import Climate
from formTemplates.inputFields import createSelectInput, createDateInput


class ClimateForm(forms.ModelForm):

    class Meta:
        model = Climate
        fields = [
            "zone",
            "firstFrost",
            "lastFrost"
        ]

        widgets = {
            "zone": createSelectInput(),
            "firstFrost": createDateInput(placeholder="First Frost"),
            "lastFrost": createDateInput(placeholder="Last Frost"),
        }

    def setFrostDates(self):
        self.data = self.data.copy()
        self.data["firstFrost"] += "/1900"
        self.data["lastFrost"] += "/1900"

    def saveClimate(self, farm):

        climate = self.save(commit=False)
        climate.farm = farm

        climate.save()

        return climate
