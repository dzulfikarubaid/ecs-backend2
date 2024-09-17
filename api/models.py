from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    payment_status = models.BooleanField(default=False)
    modul = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.username+" | "+self.name+" | "+self.email+" | "+str(self.payment_status)+" | "+self.modul