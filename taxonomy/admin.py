from django.contrib import admin

from taxonomy.models.genus import Genus
from taxonomy.models.species import Species
from taxonomy.models.subspecies import Subspecies


admin.site.register(Genus)
admin.site.register(Species)
admin.site.register(Subspecies)