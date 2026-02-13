from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    # Avoid clashes with default auth.User
    groups = models.ManyToManyField(
        Group,
        related_name='jobs_user_set',  # change this
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='jobs_user_permissions_set',  # change this
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username
