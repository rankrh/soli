from django.shortcuts import render

from farm.models.farm import Farm


def renderPage(request, pageName, context={}):

    farms = []
    user = request.user
    if user.id:
        farms = Farm.objects.filter(owner=user)

    context = {
        **{
            "user": user,
            "farms": farms},
        ** context
    }

    return render(request, pageName, context)