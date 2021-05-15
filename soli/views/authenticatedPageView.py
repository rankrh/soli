from django.core.exceptions import ValidationError

from farm.models.farm import Farm
from soli.views.pageView import PageView


class AuthenticatedPageView(PageView):
    def construct(self, request):
        super().construct(request)

        if not self.userIsAuthenticated():
            raise ValidationError("Unauthenticated User")

    def userIsAuthenticated(self):
        return self.user.id is not None

    def renderPage(self, page):
        if self.userIsAuthenticated():
            farms = Farm.objects.filter(owner=self.user)

            self.context["user"] = self.user
            self.context["farms"] = farms

            return super().renderPage(page)
