from django.shortcuts import render
from django.views import View


class PageView(View):
    request = None
    context = {}
    page = None
    user = None

    def construct(self, request):
        self.request = request
        self.user = self.request.user

    def renderPage(self, page):
        return render(self.request, page, self.context)
