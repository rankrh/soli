from django.shortcuts import render
from django.views import View


class FarmDisplay(View):
    request = None
    context = {}

    def get(self, request):
        self.request = request

        if self.request.user.id is not None:
            self.context = {
                "farms": 1,
                "farmDetails": 1,
            }
        return render(request, "createFarm.html", self.context)

