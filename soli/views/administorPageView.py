from soli.views.authenticatedPageView import AuthenticatedPageView


class AdministratorPageView(AuthenticatedPageView):
    def is_authorized(self):
        return self.user is not None and self.user.is_staff
