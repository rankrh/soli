from soli.views.authenticatedPageView import AuthenticatedPageView


class Home(AuthenticatedPageView):
    def get(self, request):

        self.construct(request)
        self.context["cards"] = ["overview"]

        return self.renderPage("account/home.html")
