# Generated by Django 4.1 on 2022-12-01 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_technician_workweek'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='workweek',
            constraint=models.UniqueConstraint(fields=('monday', 'tuesday', 'wedesday', 'thursday', 'friday', 'saturday', 'sunday'), name='unique_weeks'),
        ),
    ]
