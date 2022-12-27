# Generated by Django 4.1 on 2022-12-27 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_manager_region'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='ordersequence',
            name='unique_sequence',
        ),
        migrations.AddConstraint(
            model_name='ordersequence',
            constraint=models.UniqueConstraint(fields=('number', 'jobSite'), name='unique_sequence'),
        ),
    ]