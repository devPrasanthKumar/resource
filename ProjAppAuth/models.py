from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
import uuid


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(_('email address'), max_length=40, unique=True)
    USER_MODE = [
        ("admin", "Admin"),
        ("moderator", "Moderator"),
        ("normaluser", "NormalUser")
    ]

    userMode = models.CharField(
        choices=USER_MODE, max_length=20, default="normaluser")
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class CustomPermission(models.Model):
    can_edit = models.BooleanField(default=True)
    can_delete = models.BooleanField(default=False)
    userName = models.OneToOneField(User, on_delete=models.CASCADE)
