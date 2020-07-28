from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManger(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("email must be included..")
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length=222, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    name = models.CharField(max_length=220)
    objects = UserManger()
    USERNAME_FIELD = 'email'

