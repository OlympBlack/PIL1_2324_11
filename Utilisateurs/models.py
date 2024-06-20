from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    # Ajoutez des champs supplémentaires si nécessaire

    # Assurez-vous de spécifier des noms d'accès inverses uniques
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # Changer ce nom pour éviter le conflit
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_user_permissions',  # Changer ce nom pour éviter le conflit
        blank=True
    )
