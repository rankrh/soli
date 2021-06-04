from rest_framework.response import Response
from rest_framework.views import APIView


class Calendar(APIView):

    farmer = None

    def get(self, request, format=None):

        self.farmer = request.farmer

        calendar = Calendar.objects.filter(farmer=self.farmer).get()
        calendar_serializer = Calendar(calendar, many=True)

        return Response(calendar_serializer.data)
