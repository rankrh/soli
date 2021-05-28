from django.urls import path

from layout.views.sidebarView import SidebarView

urlpatterns = [
    path("sidebar/", SidebarView.as_view(), name="sidebar"),
]
