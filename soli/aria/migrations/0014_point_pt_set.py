# Generated by Django 3.1.2 on 2020-12-07 01:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aria', '0013_auto_20201205_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='pt_set',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]
