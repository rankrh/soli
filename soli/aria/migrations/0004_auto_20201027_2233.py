# Generated by Django 3.0.6 on 2020-10-28 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aria', '0003_auto_20201027_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='sp_ge_num',
            field=models.ForeignKey(db_column='sp_ge_num', on_delete=django.db.models.deletion.CASCADE, to='aria.Genus'),
        ),
    ]
