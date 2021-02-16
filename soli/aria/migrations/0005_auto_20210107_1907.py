# Generated by Django 3.1.2 on 2021-01-08 02:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aria', '0004_auto_20201228_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planting',
            old_name='spacing',
            new_name='interRowSpacing',
        ),
        migrations.AddField(
            model_name='planting',
            name='rowSpacing',
            field=models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
            preserve_default=False,
        ),
    ]