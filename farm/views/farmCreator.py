from django.http import HttpResponseRedirect

from climate.forms.climateForm import ClimateForm
from farm.forms.farmForm import FarmForm

from soli.views.authenticatedPageView import AuthenticatedPageView


class FarmCreator(AuthenticatedPageView):
    farm = None
    climate = None
    request = None
    user = None
    location = []
    context = {}

    def get(self, request):
        self.construct(request)

        if self.request.user.id is not None:
            self.context["farmForm"] = FarmForm()
            self.context["climateForm"] = ClimateForm()
        return self.render("createFarm.html")

    def post(self, request):
        self.construct(request)

        if self.request.user.id is not None:
            self.createFarm()
            self.createFarmClimate()

            if self.farm.is_valid():
                self.saveAllFarmData()

        return HttpResponseRedirect("/")

    def farmDataIsValid(self):

        valid = self.farm.is_valid() and self.climate.is_valid()

        if not valid:
            print(self.farm.errors)
            print(self.climate.errors)

        return valid

    def saveAllFarmData(self):
        self.climate = self.climate.saveClimate(self.farm)
        self.farm = self.farm.saveFarm(self.climate)

    def createFarmClimate(self):
        self.climate = ClimateForm(self.request.POST)
        self.climate.setFrostDates()

    def createFarm(self):
        self.farm = FarmForm(self.request.POST)
        self.farm.setFarmHeadquarters()
        self.farm.farmer = self.request.user
