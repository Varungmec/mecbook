from django.db import models
from django.contrib.auth.models import User
    # Create your models here.

class Visitor(models.Model):
   user = models.OneToOneField(User,default=None,on_delete=models.CASCADE)
  # blood_group = models.CharField(max_length=30,default=None)  
   age=models.IntegerField(default=None)    

