# Generated by Django 3.1.2 on 2021-02-12 22:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aria', '0015_auto_20210210_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='harvest',
            name='begin',
            field=models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='end',
            field=models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='harvest',
            name='variety',
            field=models.CharField(choices=[('R', 'Root'), ('G', 'Leafy green'), ('F', 'Fruit'), ('N', 'Nut'), ('S', 'Seed')], default='F', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='planting',
            name='pattern',
            field=models.CharField(blank=True, choices=[('R', 'in rows'), ('M', 'in mounds'), ('P', 'in pots'), ('T', 'on trellises'), ('S', 'by scattering')], default='R', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='plantingdate',
            name='frost',
            field=models.CharField(choices=[('F', 'First frost'), ('L', 'Last frost')], default='L', max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='plantingdate',
            name='location',
            field=models.CharField(choices=[('I', 'Start inside'), ('O', 'Direct sow')], default='I', max_length=1, null=True),
        ),
    ]
