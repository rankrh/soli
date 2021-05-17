from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from soli import settings

urlpatterns = [
    path("", include("account.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("plot/", include("plot.urls")),
    path("myfarms/", include("farm.urls")),
    path("calendar/", include("schedule.urls")),
    path("seedbank/", include("seedbank.urls")),
    path("herd/", include("herd.urls")),
    path("admin/crop/", include("crop.urls")),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
