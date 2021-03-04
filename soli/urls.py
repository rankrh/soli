from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from soli import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include("account.urls")),
    path("plot/", include("plot.urls")),
    path("myfarms/", include("farm.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
