# Generated by Django 3.2.2 on 2021-05-23 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("crop", "0003_auto_20210517_1045"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="crop",
            name="company",
        ),
    ]
