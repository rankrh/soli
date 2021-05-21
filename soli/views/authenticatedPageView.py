from django.core.exceptions import ValidationError

from farm.models.farm import Farm
from soli.views.pageView import PageView
from soli.views.sidebar import Sidebar


class AuthenticatedPageView(PageView):
    user = None
    farms = None

    def construct(self, request):
        super().construct(request)
        if not self.is_authorized():
            raise ValidationError("Unauthenticated User")

        self.set_farms()
        self.define_context()
        self.set_sidebar_sections()

    def is_authorized(self):
        return self.user is not None and self.user.id is not None

    def render(self, page):
        if self.is_authorized():
            return super().render(page)
        else:
            return super().render("error.html")

    def redirect(self, page):
        if self.is_authorized():
            return super().redirect(page)
        else:
            return self.renderErrorPage()

    def define_context(self):
        self.context["user"] = self.user
        self.context["farms"] = self.farms

    def set_sidebar_sections(self):
        self.context["sidebar"] = Sidebar(self)

    def set_farms(self):
        self.farms = Farm.objects.filter(owner=self.user)
