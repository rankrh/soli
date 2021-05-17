from django.core.exceptions import ValidationError

from farm.models.farm import Farm
from soli.views.pageView import PageView


class AuthenticatedPageView(PageView):
    def construct(self, request):
        super().construct(request)

        if not self.isAuthorized():
            raise ValidationError("Unauthenticated User")

    def isAuthorized(self):
        return self.user is not None and self.user.id is not None

    def render(self, page):
        if self.isAuthorized():
            farms = Farm.objects.filter(owner=self.user)

            self.context["user"] = self.user
            self.context["farms"] = farms

            return super().render(page)
        else:
            return super().render("error.html")

    def redirect(self, page):
        if self.isAuthorized():
            return super().redirect(page)
        else:
            return self.renderErrorPage()
