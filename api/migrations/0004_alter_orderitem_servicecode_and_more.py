# Generated by Django 4.1 on 2022-10-03 15:07

import api.models.fields.Fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_abstractlocation_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='serviceCode',
            field=api.models.fields.Fields.ServiceCodeField(max_length=2),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='warrantyCode',
            field=api.models.fields.Fields.WarrantyCodeField(max_length=1),
        ),
    ]