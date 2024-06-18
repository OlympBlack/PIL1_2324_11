from django.db import models
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime
class ZzUsersManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class ZzUsers(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    pseudo = models.CharField(unique=True, max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    nom = models.CharField(max_length=255, blank=True, null=True)
    prenom = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    sex = models.CharField(max_length=22, blank=True, null=True)
    plage = models.CharField(max_length=2, blank=True, null=True)
    astre = models.CharField(max_length=10, blank=True, null=True)
    religion = models.CharField(max_length=10, blank=True, null=True)
    longitude = models.FloatField(default=6.321)
    latitude = models.FloatField(default=2.981)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    hobby = models.JSONField(blank=True, null=True)
    pref = models.JSONField(blank=True, null=True)
    online = models.BooleanField(blank=True, null=True)
    is_superuser=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = ZzUsersManager()
    confirmation_token = models.CharField(max_length=100, blank=True, null=True)

    def generate_confirmation_token(self):
        token = get_random_string(length=30)  # Génère un token aléatoire
        self.confirmation_token = token
        self.save()
        return token
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['pseudo']

    class Meta:
        db_table = 'zz_users'

class ZzFriendship(models.Model):
    liker = models.ForeignKey('ZzUsers', models.CASCADE, db_column='liker', related_name='zzfriendship_liker_set')
    liked = models.ForeignKey('ZzUsers', models.CASCADE, db_column='liked', related_name='zzfriendship_liked_set')
    lik = models.PositiveIntegerField()

    class Meta:
        
        db_table = 'zz_friendship'
        unique_together = (('liker', 'liked', 'lik'),)

class ZzDiscussions(models.Model):
    last_message_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'zz_discussions'

class ZzLangages(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'zz_langages'

class ZzHobbys(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'zz_hobbys'

class ZzMedias(models.Model):
    path = models.CharField(unique=True, max_length=255)
    type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        
        db_table = 'zz_medias'

class ZzMessages(models.Model):
    content = models.TextField()
    media = models.ForeignKey(ZzMedias, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey('ZzUsers', models.DO_NOTHING)
    discussion = models.ForeignKey(ZzDiscussions, models.CASCADE)
    message = models.ForeignKey('self', models.DO_NOTHING)

    class Meta:
        
        db_table = 'zz_messages'

class ZzUsersDiscussions(models.Model):
    user = models.ForeignKey(ZzUsers, models.CASCADE)
    discussion = models.ForeignKey(ZzDiscussions, models.CASCADE)
    status = models.IntegerField()
    lastdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        
        db_table = 'zz_users_discussions'
        unique_together = (('user', 'discussion'),)

class ZzUsersLangages(models.Model):
    user = models.ForeignKey(ZzUsers, models.CASCADE)
    langage = models.ForeignKey(ZzLangages, models.CASCADE)
    type = models.PositiveIntegerField()

    class Meta:
        
        db_table = 'zz_users_langages'
        unique_together = (('user', 'langage', 'type'),)

class ZzUsersMedias(models.Model):
    user = models.ForeignKey(ZzUsers, models.CASCADE)
    media = models.ForeignKey(ZzMedias, models.CASCADE)
    principal = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'zz_users_medias'
        unique_together = (('user', 'media'),)






