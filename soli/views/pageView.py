from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class PageView(View):
    def construct(self, request):
        self.request = request
        self.user = self.request.user
        self.context = {}

    def render(self, page):
        return render(self.request, page, self.context)

    def redirect(self, page):
        return HttpResponseRedirect(page)

    def renderErrorPage(self):
        pass
