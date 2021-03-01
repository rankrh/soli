from django.contrib import admin

from climate.models.climate import Climate
from farm.models.farm import Farm

admin.site.register(Climate)
admin.site.register(Farm)