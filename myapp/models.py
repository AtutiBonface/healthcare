from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.utils import timezone


class CustomAccountManager(BaseUserManager):

    def create_user(self, email , username,password=None ,**other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email ,username,password ,**other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)      

        return self.create_user(email, username,password, **other_fields) 


class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length = 150,null=True,blank=True)
    email = models.EmailField(unique = 'True')    
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username']

    objects = CustomAccountManager()

    def __str__(self):
        return f'{self.username}'
    
