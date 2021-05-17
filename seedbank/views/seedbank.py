from soli.views.authenticatedPageView import AuthenticatedPageView


class Seedbank(AuthenticatedPageView):
    def get(self, request):
        self.construct(request)

        return self.render("seedbank.html")

    def post(self, request):
        self.construct(request)
