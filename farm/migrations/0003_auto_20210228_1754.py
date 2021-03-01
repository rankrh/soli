# Generated by Django 3.1.2 on 2021-03-01 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('climate', '0003_auto_20210227_1900'),
        ('geometry', '0002_auto_20210227_1953'),
        ('farm', '0002_auto_20210227_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='climate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='climate.climate'),
        ),
        migrations.AlterField(
            model_name='farm',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geometry.point'),
        ),
    ]
