# Generated by Django 2.2.7 on 2019-11-24 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aria', '0005_crop'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('plotId', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.FloatField()),
                ('crop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='aria.Crop')),
                ('garden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.Plot')),
            ],
            options={
                'db_table': 'plot',
            },
        ),
        migrations.CreateModel(
            name='PlotCoordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X', models.FloatField()),
                ('Y', models.FloatField()),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.Plot')),
            ],
            options={
                'db_table': 'plotCoordinate',
            },
        ),
        migrations.CreateModel(
            name='GrowingStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('growingStyle', models.CharField(choices=[('R', 'Row'), ('M', 'Mound'), ('P', 'Pot'), ('T', 'Trellis')], max_length=1)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.Crop')),
            ],
            options={
                'db_table': 'growingStyle',
            },
        ),
        migrations.CreateModel(
            name='CropType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cropType', models.CharField(choices=[('R', 'Root'), ('G', 'Leafy green'), ('F', 'Fruit'), ('N', 'Nut'), ('S', 'Seed'), ('L', 'Legume')], max_length=2)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.Crop')),
            ],
            options={
                'db_table': 'cropType',
            },
        ),
        migrations.CreateModel(
            name='CropPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X', models.FloatField()),
                ('Y', models.FloatField()),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.Plot')),
            ],
            options={
                'db_table': 'cropPosition',
            },
        ),
    ]