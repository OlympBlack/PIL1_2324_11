# Generated by Django 5.0.1 on 2024-06-20 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('commondatab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zzusers',
            name='profile_media',
            field=models.FileField(blank=True, null=True, upload_to='profile_media/'),
        ),
        migrations.AlterField(
            model_name='zzusers',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='zzusers',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='zzusers_groups', to='auth.group'),
        ),
        migrations.AlterField(
            model_name='zzusers',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='zzusers_user_permissions', to='auth.permission'),
        ),
    ]
