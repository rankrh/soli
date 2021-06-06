from rest_framework.response import Response
from rest_framework.views import APIView

from schedule.models.calendar import Calendar
from schedule.models.event import Event
from schedule.serializers.calendarSerializer import CalendarSerializer
from schedule.serializers.eventSerializer import EventSerializer


class CalendarView(APIView):

    farmer = None

    def get(self, request, format=None):

        self.farmer = request.user

        calendar = Calendar.objects.filter(farmer=self.farmer)

        calendar_serializer = CalendarSerializer(calendar, many=True)

        return Response(calendar_serializer.data)
