# Generated by Django 3.1.2 on 2021-02-10 03:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aria', '0011_remove_harvest_plant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planting',
            name='date',
        ),
        migrations.RemoveField(
            model_name='planting',
            name='frost',
        ),
        migrations.RemoveField(
            model_name='planting',
            name='location',
        ),
        migrations.RemoveField(
            model_name='planting',
            name='transplant',
        ),
        migrations.AlterField(
            model_name='planting',
            name='interRowSpacing',
            field=models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='planting',
            name='pattern',
            field=models.CharField(blank=True, choices=[('R', 'in rows'), ('M', 'in mounds'), ('P', 'in pots'), ('T', 'on trellises'), ('S', 'by scattering')], default=None, max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='planting',
            name='rowSpacing',
            field=models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterModelTable(
            name='planting',
            table=None,
        ),
        migrations.CreateModel(
            name='PlantingDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frost', models.CharField(blank=True, choices=[('F', 'First frost'), ('L', 'Last frost')], max_length=1, null=True)),
                ('date', models.SmallIntegerField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('location', models.CharField(blank=True, choices=[('I', 'Start inside'), ('O', 'Direct sow')], default=None, max_length=1, null=True)),
                ('transplant', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(52)])),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.crop')),
            ],
        ),
    ]
