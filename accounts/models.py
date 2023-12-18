from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, full_name, email ,username,  password=None):
        if not email:
            raise ValueError("User must have an email address!")
        if not username:
            raise ValueError("User must have an email address!")
        user = self.model(
            email = self.normalize_email(email), 
            full_name = full_name, 
            username = username,
            password = password,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, full_name, email , password, username):
        user = self.create_user(
            email = self.normalize_email(email), 
            full_name = full_name, 
            password = password,
            username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True, blank=True)
    is_admin = models.BooleanField(default=False, blank=True)
    is_active = models.BooleanField(default=False, blank=True)
    is_superadmin = models.BooleanField(default=False, blank=True)
    is_staff = models.BooleanField(default=False, blank=True)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'username']

    def __str__(self):
        return self.full_name
    
    objects = MyAccountManager()

    def has_perm(self, perm , obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True