from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserProfile(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  isActive = models.BooleanField(default=True)
  isStaff = models.BooleanField(default=False)
  
  objects = UserProfileManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['name']

  def getFullName(self):
    return self.name

  def getShortName(self):
    return self.name

  def __str__(self):
    return self.email

