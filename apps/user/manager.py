import re
from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def create_user(self, email, first_name, last_name, description=None, image=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Email kiriting')
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise ValueError('Kiritilgan email manzili to\'g\'ri emas')
        if not first_name:
            raise ValueError('Ismingizni kiriting')
        if not last_name:
            raise ValueError('Familiyangizni kiriting')
        
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, description=description, image=image, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, description=None, image=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Email kiriting')
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            raise ValueError('Kiritilgan email manzili to\'g\'ri emas')
        if not first_name:
            raise ValueError('Ismingizni kiriting')
        if not last_name:
            raise ValueError('Familiyangizni kiriting')
        
        user = self.create_user(email, first_name, last_name, description, image, password, **extra_fields)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user