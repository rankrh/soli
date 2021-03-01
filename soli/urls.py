from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include("account.urls")),
    path("plot/", include("plot.urls")),
    path("farm/", include("farm.urls"))
]
