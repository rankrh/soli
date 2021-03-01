from django import forms
from django.core.exceptions import ValidationError

from farm.models.farm import Farm
from formTemplates.inputFields import createImageUpload, createTextInput, createYearInput, createTextArea
from geometry.models.point import Point


class FarmForm(forms.ModelForm):
    location = None
    owner = None

    class Meta:
        model = Farm
        fields = [
            "name",
            "logo",
            "year",
            "description"
        ]

        widgets = {
            "name": createTextInput(placeholder="Farm Name", id="plot-name"),
            "logo": createImageUpload(id="plot-logo"),
            "year": createYearInput(),
            "description": createTextArea()
        }

    def saveFarm(self, climate):
        farm = self.save(commit=False)
        farm.location = self.location
        farm.owner = self.owner
        farm.climate = climate
        farm.save()

        return farm

    def setFarmHeadquarters(self):
        coordinates = self.getCoordinates()
        if len(coordinates) == 2:
            self.location = Point(lat=coordinates[0], long=coordinates[1])
            self.location.save()

    def getCoordinates(self):
        try:
            coordinates = [float(coord) for coord in self.data["location"].split(",")]
        except Exception as e:
            coordinates = []
            print(e)

        return coordinates
