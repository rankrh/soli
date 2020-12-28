from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from aria.forms.farm import CreateFarmForm
from aria.models.farm import Farm


def createFarm(request):

    current_user = request.user
    context = {
        "farmForm": CreateFarmForm()
    }

    if request.is_ajax():
        if request.method == "POST":
            farm = Farm(
                name=request.POST["name"],
                logo=request.POST["logo"],
                owner=current_user
            )

            farm.save()
            response = {"plot": farm.id}

            return JsonResponse(response)

        elif request.method == "GET":
            html = render_to_string("aria/create/farm.html", context)
            return HttpResponse(html)
    else:
        return render(request, "aria/create/farm.html", context)
