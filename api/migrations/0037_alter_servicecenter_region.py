# Generated by Django 4.1 on 2022-12-28 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_alter_technician_centers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecenter',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='centers', to='api.region'),
        ),
    ]