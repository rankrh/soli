from rest_framework.response import Response
from rest_framework.views import APIView

from farm.models.farm import Farm
from farm.serializers.farmSerializer import FarmSerializer


class FarmApi(APIView):
    user = None

    def get(self, request, format=None):

        self.user = request.user

        farms = Farm.objects.filter(owner=self.user)
        farm_serializer = FarmSerializer(farms, many=True)

        return Response(farm_serializer.data)
