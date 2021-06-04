from rest_framework.response import Response
from rest_framework.views import APIView

from farm.models.farm import Farm
from farm.serializers.farmSerializer import FarmSerializer


class FarmApi(APIView):
    farmer = None

    def get(self, request, format=None):

        self.farmer = request.farmer

        farms = Farm.objects.filter(farmer=self.farmer)
        farm_serializer = FarmSerializer(farms, many=True)

        return Response(farm_serializer.data)
