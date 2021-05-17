from soli.views.authenticatedPageView import AuthenticatedPageView


class Herd(AuthenticatedPageView):
    def get(self, request):
        self.construct(request)

        return self.render("herd.html")

    def post(self, request):
        self.construct(request)
