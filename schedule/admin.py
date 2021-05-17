from django.contrib import admin

from schedule.models.calendar import Calendar
from schedule.models.event import Event

admin.site.register(Calendar)
admin.site.register(Event)
