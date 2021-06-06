# Generated by Django 3.2.4 on 2021-06-06 05:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Shape",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("M", "Marker"), ("L", "Line"), ("P", "Polygon")],
                        default=None,
                        max_length=1,
                        null=True,
                    ),
                ),
                ("area", models.FloatField(blank=True, null=True)),
                ("length", models.FloatField(blank=True, null=True)),
            ],
            options={
                "db_table": "shape",
            },
        ),
        migrations.CreateModel(
            name="Point",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                (
                    "set",
                    models.IntegerField(
                        default=0,
                        validators=[django.core.validators.MinValueValidator(0)],
                    ),
                ),
                ("lat", models.FloatField()),
                ("long", models.FloatField()),
                (
                    "shape",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="geometry.shape",
                    ),
                ),
            ],
            options={
                "db_table": "point",
            },
        ),
    ]
