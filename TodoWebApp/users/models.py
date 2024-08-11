from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_("email address"), unique=True)
#
#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = []
#
#     objects = CustomUserManager()
#
#     def __str__(self):
#         return self.email


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=48)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

