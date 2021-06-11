from rest_framework.response import Response
from rest_framework.views import APIView

from crop.serializers.cropFormSerializer import CropFormSerializer


class CropForm(APIView):
    def get(self, request, format=None):

        crop_form_serializer = CropFormSerializer()

        return Response(crop_form_serializer.data)
