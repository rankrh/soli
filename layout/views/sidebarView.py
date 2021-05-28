from rest_framework.response import Response
from rest_framework.views import APIView

from layout.models.sidebar import Sidebar
from layout.serializers.sidebarSerializer import SidebarSerializer


class SidebarView(APIView):
    def get(self, request, format=None):

        sidebar_serializer = SidebarSerializer(Sidebar(request.user))
        return Response(sidebar_serializer.data)
