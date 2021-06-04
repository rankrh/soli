from django.db.models import CASCADE

from django.contrib.auth.models import User
from django.db import models


class Calendar(models.Model):
    class Meta:
        db_table = "calendar"
        app_label = "schedule"

    farmer = models.OneToOneField(User, on_delete=CASCADE)
