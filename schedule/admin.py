from django.contrib import admin

from schedule.models.calendar import Calendar
from schedule.models.event import Event
from schedule.models.event import EventType

admin.site.register(Calendar)
admin.site.register(Event)
admin.site.register(EventType)
