# Generated by Django 4.1 on 2022-12-28 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_remove_zipcode_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='zipcode',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='zipCodes', to='api.region'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='api.region'),
        ),
        migrations.RemoveField(
            model_name='zipcode',
            name='city',
        ),
        migrations.AddField(
            model_name='zipcode',
            name='city',
            field=models.ManyToManyField(related_name='zipCodes', to='api.city'),
        ),
    ]
