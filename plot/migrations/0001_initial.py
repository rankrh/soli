# Generated by Django 3.1.2 on 2021-02-25 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farm', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('geometry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Unnamed Plot', max_length=128)),
                ('description', models.CharField(blank=True, default='', max_length=1024)),
                ('type', models.CharField(blank=True, choices=[('F', 'field'), ('W', 'forest'), ('G', 'garden'), ('O', 'orchard'), ('P', 'pasture'), ('S', 'silvopasture')], default=None, max_length=1, null=True)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm.farm')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='plot.plot')),
                ('shape', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='geometry.shape')),
            ],
            options={
                'db_table': 'plot',
            },
        ),
    ]