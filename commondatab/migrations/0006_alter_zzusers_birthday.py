# Generated by Django 5.0.6 on 2024-06-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commondatab', '0005_alter_zzusers_latitude_alter_zzusers_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zzusers',
            name='birthday',
            field=models.DateField(),
        ),
    ]
