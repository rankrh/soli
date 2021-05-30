from soli.views.authenticatedPageView import AuthenticatedPageView


class Home(AuthenticatedPageView):
    def get(self, request):

        self.construct(request)
        self.context["cards"] = ["overview"]

        return self.render("account/home.html")

    def getAPI(self, request, format=None):

        self.user = request.user
        # user_serializer = UserSerializer(self.user, many=False)

        # return Response(user_serializer.data)
