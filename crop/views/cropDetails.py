from crop.models.crop import Crop
from soli.views.administorPageView import AdministratorPageView


class CropDetails(AdministratorPageView):
    def get(self, request):
        self.construct(request)
        self.context["crops"] = Crop.objects.all()

        return self.render("list_crops.html")
