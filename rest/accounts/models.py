from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=25)
    is_verified = models.BooleanField(default=False)
    email_token = models.CharField( max_length=100 , null=True , blank=True)
    forget_password = models.CharField(max_length=100 , null=True , blank= True)
    last_login_time = models.DateTimeField(null=True , blank=True)
    last_logout_time = models.DateTimeField(null=True , blank = True) 
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
