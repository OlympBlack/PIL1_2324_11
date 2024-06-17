# Generated by Django 5.0.6 on 2024-06-16 12:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZzDiscussions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_message_id', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'zz_discussions',
            },
        ),
        migrations.CreateModel(
            name='ZzHobbys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'zz_hobbys',
            },
        ),
        migrations.CreateModel(
            name='ZzLangages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'zz_langages',
            },
        ),
        migrations.CreateModel(
            name='ZzMedias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('type', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'zz_medias',
            },
        ),
        migrations.CreateModel(
            name='ZzUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('pseudo', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('created_at', models.DateTimeField()),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('nom', models.CharField(blank=True, max_length=255, null=True)),
                ('prenom', models.CharField(blank=True, max_length=255, null=True)),
                ('birthday', models.DateField()),
                ('bio', models.TextField(blank=True, null=True)),
                ('sex', models.CharField(blank=True, max_length=22, null=True)),
                ('plage', models.CharField(blank=True, max_length=2, null=True)),
                ('astre', models.CharField(blank=True, max_length=10, null=True)),
                ('religion', models.CharField(blank=True, max_length=10, null=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('hobby', models.JSONField(blank=True, null=True)),
                ('pref', models.JSONField(blank=True, null=True)),
                ('online', models.BooleanField(blank=True, null=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'zz_users',
            },
        ),
        migrations.CreateModel(
            name='ZzMessages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('discussion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commondatab.zzdiscussions')),
                ('media', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='commondatab.zzmedias')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='commondatab.zzmessages')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'zz_messages',
            },
        ),
        migrations.CreateModel(
            name='ZzFriendship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lik', models.PositiveIntegerField()),
                ('liked', models.ForeignKey(db_column='liked', on_delete=django.db.models.deletion.CASCADE, related_name='zzfriendship_liked_set', to=settings.AUTH_USER_MODEL)),
                ('liker', models.ForeignKey(db_column='liker', on_delete=django.db.models.deletion.CASCADE, related_name='zzfriendship_liker_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'zz_friendship',
                'unique_together': {('liker', 'liked', 'lik')},
            },
        ),
        migrations.CreateModel(
            name='ZzUsersDiscussions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('lastdate', models.DateTimeField(blank=True, null=True)),
                ('discussion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commondatab.zzdiscussions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'zz_users_discussions',
                'unique_together': {('user', 'discussion')},
            },
        ),
        migrations.CreateModel(
            name='ZzUsersLangages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.PositiveIntegerField()),
                ('langage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commondatab.zzlangages')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'zz_users_langages',
                'unique_together': {('user', 'langage', 'type')},
            },
        ),
        migrations.CreateModel(
            name='ZzUsersMedias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal', models.PositiveIntegerField(blank=True, null=True)),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commondatab.zzmedias')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'zz_users_medias',
                'unique_together': {('user', 'media')},
            },
        ),
    ]