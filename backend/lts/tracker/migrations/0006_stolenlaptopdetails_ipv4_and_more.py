# Generated by Django 5.0.3 on 2024-04-07 19:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_stolenlaptopdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='stolenlaptopdetails',
            name='ipv4',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='stolenlaptopdetails',
            name='location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stolenlaptopdetails',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stolenlaptopdetails',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stolen_laptop_details', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='police_id',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
