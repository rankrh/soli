from soli.views.authenticatedPageView import AuthenticatedPageView


class AdministratorPageView(AuthenticatedPageView):
    def isAuthorized(self):
        return self.user is not None and self.user.is_staff
