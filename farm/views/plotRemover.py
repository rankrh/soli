import json

from django.http import JsonResponse

from farm.models.plot import Plot
from soli.views.authenticatedPageView import AuthenticatedPageView


class PlotRemover(AuthenticatedPageView):
    def get(self, request):
        self.construct(request)
        pass

    def post(self, request, slug):
        response = {"errors": []}

        self.construct(request)
        plots = json.loads(self.request.POST["plots"])
        deleted, rows = Plot.objects.filter(
            id__in=plots, owner=self.user, farm=self.request.POST["farm"]
        ).delete()

        if rows == 0:
            response["errors"] += f"Could not delete plots: {plots}"

        return JsonResponse(response)
