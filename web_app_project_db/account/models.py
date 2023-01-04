from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomAccountManager(BaseUserManager):

    def create_admin(self, email, user_name, password, status):

        status.setdefault('is_superuser', True)

        if status.get('is_superuser') is not True:
            raise ValueError(
                'Admin must be assigned to is_superuser=True')

        return self.create_user(self, email, user_name, password, status)

    def create_user(self, email, user_name, password, status):

        user = self.model(email=email, user_name=user_name, status=status)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    # Delivery details
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=150, blank=True)
    # User Status
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.user_name
