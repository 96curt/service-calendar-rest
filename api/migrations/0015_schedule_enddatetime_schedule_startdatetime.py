# Generated by Django 4.1 on 2022-11-22 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_schedule_enddatetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='endDateTime',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='schedule',
            name='startDateTime',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]
