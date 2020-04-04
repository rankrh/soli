# Generated by Django 3.0.3 on 2020-04-04 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aria', '0017_auto_20200403_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='harvest',
            name='form',
            field=models.CharField(choices=[('R', 'Root'), ('G', 'Leafy green'), ('F', 'Fruit'), ('N', 'Nut'), ('S', 'Seed'), ('L', 'Legume')], max_length=1, null=True),
        ),
    ]