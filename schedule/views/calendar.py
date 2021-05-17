from soli.views.authenticatedPageView import AuthenticatedPageView


class Calendar(AuthenticatedPageView):
    def get(self, request):
        self.construct(request)

        return self.render("calendar.html")

    def post(self):
        pass
