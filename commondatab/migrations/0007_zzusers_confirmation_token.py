# Generated by Django 5.0.1 on 2024-06-17 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commondatab', '0006_alter_zzusers_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='zzusers',
            name='confirmation_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
