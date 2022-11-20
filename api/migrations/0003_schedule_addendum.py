# Generated by Django 4.1 on 2022-11-02 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_schedule_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='addendum',
            field=models.ForeignKey(blank=True, db_column='addendum_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule_set', to='api.orderaddendum'),
        ),
    ]