from crop.models.crop import Crop
from soli.views.administorPageView import AdministratorPageView
from taxonomy.models.species import Species


class CropDetails(AdministratorPageView):
    def get(self, request):
        self.construct(request)
        self.context["crops"] = Crop.objects.all()
        self.context["species"] = Species.objects.filter(genus__kingdom="P")

        return self.render("list_crops.html")
