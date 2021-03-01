from django.http import HttpResponseRedirect
from django.views import View

from climate.forms.climateForm import ClimateForm
from farm.forms.farmForm import FarmForm

from soli.pageRender import renderPage


class FarmCreator(View):
    farm = None
    climate = None
    request = None
    user = None
    location = []
    context = {}

    def get(self, request):
        self.request = request

        if self.request.user.id is not None:
            self.context = {
                "farmForm": FarmForm(),
                "climateForm": ClimateForm()
            }
        return renderPage(request, "createFarm.html", self.context)

    def post(self, request):
        self.request = request

        if self.request.user.id is not None:
            self.createFarm()
            self.createFarmClimate()

            if self.farmDataIsValid():
                self.saveAllFarmData()

        return HttpResponseRedirect("/")

    def farmDataIsValid(self):
        return self.farm.is_valid() and self.climate.is_valid()

    def saveAllFarmData(self):
        self.climate = self.climate.saveClimate(self.farm)
        self.farm = self.farm.saveFarm(self.climate)

    def createFarmClimate(self):
        self.climate = ClimateForm(self.request.POST)
        self.climate.setFrostDates()

    def createFarm(self):
        self.farm = FarmForm(self.request.POST)
        self.farm.setFarmHeadquarters()
        self.farm.owner = self.request.user
