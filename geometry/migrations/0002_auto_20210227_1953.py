# Generated by Django 3.1.2 on 2021-02-28 02:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geometry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='order',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='point',
            name='set',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]