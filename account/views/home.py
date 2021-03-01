from soli.pageRender import renderPage


def home(request):

    return renderPage(request, "account/home.html")
