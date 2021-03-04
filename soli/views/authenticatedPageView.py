from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.views import View

from farm.models.farm import Farm


class AuthenticatedPageView(View):

    request = None
    context = {}
    page = None
    user = None

    def construct(self, request):
        self.request = request
        self.user = self.request.user

        if not self.userIsAuthenticated():
            raise ValidationError

    def userIsAuthenticated(self):
        return self.user.id is not None

    def renderPage(self, page):
        if self.userIsAuthenticated():
            farms = Farm.objects.filter(owner=self.user)

            self.context["user"] = self.user,
            self.context["farms"] = farms

            return render(self.request, page, self.context)
