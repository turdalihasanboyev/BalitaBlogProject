from django.db import models
from apps.common.models import BaseModel
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from .manager import CustomUserManager


class CustomUser(BaseModel, AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='user_images/', default='images/default-user-image.png')

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        if self.email:
            return f"{self.email}"

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'