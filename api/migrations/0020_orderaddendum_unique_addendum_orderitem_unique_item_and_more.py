# Generated by Django 4.1 on 2022-12-01 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_workweek_unique_weeks'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='orderaddendum',
            constraint=models.UniqueConstraint(fields=('number', 'sequence'), name='unique_addendum'),
        ),
        migrations.AddConstraint(
            model_name='orderitem',
            constraint=models.UniqueConstraint(fields=('number', 'addendum'), name='unique_item'),
        ),
        migrations.AddConstraint(
            model_name='ordersequence',
            constraint=models.UniqueConstraint(fields=('number', 'region'), name='unique_sequence'),
        ),
    ]