# Generated by Django 3.1.2 on 2020-12-23 14:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Climate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('zone', models.CharField(max_length=2)),
                ('firstFrost', models.DateField()),
                ('lastFrost', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(null=True)),
                ('company', models.CharField(max_length=30, null=True)),
                ('organic', models.BooleanField(null=True)),
                ('treated', models.BooleanField(null=True)),
                ('hybrid', models.BooleanField(null=True)),
            ],
            options={
                'db_table': 'crop',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('details', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('climate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aria.climate')),
            ],
        ),
        migrations.CreateModel(
            name='Genus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'db_table': 'genus',
            },
        ),
        migrations.CreateModel(
            name='GrowPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sun', models.CharField(blank=True, choices=[('F', 'Full sun'), ('P', 'Part sun'), ('S', 'Shade')], default=None, max_length=1, null=True)),
                ('soil', models.CharField(blank=True, max_length=30, null=True)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.crop')),
            ],
            options={
                'db_table': 'growPlan',
            },
        ),
        migrations.CreateModel(
            name='Livestock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'livestock',
            },
        ),
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Unnamed Plot', max_length=128)),
                ('description', models.CharField(blank=True, default='', max_length=1024)),
                ('type', models.CharField(blank=True, choices=[('F', 'field'), ('W', 'forest'), ('G', 'garden'), ('O', 'orchard'), ('P', 'pasture'), ('S', 'silvopasture')], default=None, max_length=1, null=True)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.farm')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aria.plot')),
            ],
            options={
                'db_table': 'plot',
            },
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('M', 'Marker'), ('L', 'Line'), ('P', 'Polygon')], default=None, max_length=1, null=True)),
                ('area', models.FloatField(blank=True, null=True)),
                ('length', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'shape',
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('common_name', models.CharField(max_length=30, null=True)),
                ('genus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.genus')),
            ],
            options={
                'db_table': 'species',
                'unique_together': {('id', 'genus')},
            },
        ),
        migrations.CreateModel(
            name='Silvopasture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.plot')),
            ],
            options={
                'db_table': 'silvopasture',
            },
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('set', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('shape', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='aria.shape')),
            ],
            options={
                'db_table': 'point',
            },
        ),
        migrations.AddField(
            model_name='plot',
            name='shape',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='aria.shape'),
        ),
        migrations.CreateModel(
            name='PlantingPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern', models.CharField(choices=[('R', 'Row'), ('M', 'Mound'), ('P', 'Pot'), ('T', 'Trellis'), ('S', 'Scatter')], default=None, max_length=1)),
                ('spacing', models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('frost', models.CharField(choices=[('F', 'First frost'), ('L', 'Last frost')], default=None, max_length=1)),
                ('date', models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('location', models.CharField(choices=[('I', 'Start inside'), ('O', 'Direct sow')], default=None, max_length=1)),
                ('temperature', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(-50), django.core.validators.MaxValueValidator(50)])),
                ('germination', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(365)])),
                ('depth', models.SmallIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)])),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.crop')),
                ('transplant', models.ForeignKey(blank=True, db_column='pl_transplant', null=True, on_delete=django.db.models.deletion.CASCADE, to='aria.plantingplan')),
            ],
            options={
                'db_table': 'plantingPlan',
            },
        ),
        migrations.CreateModel(
            name='Pasture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stockrate', models.FloatField()),
                ('livestock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.livestock')),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.plot')),
            ],
            options={
                'db_table': 'pasture',
            },
        ),
        migrations.CreateModel(
            name='Orchard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.plot')),
            ],
            options={
                'db_table': 'orchard',
            },
        ),
        migrations.AddField(
            model_name='livestock',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.species'),
        ),
        migrations.CreateModel(
            name='HarvestPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.IntegerField(default=None, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('end', models.IntegerField(default=None, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('variety', models.CharField(choices=[('R', 'Root'), ('G', 'Leafy green'), ('F', 'Fruit'), ('N', 'Nut'), ('S', 'Seed'), ('L', 'Legume')], default=None, max_length=1, null=True)),
                ('crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.crop')),
                ('grow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.growplan')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.plantingplan')),
            ],
            options={
                'db_table': 'harvestPlan',
            },
        ),
        migrations.AddField(
            model_name='growplan',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.plantingplan'),
        ),
        migrations.CreateModel(
            name='Garden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.plot')),
            ],
            options={
                'db_table': 'garden',
            },
        ),
        migrations.CreateModel(
            name='Forest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.plot')),
            ],
            options={
                'db_table': 'forest',
            },
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.plot')),
            ],
            options={
                'db_table': 'field',
            },
        ),
        migrations.AddField(
            model_name='farm',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.point'),
        ),
        migrations.AddField(
            model_name='farm',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='crop',
            name='species',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.species'),
        ),
        migrations.CreateModel(
            name='Subspecies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aria.species')),
            ],
            options={
                'db_table': 'subspecies',
                'unique_together': {('id', 'species')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='crop',
            unique_together={('id', 'species')},
        ),
    ]
