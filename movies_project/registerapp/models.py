from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Users(AbstractUser):
    phone_number = models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.USERNAME_FIELD



