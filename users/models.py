from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings

class User(AbstractUser):
    ROLES = (
        ('read', 'Read'),
        ('write', 'Write'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=5, choices=ROLES, default='read')
    email = models.EmailField(unique=True)
    
    # To resolve the conflict with the default `User` model, add `related_name`
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',  # Custom related_name to avoid conflict
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Custom related_name to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
        related_query_name='user'
    )

    blocked_users = models.ManyToManyField(
        'self', symmetrical=False, related_name='blocked_by'
    )
    def __str__(self):
        return self.username
class UserActivity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)  # e.g., 'friend_request_sent'
    description = models.TextField()  # Description of the activity
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user} - {self.activity_type} - {self.timestamp}'


