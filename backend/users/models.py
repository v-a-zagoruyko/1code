from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=64, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=11, null=True, blank=True)

    def __str__(self):
        return self.user.full_name()